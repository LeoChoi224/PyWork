# 함수1 - 형성평가 5
# https://jungol.co.kr/problem/9468?cursor=MTYsMTIsMTg=


def calculator(a, b):
    return (a ** 2) - (b ** 2) if a > b else (b ** 2) - (a ** 2)

a, b = map(int, input().split())
print(calculator(a, b))