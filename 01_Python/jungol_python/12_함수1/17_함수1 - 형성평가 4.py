# 함수1 - 형성평가 4
# https://jungol.co.kr/problem/9467?cursor=MTYsMTIsMTc=


def func(n, m):
    return abs(n + m)

n, m = map(int, input().split())
print(func(n, m))