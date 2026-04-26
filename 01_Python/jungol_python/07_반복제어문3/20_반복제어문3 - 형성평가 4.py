# 반복제어문3 - 형성평가 4
# https://jungol.co.kr/problem/9344?cursor=MTYsNywyMA==


n = int(input())

ch, num = ord('Z'), 0

for i in range(n):
    for j in range(0, n - i):
        print(chr(ch), end= ' ')
        ch -= 1

    for j in range(0, n - j - 1):
        print(num, end=' ')
        num += 1

    print()