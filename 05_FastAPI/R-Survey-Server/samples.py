from models import Survey
import asyncio
from database import engine, AsyncSessionLocal, Base


SAMPLE_SURVEYS = [
    {"name": "홍길동", "age": 21, "gender": "MALE", "area": "서울", "favorite": "고윤정,장원영,카리나"},
    {"name": "최홍묵", "age": 31, "gender": "MALE", "area": "경기도", "favorite": "고윤정"},
    {"name": "아이언맨", "age": 41, "gender": "MALE", "area": "서울", "favorite": "카리나,장원영"},
    {"name": "캡틴아메리카", "age": 71, "gender": "MALE", "area": "서울", "favorite": "카리나"},
]

async def create_samples():
    # 1. 비동기 엔진에서 테이블을 생성하는 올바른 방법
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # 2. await with 대신 'async with' 사용
    async with AsyncSessionLocal() as session:
        surveys = [Survey(**data) for data in SAMPLE_SURVEYS]
        session.add_all(surveys)
        
        # 3. 데이터베이스에 저장(커밋)할 때도 await 붙이기
        await session.commit()
        print("샘플 데이터 저장 완료!")

if __name__ == "__main__":
    # 4. 비동기 함수를 실행할 때는 asyncio.run()을 사용해야 합니다.
    asyncio.run(create_samples())
    create_samples()
