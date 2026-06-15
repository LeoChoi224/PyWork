from models import Book
import asyncio
import sys
from sqlalchemy import func, select
from database import engine, AsyncSessionLocal, Base


SAMPLE_BOOKS = [
    {"title": "객체지향의 사실과 오해", "author": "조영호"},
    {"title": "클린 코드", "author": "로버트 마틴"},
    {"title": "이펙티브 파이썬", "author": "브렛 슬라킨"},
    {"title": "FastAPI를 사용한 파이썬 웹 개발", "author": "압둘라지즈 압둘라지즈 아디"},
    {"title": "혼자 공부하는 파이썬", "author": "윤인성"},
    {"title": "Do it! 점프 투 파이썬", "author": "박응용"},
    {"title": "리팩터링", "author": "마틴 파울러"},
]

def create_samples():
    # 테이블이 없으면 생성
    Base.metadata.create_all(engine)

    with AsyncSessionLocal() as session:
        books = [Book(**data) for data in SAMPLE_BOOKS]
        session.add_all(books)
        session.commit()

if __name__ == "__main__":
    create_samples()
