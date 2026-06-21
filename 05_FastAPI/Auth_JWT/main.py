from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
import controllers
from database import engine

# 애플리케이션 구동 시 테이블 생성
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title = "JWT Auth Server")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 프론트엔드 Vite 주소
    allow_credentials=True,  # header 에 인증정보 담겨오는것을 허용
    allow_methods=["*"],
    allow_headers=["*"],
)

# controllers.py 에서 완비된 회원 가입 및 인증 라우팅 세트를 메인 애플리케이션 주체에 마운트(등록)합니다.
app.include_router(controllers.router)