# 반복제어문1 - 자가진단 4-1
# https://jungol.co.kr/problem/9271?cursor=MTYsNSwxNQ==


s, e = map(int, input().split())

for n in range(s, e + 1):
    if n % 2 != 0:
        print(n)