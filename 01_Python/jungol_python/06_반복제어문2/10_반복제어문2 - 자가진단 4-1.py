# 반복제어문2 - 자가진단 4-1
# https://jungol.co.kr/problem/9300?cursor=MTYsNiwxMA==


s, e = map(int, input().split())

for i in range(s, e - 1, -1):
    if i % 2 != 0:
        print(i)