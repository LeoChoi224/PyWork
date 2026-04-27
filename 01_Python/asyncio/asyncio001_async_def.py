"""
동기(synchronous) 프로그래밍 과 비동기(asynchronous) 프로그래밍은 
작업을 처리하고 결과를 기다리는 방식에 대한 개념


🌐 1. 동기 프로그래밍 (Synchronous Programming)
    개념:
      작업을 순차적으로 처리함.
      앞의 작업이 끝나야 다음 작업을 시작함.
      결과가 올 때까지 기다림.
    
    장점:
      디버깅이 상대적으로 쉬움.
    
    단점:
      '시간이 오래 걸리는 작업'이 있으면 전체 흐름이 멈춤.
        - ex) 네트워크/웹 통신 I/O, DB I/O, 파일 I/O 등.. (IO bound 작업 이라 함)
      사용자 경험이 나쁠 수 있음 (예: UI 멈춤).  
      '비동기 프로그래밍' 이나 '멀티쓰레딩' 으로 해결해야 한다.

⚡ 2. 비동기 프로그래밍 (Asynchronous Programming)
    개념:
      작업을 백그라운드에서 처리하고, 나중에 결과가 도착하면 알림을 받음.
      기다리지 않고 다음 작업을 바로 실행함.
    
    장점:
      긴 작업 중에도 다른 작업을 동시에 수행할 수 있음.
      자원을 더 효율적으로 사용 가능 (특히 I/O 작업에 적합).
    
    단점:
      코드 흐름이 복잡해질 수 있음 (콜백 지옥,  async/await 등).
      디버깅이 어려움.

"""
None

"""
파이썬 3.4에서 asyncio 모듈이 표준 라이브러리로 추가되면서 비동기 프로그래밍 가능

파이썬 3.5에서 async / await 키워드가 문법으로 채택이 되면서 
  외부 라이브러리 없이도 비동기 프로그래밍이 가능해졌다.
"""
None

import asyncio
import time

def hello():
    print('🟨 hello python!')

print(hello, type(hello))
hello()


# async def 으로 선언한 함수는 코루틴(coroutin) 을 리턴함.
async def hello():
    print('🟣hello python!')

print(hello, type(hello))
print(hello())  # 코루틴 리턴

# async 함수 호출
asyncio.run(hello())


