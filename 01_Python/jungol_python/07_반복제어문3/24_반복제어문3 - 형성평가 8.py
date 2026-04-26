# 반복제어문3 - 형성평가 8
# https://jungol.co.kr/problem/9349?cursor=MTYsNywyNA==


# n = int(input())
n=2

str, end = ord('a'), ord('z')
for i in range(str, end + 1):
    if (i - 96) % n == 0:
        print(chr(i), end='')