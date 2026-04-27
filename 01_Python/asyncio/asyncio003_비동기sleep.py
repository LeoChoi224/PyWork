import asyncio
import time

async def async_work(icon, seconds=0):
  print(f'{icon} {seconds}초 작업 시작')
  start = time.time()  # 현재 시간 저장 (단위. 초)
  
#   asyncio.sleep(seconds)  # 시간이 걸리는 작업
#     # 비동기 함수인데 await 를 붙이지 않으면?
#     # 기다리지 않고 다음 코드 진행.   warning 발생.  
#     # coroutine 'sleep' was never awaited 

  # ⭐️ await 는 async 함수 에서만 사용 가능!
  await asyncio.sleep(seconds)
  
  end = time.time()
  print(f'{icon} 작업종료: {end - start:.3f}초 소요')
  return f'{icon}-{seconds} 작업' # 비동기 함수의 리턴값.

# asyncio.run(async_work('🍆', 3))

async def async_all():
#   task1 = asyncio.create_task(async_work('🍆', 3))
#   task2 = asyncio.create_task(async_work('🍊', 1))
#   task3 = asyncio.create_task(async_work('🥦', 2))

#   await task1
#   await task2
#   await task3
#   results = await asyncio.gather(task1, task2, task3) # gather() 는 각 비동기 작업의 리턴값들을 리턴.
#   print(results)

    data = [('🍆', 3), ('🍊', 1), ('🥦', 2)]
    tasks = [asyncio.create_task(async_work(icon, seconds)) for icon, seconds in data]
    results = await asyncio.gather(*tasks)
    print(results)

start = time.time()
asyncio.run(async_all())
end = time.time()
print(f'>>> 총 경과시간: {end - start}')

print('\n' * 10, '🟨프로그램 종료')
