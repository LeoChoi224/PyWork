# 반복제어문3 - 연습문제 6
# https://jungol.co.kr/problem/9337?cursor=MTYsNywxMw==


n = int(input())

a = ord('A')

for i in range(n, 0, -1):
    for j in range(a, a + (n - i + 1)):
        print(chr(a), end='')
        a += 1
    print()