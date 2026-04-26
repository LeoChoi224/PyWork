# 함수2 - 연습문제 3
# https://jungol.co.kr/problem/9475?cursor=MTYsMTMsNA==


# TODO 반올림
def func(n):
    import math

    r = (n ** 2) * 3.14
    print(f"원의 넓이\n버림 : {math.floor(r)}")
    print(f"올림 : {math.ceil(r)}\n반올림 : {round(r)}")

func(float(input()))