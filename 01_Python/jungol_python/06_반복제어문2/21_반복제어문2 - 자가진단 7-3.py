# 반복제어문2 - 자가진단 7-3
# https://jungol.co.kr/problem/9310?cursor=MTYsNiwyMQ==


n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= n:
        print(i + j, end=" ")
        j += 1
    print()
    i += 1
