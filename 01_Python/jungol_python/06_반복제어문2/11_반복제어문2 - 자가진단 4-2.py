# 반복제어문2 - 자가진단 4-2
# https://jungol.co.kr/problem/9301?cursor=MTYsNiwxMQ==


s, e = map(int, input().split())
k = int(input())

for i in range(s, e - 1, -k):
        print(i, end=' ')