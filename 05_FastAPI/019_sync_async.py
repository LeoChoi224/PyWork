from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/sync")
def read_item():
    print('🎃 /sync 호출')
    start_time = time.time()
    time.sleep(1)  # 시간이 많이 걸리는 작업
    lap_time = time.time() - start_time
    print('🎃 /sync 종료', 'lap_time:', lap_time)
    return {"type": "sync", "lap_time": lap_time}

import asyncio

@app.get("/async")
async def read_async_item():
    print("🥎 /async 호출")
    start_time = time.time()
    await asyncio.sleep(1)  # 시간이 많이 걸리는 작업
    lap_time = time.time() - start_time
    print("🥎 /async 종료", 'lap_time:', lap_time)
    return {"type": "async", "lap_time": lap_time}