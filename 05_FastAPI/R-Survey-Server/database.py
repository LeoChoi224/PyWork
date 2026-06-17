# DB 연결 설정
import os
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# .env 파일의 환경 변수를 로드
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")

# 데이터베이스 URL 정의
DATABASE_URL = f'mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# 엔진 생성
engine = create_async_engine(DATABASE_URL, echo=True)

# 세션 생성
AsyncSessionLocal = async_sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine,
    expire_on_commit=False,
)

# Base 클래스생성
class Base(DeclarativeBase):
    pass

# Session 주입
async def get_db():
    """요청마다 세션을 생성하고, 끝나면 자동으로 close 되는 의존함수"""
    async with AsyncSessionLocal() as session:
        yield session
