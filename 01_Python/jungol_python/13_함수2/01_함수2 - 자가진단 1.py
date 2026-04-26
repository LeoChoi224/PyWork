# 함수2 - 자가진단 1
# https://jungol.co.kr/problem/9472?cursor=MTYsMTMsMQ==


def func(n):
    print(max(n) - min(n))

n, m, l, k, j = map(int, input().split())
func([n, m, l, k, j])