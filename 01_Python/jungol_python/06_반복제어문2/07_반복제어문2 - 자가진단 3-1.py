# 반복제어문2 - 자가진단 3-1
# https://jungol.co.kr/problem/9297?cursor=MTYsNiw3


s, e = map(int, input().split())

for i in range(s, e + 1):
    if i % 2 == 0:
        print(i, end=' ')