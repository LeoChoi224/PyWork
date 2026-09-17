"""
from contextlib import asynccontextmanager
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

이 import들은 MCP 클라이언트를 구현할 때 자주 등장하는 조합이다.
"""

# asynccontextmanager 는
# Python 표준라이브러리의 데코레이터다.
# 일반 제너레이터 함수를 비동기 '컨텍스트매니저' 로 바꿔주는 역할  (context manager -> with 구문 사용 가능한 객체)


from contextlib import asynccontextmanager
import asyncio

@asynccontextmanager
async def my_resource():
    print('🧡1. 진입:리소스 준비')
    yield "💚2. 리소스"
    print('💙3. 종료:리소스 정리')   # with 블럭 끝난뒤 실행 


async def test():
    async with my_resource() as r:
        print('🟡 4. with 시작 --------')
        print(r)
        print('🟡 5. with 종료---------')    

# test() 실행하면 화면에 찍히는 순서?
asyncio.run(test())

# MCP 클라이언트/서버 코드에서 
#    연결 설정 → 사용 → 정리(cleanup) 흐름을 async with로 깔끔하게 감싸기 위해 거의 항상 쓰입니다.    



