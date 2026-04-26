# 함수1 - 형성평가 3
# https://jungol.co.kr/problem/9466?cursor=MTYsMTIsMTY=


def func(n):
    for i in range(1, n ** 2 + 1, n):
        for j in range(n):
            print(i + j, end=' ')
        print()

func(int(input()))