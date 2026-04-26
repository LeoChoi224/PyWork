# 반복제어문3 - 자가진단 5-2
# https://jungol.co.kr/problem/9336?cursor=MTYsNywxMg==


a, b = map(ord, input().split())

if a > b :
    a, b = b, a
for ch in range(a, b + 1): print(chr(ch), end=' ')