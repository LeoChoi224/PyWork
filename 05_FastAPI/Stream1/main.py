import sys
from dotenv import load_dotenv
load_dotenv()

# Windows 콘솔(cp949 등)에서 이모지/유니코드 print 시 UnicodeEncodeError 방지
# - Windows의 기본 콘솔 인코딩은 cp949(또는 cp65001이 아닌 코드페이지)인 경우가 많아,
#   LangChain/LangGraph 등이 콘솔에 이모지나 특수 유니코드 문자를 출력하면 에러가 발생할 수 있다.
# - sys.stdout.encoding이 이미 "utf-8"이 아니라면 표준 출력/에러 스트림을 utf-8로 재설정한다.
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

# controllers.py: 실제 LangGraph Agent를 호출하고 SSE(Server-Sent Events) 형태로
# 응답을 스트리밍해주는 비즈니스 로직이 들어있는 모듈
from controllers import stream_company_analysis

# schemas.py: 요청 바디의 형태(pydantic 모델)를 정의해 둔 모듈
from schemas import CompanyAnalysisRequest

# FastAPI 애플리케이션 인스턴스 생성. title은 자동 생성되는 API 문서(Swagger UI)의 제목으로 쓰인다.
app = FastAPI(title="LangChain Agent Streaming API")

# CORS(Cross-Origin Resource Sharing) 설정.
# 프론트엔드(Vite 개발 서버, 보통 5173/5174 포트)와 백엔드(보통 8000 포트)가
# 서로 다른 origin(포트)에서 실행되므로, 브라우저가 요청을 차단하지 않도록 허용해줘야 한다.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,  # 쿠키/인증정보를 포함한 요청을 허용
    allow_methods=["*"],  # GET, POST 등 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 요청 헤더 허용
)

@app.post("/api/analyze")
async def analyze_company(payload: CompanyAnalysisRequest, request: Request):
    # StreamingResponse: 응답 전체를 한 번에 만들지 않고,
    # 비동기 제너레이터(stream_company_analysis)가
    # 데이터를 만들어내는 즉시 클라이언트로 조각조각(chunk) 전송한다.

    return StreamingResponse(
        stream_company_analysis(payload.company_name, request),  # AsyncGenerator

        # text/event-stream: SSE(Server-Sent Events) 프로토콜임을 명시하는 MIME 타입.
        # 프론트엔드는 이 형식("event: ...\ndata: ...\n\n")에 맞춰 직접 파싱한다.
        media_type="text/event-stream",

        headers={
            "Cache-Control": "no-cache",  # 스트리밍 응답을 브라우저가 캐시하지 않도록 설정
            "X-Accel-Buffering": "no",   # nginx 등에서 응답을 버퍼링 하지 말고 즉시 전달
        }
    )