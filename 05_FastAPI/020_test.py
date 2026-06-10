import time
import asyncio
import aiohttp   # 비동기 HTTP 요청
import requests  # 동기 HTTP 요청

def sync_call(url, times):
    start_time = time.time()
    for _ in range(times):
        requests.get(url)
    lap_time = time.time() - start_time
    print(f"🎃Sync lap time: {lap_time} 초 경과")


async def async_call(url, times):
    start_time = time.time()

    async with aiohttp.ClientSession() as session:   # 비동기 세션 시작
        tasks = []  # 비동기 task 들을 저장할 리스트
        for _ in range(times):
            task = session.get(url)  # 비동기 API 호출하고, task객체 리턴
            tasks.append(task)  # task 객체를 리스트에 추가
        await asyncio.gather(*tasks)  # 모든 비동기 작업이 완료될때까지 기다림

    lap_time = time.time() - start_time
    print(f"🥎Async lap time: {lap_time} 초 경과")
    

if __name__ == "__main__":
    url_sync = "http://127.0.0.1:8000/sync"
    url_async = "http://127.0.0.1:8000/async"
    times = 10

    sync_call(url_sync, times)

    asyncio.run(async_call(url_async, times))