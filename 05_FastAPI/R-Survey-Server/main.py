from contextlib import asynccontextmanager
from fastapi import FastAPI
import models, controllers
from fastapi.middleware.cors import CORSMiddleware
from database import engine  # AsyncEngine을 가져온다고 가정

# 테이블 생성을 위한 비동기 함수 정의
async def init_db():
    async with engine.begin() as conn:
        # run_sync를 통해 동기 메서드인 create_all을 실행합니다.
        await conn.run_sync(models.Base.metadata.create_all)

# FastAPI 시작 시 실행되도록 설정 (수정된 부분)
# 기존의 models.Base.metadata.create_all(database.engine) 코드는 삭제하거나 주석 처리하세요.

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 서버 시작 시 테이블 생성
    await init_db()
    yield
    # 서버 종료 시 실행할 코드가 있다면 여기에 작성

app = FastAPI(lifespan=lifespan)


# React 프론트엔드 연동을 위한 CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)

app.include_router(controllers.router)

@app.get("/")
def root():
    return {"message": "설문조사 CRUD. /survey 로 이동해보세요"}
