# Windows 콘솔(cp949 등)에서 이모지/한글 print가 깨지지 않도록 표준출력을 UTF-8로 고정
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# FastAPI 서버
from pathlib import Path
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

# 랭체인, 랭그래프
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# MCP 클라이언트 
from contextlib import asynccontextmanager
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import ClientSession
import httpx
from mcp.client.streamable_http import streamable_http_client

# 환경변수
from dotenv import load_dotenv
load_dotenv()

# ------------------------------------------------
# 🟦 프롬프트 템플릿 

# 에이전트의 역할과 사용 가능한 도구를 정의하는 시스템 프롬프트를 생성합니다. 
# 나중에 create_agent() 의  prompt= 에 전달할 문자열(str) 로 리턴해야 한다
# "금토깽"이라는 이름과 각 도구의 기능을 명시하여 에이전트가 적절히 활용할 수 있도록 합니다. 
def create_prompt_template(tools) -> str:
    """에이전트를 위한 시스템 프롬프트(문자열)를 생성합니다."""
    tool_descriptions = "\n".join(f"- {t.name}: {t.description}" for t in tools)

    system_prompt = f"""
당신은 친절하고 도움이 되는 AI 어시스턴트 "금토깽"입니다. 

다음과 같은 도구들을 활용하여 사용자를 도와드릴 수 있습니다:

사용 가능한 도구:
{tool_descriptions}

사용자가 위치한 곳을 안다면 바로 brief_today() 도구의 지침을 따르면 됩니다. 아니라면, 위치를 물어보고나서 도구의 지침을 따릅니다. 

사용자와의 대화에서 다음 원칙을 지켜주세요:
1. 항상 친절하고 정중한 태도로 응답해주세요
2. 사용자의 질문을 정확히 이해하고 관련된 도구를 적절히 활용해주세요
3. 최신 뉴스를 요청받으면, 도구의 출력을 그대로 출력하면 됩니다.
4. 응답은 명확하고 이해하기 쉽게 구성해주세요
5. 필요시 추가 정보나 설명을 제공하여 사용자에게 더 나은 도움을 주세요
6. 링크가 포함된 정보를 제공할 때는 [제목](URL) 형태의 마크다운 링크로 제공해주세요
"""
    return system_prompt

# -----------------------------------------------
# 🟦 에이전트 생성

def build_agent_executor(tools):
    """주어진 도구들을 사용하여 에이전트를 생성"""
    memory = InMemorySaver()  # 체크포인터 사용
    prompt = create_prompt_template(tools)  # tools 전달.  ✨반드시 str 이어야 함.
    llm = ChatOpenAI(model='gpt-4o')

    agent_executor = create_agent(
        model=llm,
        tools=tools, 
        system_prompt=prompt,   # 시스템프롬프트, ✨반드시 str 이어야 함.
        checkpointer=memory,
    )

    return agent_executor 


# ------------------------------------------
# 🟦 에이전트 사용 준비

# 우리가 만드는 채팅 에이전트는 FastAPI 기반의 웹 서버 상에서 동작하는 에이전트입니다. 
# FastAPI의 lifespan 기능을 사용하면 애플리케이션 시작 '전'과 '후'의 동작을 제어할 수 있습니다. 
# MCP 서버에 연결하고, 도구를 로드한 뒤, 에이전트 실행기를 생성하는 준비 과정을 담당합니다.

http_client = httpx.AsyncClient(timeout=30.0)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI 애플리케이션의 생명주기 동안 MCP 연결 및 에이전트 설정을 관리합니다."""
    print("🔵 애플리케이션 시작: MCP 서버에 연결하고 에이전트를 설정합니다...")

    async with streamable_http_client(
        url = "http://localhost:8000/mcp",
        http_client=http_client,
    ) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)

            # app.state 란? 
            # FastAPI는 내부적으로 Starlette을 쓰는데, app.state는 그냥 빈 네임스페이스 객체. 
            # 속성을 자유롭게 붙였다 뗐다 할 수 있는 컨테이너
            #  라우트 핸들러에서는 request.app.state.agent_executor로 어디서든 똑같은 객체에 접근할 수 있습니다.
            app.state.agent_executor = build_agent_executor(tools) # 에이전트 생성
            print("🔵 에이전트 설정 완료. 애플리케이션이 준비 되었습니다")
            yield

    print('🔵 애플리케이션 종료')
    app.state.agent_executor = None


app = FastAPI(lifespan=lifespan)

# chat_agent.py 파일의 위치를 기준으로 정적 파일 마운트
static_path = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=static_path), name="static")

# chat_agent.py 파일의 위치를 기준으로 templates 디렉토리의 절대 경로를 계산하여 설정
templates_path = Path(__file__).resolve().parent / "templates"
templates = Jinja2Templates(directory=templates_path)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):  # 라우팅 함수는 Request 객체 받을수 있다.
    """메인 채팅 페이지를 렌더링"""
    return templates.TemplateResponse(request, "index.html")


# 채팅 API 엔드포인드
@app.post("/chat")
async def chat(request: Request, message: str = Form(...), session_id: str = Form(...)):
    """사용자 메시지를 받아 에이전트의 응답을 스트리밍 합니다."""
    agent_executor = request.app.state.agent_executor

    # 🔷TODO: 스트링밍 응답

    return ""



# ▼ 메인 실행 부분
# uvicorn을 사용하여 FastAPI 앱을 포트 8001에서 실행합니다. 
# MCP 서버가 8000번 포트를 사용하므로 다른 포트를 사용합니다.
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8001)

# python 명령으로 실행하기

