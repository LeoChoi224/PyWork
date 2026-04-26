# 함수2 - 연습문제 2
# https://jungol.co.kr/problem/9473?cursor=MTYsMTMsMg==


def func():
    n = list(map(int, input().split()))
    print(sum(map(abs, n)))

func()