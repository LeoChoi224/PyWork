import os, time
from dotenv import load_dotenv

load_dotenv()

# macOS에서 FAISS 사용 시 발생하는 OpenMP 중복 초기화 오류(libomp.dylib 충돌) 방지 설정
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

print(f'✅ {os.path.basename( __file__ )} 실행됨 {time.strftime('%Y-%m-%d %H:%M:%S')}')  # 실행파일명, 현재시간출력
print(f'\tOPENAI_API_KEY={os.getenv("OPENAI_API_KEY")[:20]}...') # OPENAI_API_KEY 필요!
#─────────────────────────────────────────────────────────────────────────────────────────
import streamlit as st

from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings.base import OpenAIEmbeddings
from langchain_core.runnables.passthrough import RunnablePassthrough
from langchain_core.runnables.base import RunnableLambda
from langchain_openai.chat_models.base import ChatOpenAI
from langchain_core.prompts.chat import ChatPromptTemplate

from langchain_community.document_loaders.sitemap import SitemapLoader

# ────────────────────────────────────────
# 🎃 LLM 로직
# ────────────────────────────────────────
llm = ChatOpenAI(
    temperature=0.1,
)

answers_prompt = ChatPromptTemplate.from_template("""
    Using ONLY the following context answer the user's question. If you can't just say you don't know, don't make anything up.
                                                 
    Then, give a score to the answer between 0 and 5.

    If the answer answers the user question the score should be high, else it should be low.

    Make sure to always include the answer's score even if it's 0.

    Context: {context}
                                                 
    Examples:
                                                 
    Question: How far away is the moon?
    Answer: The moon is 384,400 km away.
    Score: 5
                                                 
    Question: How far away is the sun?
    Answer: I don't know
    Score: 0
                                                 
    Your turn!

    Question: {question}
""")

choose_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            # 먼저 생성된 answer 들만을 사용하여 사용자의 question 에 답변하세요
            # 더 높은 점수를 가진 답변들을 사용하세요 (더 유용합니다)
            # 최신의 자료를 우선시하고, 출처도 남겨주세요.
            """
            Use ONLY the following pre-existing answers to answer the user's question.

            Choose one answer that have the highest score (more helpful) and favor the most recent ones.

            Cite sources and return the sources as it is.  Do not change them. Keep is as a link

            Answers: {answers}
            """,
        ),
        ("human", "{question}"),
    ]
)



# ────────────────────────────────────────
# 🍇 file load & cache
# ────────────────────────────────────────

# 입력: 웹페이지를 로딩한 BeautifulSoup 객체
# 리턴값: Document 객체에 담을 text
def parse_page(soup):
    header = soup.find("header")   # <header> element
    footer = soup.find("footer")  # <footer>

    if header:
        header.decompose()
    if footer:
        footer.decompose()

    return soup.get_text().replace("\n", " ")


@st.cache_resource(show_spinner="Fetching URL...")
def load_website(url):
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1000,
        chunk_overlap=200,
    )

    loader = SitemapLoader(
            url,
            # data 를 load 하고 싶은 url 들을 담을 list. url 은 정규표현식으로 인식된다.
            # filter_urls=[
            #     # "https://stability.ai/news-updates/meet-stable-audio-3-the-model-family-built-for-artistic-experimentation-with-open-weight-models"

            #     # 정규표현식 사용
            #     r"^(.*\/news-updates\/).*",

            #     # ?! <- negative lookahead   /news-updates/ 를 포함하지 않는 url 만
            #     # r"^(?!.*\/news-updates\/).*",
            # ],
            parsing_function=parse_page,
        )
    loader.max_depth = 10  # 수업시간 depth 1  (기본값 10)
    loader.headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36'}
    docs = loader.load_and_split(text_splitter=splitter)  # 페이지 크롤링 -> List[Document] 리턴   기본적으로 html <tag> 는 제거된 형태 

    vector_store = FAISS.from_documents(
        documents=docs,
        # ★명심. cache 를 만들때..
        #   다른 sitemap 에서 얻은 각각의 URL 마다 별도의 cache를 만들어야 한다
        embedding=OpenAIEmbeddings(),
    )

    return vector_store.as_retriever()


def get_answers(inputs):
    docs = inputs['docs']
    question = inputs['question']

    answers_chain = answers_prompt | llm

    answers = {
        "question": question,
        "answers": [
                        {
                            "answer": answers_chain.invoke({
                                        "question": question,
                                        "context": doc.page_content,
                                    }).content,
                            "source": doc.metadata['source'],
                            "date": doc.metadata['lastmod'],
                        }
                        for doc in docs
                    ]
    }
    return answers

def choose_answer(inputs):
    answers = inputs["answers"]
    question = inputs["question"]

    choose_chain = choose_prompt | llm

    condensed = "\n\n".join(
        f"{answer['answer']}\nSource:{answer['source']}\nDate:{answer['date']}\n"
        for answer in answers
    )

    # st.write(condensed)  # 확인용

    return choose_chain.invoke({
        "question": question,
        "answers": condensed,
    })

# ────────────────────────────────────────
# ⭕ Streamlit 로직
# ────────────────────────────────────────
st.set_page_config(
    page_title="SiteGPT",
    page_icon="🖥️",
)

st.markdown(
"""
    # SiteGPT
            
    Ask questions about the content of a website.
            
    Start by writing the URL of the website on the sidebar.
"""
)

with st.sidebar:
    url = st.text_input(
        "Write down a URL",
        placeholder="https://example.com",
    )


if url:
    if ".xml" not in url:
        with st.sidebar:
            st.error("Please write down a Sitemap URL")

    else:
        retriever = load_website(url)
        query = st.text_input("Ask a question to the website")
        if query:
        
            chain = {
                "docs": retriever,
                "question": RunnablePassthrough(),
            } | RunnableLambda(get_answers) | RunnableLambda(choose_answer)

            result = chain.invoke(query)
            st.markdown(result.content)




    