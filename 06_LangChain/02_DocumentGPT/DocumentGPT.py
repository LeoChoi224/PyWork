import os
import time
from dotenv import load_dotenv

load_dotenv()

print(f'✅ {os.path.basename( __file__ )} 실행됨 {time.strftime('%Y-%m-%d %H:%M:%S')}')  # 실행파일명, 현재시간출력
print(f'\tOPENAI_API_KEY={os.getenv("OPENAI_API_KEY")[:20]}...') # OPENAI_API_KEY 필요!
#─────────────────────────────────────────────────────────────────────────────────────────
import streamlit as st

from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_openai.chat_models.base import ChatOpenAI
from langchain_core.runnables.base import RunnableLambda
from langchain_core.runnables.passthrough import RunnablePassthrough
from langchain_community.document_loaders.unstructured import UnstructuredFileLoader
from langchain_classic.embeddings import CacheBackedEmbeddings
from langchain_openai.embeddings.base import OpenAIEmbeddings
from langchain_classic.storage import LocalFileStore 
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_faiss import FAISS

# LangChain 의 context 안에 있는 callback handler 는
# 기본적으로 LLM 의 event 를 listen 하는 class 다. 가령.
# ex) LLM 이 무언가를 만들기 시작할때,  작업을 끝낼 때,  LLM 이 글자를 생성하거나,  
#     streaming 할때, LLM 에 에러가 발생할때.. 등등
# callback handler 를 사용하여 log 를 작성하거나 analytics 등으로 보내는 등의 유용한 동작을 구현해볼수 있다.

from langchain_core.callbacks.base import BaseCallbackHandler

# ────────────────────────────────────────
# 🎃 LLM 로직
# ────────────────────────────────────────

class ChatCallbackHandler(BaseCallbackHandler):
    # CallbackHandler 는 event 들을 listen 하는 여러 함수들이 있다.
    # on_xxx() 으로 시작하는 함수들을 오버라이딩 하여 구현한다
    #    ex) LLM 상에서 발생한 event 를 다루는 함수들
    #       chain, retriever, 혹은 agent 에 대한 함수들도 있다.
    #    이벤트핸들러 함수 참조: https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler

    # ↓ on_llm_start() : LLM 작업 시작할때 호출
    #   많은 argument 들이 있지만 이번예제에선 걍 *args, **kwargs 로 받아낸다.
    def on_llm_start(self, *args, **kwrags):
        self.message = ""  # token 들을 채워나갈 빈 문자열
        self.message_box = st.empty()

    # ↓ on_llm_end() : LLM 작업 종료할때 호출
    def on_llm_end(self, *args, **kwargs):
        # LLM 의 답변이 끝나면 메세지를 저장.
        save_message(self.message, "ai")
       
    # ↓ on_llm_new_token() : LLM이 생성해내는 새로운 token 마다 호출
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

    Context: {context}
    """),
    ("human", "{question}")
])


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

    # 업로드된 파일 저장
    file_content = file.read()
    file_path = os.path.join(upload_dir, file.name)
    with open(file_path, 'wb') as f:
        f.write(file_content)

    # Load & Split
    splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n",
        chunk_size=600,
        chunk_overlap=100,
    )
    loader = UnstructuredFileLoader(file_path)
    docs = loader.load_and_split(text_splitter=splitter)

    # embedding & cache & vector store
    embeddings = OpenAIEmbeddings()
    cache_dir = LocalFileStore(os.path.join(embedding_dir, file.name))  # 임베딩은 '파일'별로 만들어 두는게 좋다.
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

def save_message(message, role):
    st.session_state['messages'].append({'message': message, 'role': role})


# 일전에 만들어 봤던것과 같은 메세지 보내는 함수 작성
def send_message(message, role, save=True):
    with st.chat_message(role):
        st.markdown(message)
    if save:
        save_message(message, role)        

# chat history 그리는 함수
def paint_history():
    for message in st.session_state['messages']:
        send_message(message['message'], message['role'], save=False)

# retriever 의 결과를 받아 원하는 포맷으로 리턴 
def format_docs(docs):
    return "\n\n".join(document.page_content for document in docs)

with st.sidebar:
    file = st.file_uploader(
        label="Upload a .txt .pdf or .docx file",
        type=["pdf", "txt", "docx"],
    )

if file:
    retriever = embed_file(file)

    send_message('준비되었습니다. 질문해보세요!', 'ai', save=False)
    paint_history()
    message = st.chat_input("업로드 한 file 에 대해 질문을 남겨보세요...")
    if message:
        send_message(message, 'human')

        chain = (
            {
                "context": retriever | RunnableLambda(format_docs),
                "question": RunnablePassthrough(),
            }
            | prompt
            | llm
        )

        with st.chat_message('ai'):
            chain.invoke(message)


else:
    st.session_state['messages'] = []  # file 이 없거나 삭제되면 chat history 초기화