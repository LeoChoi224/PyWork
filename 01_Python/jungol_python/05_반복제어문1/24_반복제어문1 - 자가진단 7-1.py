# 반복제어문1 - 자가진단 7-1
# https://jungol.co.kr/problem/9280?cursor=MTYsNSwyNA==


n = int(input())

i = 0
while i < 4:
    i += 1
    if i == n:
        continue
    print(i)