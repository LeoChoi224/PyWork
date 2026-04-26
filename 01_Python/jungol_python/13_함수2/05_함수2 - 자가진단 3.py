# 함수2 - 자가진단 3
# https://jungol.co.kr/problem/9476?cursor=MTYsMTMsNQ==


def func(n):
    import math

    max_idx, min_idx, other = -1, -1, -1,
    for i in range(len(n)):
        if max(n) == n[i]:
            n[i] = math.ceil(n[i])
            max_idx = i
        elif min(n) == n[i]:
            n[i] = math.floor(n[i])
            min_idx = i
        else:
            n[i] = round(n[i])
            other = i

    print(n[max_idx], n[min_idx], n[other])

func(list(map(float, input().split())))