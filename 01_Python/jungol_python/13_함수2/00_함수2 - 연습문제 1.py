# 함수2 - 연습문제 1
# https://jungol.co.kr/problem/9471?cursor=MTYsMTMsMA==


def func(n):
    print(f"max: {max(n)}")
    print(f"min: {min(n)}")

n, m, l = map(int, input().split())
func([n, m, l])