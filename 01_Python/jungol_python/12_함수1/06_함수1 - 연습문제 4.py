# 함수1 - 연습문제 4
# https://jungol.co.kr/problem/9456?cursor=MTYsMTIsNg==


def func(x, a, b, c):
    return (a * (x ** 2)) + (b * x) + c

a, b, c = map(int, input().split())
print(func(2, a, b, c))
print(func(3, a, b, c))
print(func(5, a, b, c))