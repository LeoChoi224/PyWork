# 반복제어문1 - 자가진단 2-3
# https://jungol.co.kr/problem/9264?cursor=MTYsNSw4


n = int(input())

for n in range(2, n + 1):
    if n % 2 == 0:
        print(n, end=' ')