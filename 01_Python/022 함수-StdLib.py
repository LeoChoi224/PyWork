print("\n🟦 Python Standard Library")

# 파이썬 설치시 '기본적'으로 설치된 라이브러리로부터 사용 가능한 함수들

# 라이브러리(library) 란 파이썬 프로그래밍에 사용가능한 프로그램을을 모아놓은 것.

# 모듈을 import 해서 사용한다.

# https://docs.python.org/3/library/index.html    <-- Python Standard Library

print("\n🟦 random 모듈")

import random

for _ in range(10):
    print(random.random()) # 0.0 <= < 1.0 사이의 난수값 리턴 [0.0, 1.0] 0.0은 포함 1.0은 제외

print('-' * 20)

random.seed(43) # seed(k) <- 랜덤 결과값 고정.
for _ in range(10):
    print(random.random())

random.seed(None) # 랜덤 시드값 해제
data = ['dog', 'cat', 'bird', 'fish']
random.shuffle(data)
print(data)

# 로또 1 ~ 45 중에서 랜덤 6개 선택하기
data = [i + 1 for i in range(45)]
print(data)
random.shuffle(data)
print(data[:6])

print('-' * 20)
for _ in range(10):
    print(random.randint(1, 5))

print('-' * 20)

data = ['dog', 'cat', 'bird', 'fish']
for _ in range(5):
    print(random.choice(data))


data = """
권용현
김수림
김정준
문태현
박수연
박영진
박지원
신하석
양정운
이민재
이희본
임지웅
장희준
최홍묵
"""
# 램던으로 8명을 담은 리스트 만들기

data = data.split()
print(data)
random.shuffle(data)
print(data)
print(data[:8])

# list = data.split()
# name = ""
# print(list)
# for i in range(0, 8):
#     name = random.randint(list)
#     if name == list[i]:
#         i -= 1
#         continue
#     print(name)


print('\n🟦 math 모듈')

import math

for d in [
    math.pi,
    math.e,   # 자연로그
    math.radians(180), # 180도 (degree) -> radian
    math.sqrt(4), # 제곱근, 루트

    # math 모듈
    #   ceil(n):  주어진 숫자보다 큰 정수중에 가장 작은 정수
    #   floor(n): 주어진 숫자보다 작은 정수중에 가장 큰 정수
    #   trunc(n): 소숫점 이하 제거
    #   round(n): 기본 내장함수. 반올림 사사오입

    d := [1.2, 1.7, -1.2, -1.7],
    ["ceil", math.ceil(1.2), math.ceil(1.7), math.ceil(-1.2), math.ceil(-1.7)],
    ["floor", math.floor(1.2), math.floor(1.7), math.floor(-1.2), math.floor(-1.7)], 
    ["trunc", math.trunc(1.2), math.trunc(1.7), math.trunc(-1.2), math.trunc(-1.7)], 
    # 파이썬은 사사오입이 아니라,  오사오입. (banker's rounding) 
    #   딱 0.5일때는 가장 가까운 짝수로 반올림 <- (통계적 편향을 줄이기 위해)
    #    round(2.5)  -> 2
    #    round(3.5)  -> 4
    ["round", round(2.5), round(3.5), round(-1.2), round(-1.7)],

    math.sin(math.pi / 2),
    math.cos(math.pi / 2),
    math.tan(math.pi / 2),

]:
    print(d)


print('\n🟦 time 모듈')
import time

for d in [
    time.time(), # 1970.1.1 00:00:00 초 기준으로 경과한 시간 (초)   타임스탬프(time stamp) 라고도 한다
    time.localtime(), #   '현재' 연,월,일, 시,분,초 요일 정보 등을 담고 있다 -> struct_time
    t1 := time.struct_time((2025, 6, 11, 18, 6, 23, 3, 2, 100)),
    time.localtime(time.time()),
    time.localtime(0), # 0 이면 0시 0분 0초 아닌가?  그런데 9시 라 나온다!  왜?  세계표준시 (UTC) 기준  Asia/Seoul 시간은 +9시간이기 때문

    # timestramp 를 -> str 으로 포맷팅
    time.strftime('%x'), # 현재시간 ->mm/dd/yy
    time.strftime('%c'), # 영어권에서 많이 쓰이는
    time.strftime('%Y-%m-%d %H:%M:%S', t1), # 우리나라에서 많이 쓰이는, 두번째 매개변수 = 특정시간 지정
    time.strftime('%Y년%m월%d일 %H시%M분%S초', t1),
    time.strftime('%Y년%m월%d일 %p %I시%M분%S초', t1),

]:print(d)


# 일정시간 delay. sleep() 함수
for i in range(5):
    print(i)
    time.sleep(1) # 이 코드가 끝날때까지 다음 코드가 진행 x -> blocking


print('\n🟦 datetime 모듈')
# 특정 date & time 정보를 가진 객체 생성
# time 모듈과는 목적과 제공되는 level 이 다르다.
#   time -> 시스템 시간 중심. low-level => 기계쪽에 가까운
#   datetime -> 날짜/시간 객체 중심. high-level => 사람쪽에 가까운

import datetime

for d in [
    dt := datetime.datetime(year=2021, month=10, day=20), # datetime 객체 생성

    # str -> datetime 으로 변경
    str1 := '2018-07-23 18:59:09',
    str2 := '2026-04-16 09:23:09',
    dt1 := datetime.datetime.strptime(str1, '%Y-%m-%d %H:%M:%S'),
    dt2 := datetime.datetime.strptime(str2, '%Y-%m-%d %H:%M:%S'),

    # timestamp -> datetime 으로 변경
    timestamp := 1463460958000,  # ms
    dt3 := datetime.datetime.fromtimestamp(timestamp / 1000), # s <- ms

    # datetime -> struct_time으로 변경3
    dt3.timetuple(),

    # datetime -> timestamp으로 변경
    time.mktime(dt3.timetuple()),

    # 비교연산 가능
    dt1 > dt2,
    dt1 < dt2,

]: print(d)


print('\n⭐️ 경과시간 측정')

start_time = time.time()

for i in range(5):
    print(i)
    time.sleep(1)

end_time = time.time()

elapsed_time = end_time - start_time # 경과시간

print(f"{elapsed_time} 초 경과")


print("\n🟦 timedelta")
# 경과시간을 시:분:초  로 나타내려면?

# 물론 일일히 계산 할수도 있다.. 3600 나눈몫이 경과 시간이고..
# 다시 나머지로... 분, 초 계산하고

# 그러나, 파이썬에서는 이를 위한 timedelta 객체가 있다
from datetime import timedelta

for d in [
    # elapsed_time = 10.019780158996582,
    elapsed_time := end_time - start_time, # 경과시간
    timedelta(seconds=elapsed_time),
    td1 := timedelta(seconds=45632),
    td2 := timedelta(seconds=86401), # 하루 = 86400초
    tb := timedelta(seconds=106401),
    tb.days,
    tb.seconds, # 하루(day)를 제외한 나머지 초 (0~86399)
    tb.total_seconds(),

    td1 + td2,
    td2 - td1,

]: print(d)


print('\n' * 15)
