import asyncio
import time

def sync_work(icon, seconds=0):
  print(f'{icon} {seconds}초 작업 시작')
  start = time.time()  # 현재 시간 저장 (단위. 초)
  time.sleep(seconds)  # 시간이 걸리는 작업
  end = time.time()
  print(f'{icon} 작업종료: {end - start:.3f}초 소요')


def sync_all():
    sync_work('🍆', 3)
    sync_work('🍊', 1)
    sync_work('🥦', 2)


start = time.time()
sync_all()
end = time.time()
print(f'>>> 총 경과시간: {end - start}')