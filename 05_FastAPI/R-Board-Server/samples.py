from models import Post
import asyncio
from database import engine, AsyncSessionLocal, Base


SAMPLE_POSTS = [
    {"user": "홍길동", "subject": "가나다라", "content": "마바사아"},
    {"user": "나폴레옹", "subject": "abcd", "content": "efgh"},
    {"user": "아이언맨", "subject": "I am IronMan", "content": "나는 아이언맨"},
    {"user": "캡틴아메리카", "subject": "I am loser", "content": "나는 찌질이"},
]

async def create_samples():
    # 1. 비동기 엔진에서 테이블을 생성하는 올바른 방법
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # 2. await with 대신 'async with' 사용
    async with AsyncSessionLocal() as session:
        posts = [Post(**data) for data in SAMPLE_POSTS]
        session.add_all(posts)
        
        # 3. 데이터베이스에 저장(커밋)할 때도 await 붙이기
        await session.commit()
        print("샘플 데이터 저장 완료!")

if __name__ == "__main__":
    # 4. 비동기 함수를 실행할 때는 asyncio.run()을 사용해야 합니다.
    asyncio.run(create_samples())
    create_samples()
