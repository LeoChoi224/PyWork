# 함수2 - 자가진단 6
# https://jungol.co.kr/problem/9482?cursor=MTYsMTMsMTE=


def func(*agrs):
    for i in range(len(agrs) - 1, 0, -1):
        print(agrs[i], end=' ')

n = int(input())
list_a = []

for i in range(n):
    list_a.append(input())

func(list_a)