# LangGraph 를 사용한 DocumentGPT + Memory 구현 
# 매 대화 턴마다 생성한 그래프가 실행되도록 작성
import os
import time
from dotenv import load_dotenv

load_dotenv()

# macOS에서 FAISS 사용 시 OpenMP 중복 초기화 오류(libomp.dylib 충돌) 방지
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

print(f'✅ {os.path.basename( __file__ )} 실행됨 {time.strftime('%Y-%m-%d %H:%M:%S')}')  
print(f'\tOPENAI_API_KEY={os.getenv("OPENAI_API_KEY")[:20]}...') 

import streamlit as st

from typing import Dict, Any, Annotated
from pydantic import BaseModel, Field

from langchain_core.prompts.chat import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai.chat_models.base import ChatOpenAI
from langchain_community.document_loaders.unstructured import UnstructuredFileLoader
from langchain_classic.embeddings import CacheBackedEmbeddings
from langchain_openai.embeddings.base import OpenAIEmbeddings
from langchain_classic.storage import LocalFileStore 
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.callbacks.base import BaseCallbackHandler

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver

# ────────────────────────────────────────
# 🎃 LLM 로직
# ────────────────────────────────────────
class ChatCallbackHandler(BaseCallbackHandler):
    def on_llm_start(self, *args, **kwrags):
        self.message = ""  
        self.message_box = st.empty()

    def on_llm_end(self, *args, **kwargs):
        save_message(self.message, "ai")
    
    def on_llm_new_token(self, token, *args, **kwargs):
        self.message += token
        self.message_box.markdown(self.message)

llm = ChatOpenAI(
    temperature=0.1,
    streaming=True,
    callbacks=[ChatCallbackHandler()],
)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
    Answer the question using ONLY the following context. 
    If you don't know the answer just say you don't know. DON'T make anything up.            
    If the question is about our conversation, answer using the conversation history below.

    Context: {context}
    """),
    MessagesPlaceholder(variable_name='history'),
    ("human", "{question}")
])


# ────────────────────────────────────────
# 🎃 그래프 상태 정의
# ────────────────────────────────────────
class GraphState(BaseModel):
    question: str = Field(default="", description="이번 턴의 사용자 질문")
    context: str = Field(default="", description="retriever 가 찾아온 문서 내용")
    answer: str = Field(default="", description="이번 턴의 최종 답변")
    messages: Annotated[list, add_messages] = Field(
        default_factory=list,
        description="누적되는 대화 내역 (= 메모리)",
    )


# ────────────────────────────────────────
# 🎃 노드 생성
# ────────────────────────────────────────
def retrieve(state: GraphState) -> Dict[str, Any]:
    """검색 노드 : 업로드한 파일에서 관련 문서 조각을 찾아 context를 업데이트"""
    retriever = st.session_state['retriever']
    docs = retriever.invoke(state.question)
    print(f'🔵 retrieve : {len(docs)}개 문서 조각 검색됨')

    return {"context": format_docs(docs)}


def generate(state: GraphState) -> Dict[str, Any]:
    """답변 노드 : context + 대화 내역으로 LLM이 답변"""
    chain = prompt | llm
    response = chain.invoke({
        "context": state.context,
        "history": state.messages,
        "question": state.question,
    })

    return {
        "answer": response.content,
        "messages": [
            HumanMessage(content=state.question),
            AIMessage(content=response.content),
        ],
    }


# ────────────────────────────────────────
# 🎃 그래프 생성
# ────────────────────────────────────────
@st.cache_resource(show_spinner="Building graph...")
def create_graph():

    checkpointer = InMemorySaver()
    workflow = StateGraph(GraphState)

    # 노드 추가
    workflow.add_node("retrieve", retrieve)
    workflow.add_node("generate", generate)

    # 엣지 연결
    workflow.add_edge(START, "retrieve")
    workflow.add_edge("retrieve", "generate")
    workflow.add_edge("generate", END)

    app = workflow.compile(checkpointer=checkpointer)

    return app


# ────────────────────────────────────────
# 🍇 file load & cache
# ────────────────────────────────────────
upload_dir = r'./.cache/files'
embedding_dir = r'./.cache/embedding'
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)
if not os.path.exists(embedding_dir):
    os.makedirs(embedding_dir)

@st.cache_resource(show_spinner="Embedding file...")
def embed_file(file):
    print('🔵 embed_file 호출', file.name)
    
    file_content = file.read()
    file_path = os.path.join(upload_dir, file.name)
    with open(file_path, 'wb') as f:
        f.write(file_content)
    
    splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n",
        chunk_size=600,
        chunk_overlap=100,
    )
    loader = UnstructuredFileLoader(file_path)
    docs = loader.load_and_split(text_splitter=splitter)
    
    embeddings = OpenAIEmbeddings()
    cache_dir = LocalFileStore(os.path.join(embedding_dir, file.name))  
    cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings, cache_dir)

    vectorstore = FAISS.from_documents(docs, cached_embeddings)
    retriever = vectorstore.as_retriever()
    return retriever


# ────────────────────────────────────────
# ⭕ Streamlit 로직
# ────────────────────────────────────────
st.set_page_config(
    page_title="DocumentGPT",
    page_icon="📃",
)

st.title("Document GPT")

if "thread_id" not in st.session_state:
    st.session_state['thread_id'] = 'documentgpt-1'

def save_message(message, role):
    st.session_state['messages'].append({'message': message, 'role': role})

def send_message(message, role, save=True):
    with st.chat_message(role):
        st.markdown(message)
    if save:
        save_message(message, role)        

def paint_history():
    for message in st.session_state['messages']:
        send_message(message['message'], message['role'], save=False)

def format_docs(docs):
    return "\n\n".join(document.page_content for document in docs)

with st.sidebar:
    file = st.file_uploader(
        label="Upload a .txt .pdf or .docx file",
        type=["pdf", "txt", "docx"],
    )

if file:
    st.session_state['retriever'] = embed_file(file)   # 노드에서 꺼내 쓴다

    # 그래프 생성. CompiledStateGraph 객체
    app = create_graph()

    # InMemorySaver 사용을 위한 config 설정. config는 '매 실행마다 전달'되어야 한다.
    config = {"configurable": {"thread_id": "st.session_state['thread_id']"}}

    send_message('준비되었습니다. 질문해보세요!', 'ai', save=False)
    paint_history()
    message = st.chat_input("업로드 한 file 에 대해 질문을 남겨보세요...")
    if message:
        send_message(message, 'human')

        with st.chat_message('ai'):
            # 그래프 실행 (매 대화 턴마다)
            # messages 를 안 넘겨도 체크포인터가 thread_id 로 불러와 합쳐준다.
            app.invoke({"question": message}, config)

else:
    st.session_state['messages'] = []  
    st.session_state['thread_id'] = f'documentgpt-{time.time()}'


