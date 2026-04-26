# 반복제어문3 - 자가진단 5-1
# https://jungol.co.kr/problem/9335?cursor=MTYsNywxMQ==


a, b = map(ord, input().split())

if a > b :
    for ch in range(a, b - 1, -1):
        print(chr(ch), end=' ')
else:
    for ch in range(a, b + 1):
        print(chr(ch), end=' ')