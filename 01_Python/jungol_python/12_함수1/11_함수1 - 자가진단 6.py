# 함수1 - 자가진단 6
# https://jungol.co.kr/problem/9461?cursor=MTYsMTIsMTE=


n, m = map(int, input().split())
def func():
    global n, m

    if n < m:
        n, m = n * 2, m // 2
    else:
        n, m = n // 2, m * 2
    return n, m

func()
print(n, m)