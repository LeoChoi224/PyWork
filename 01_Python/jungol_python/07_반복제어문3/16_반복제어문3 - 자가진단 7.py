# 반복제어문3 - 자가진단 7
# https://jungol.co.kr/problem/9340?cursor=MTYsNywxNg==


n = int(input())

num, ch = 0, ord('A')

for i in range(n, 0, -1):
    for j in range(1, (n - i) + 2):
        print(num, end=' ')
        num += 1
    for j in range(i - 1):
        print(chr(ch), end=' ')
        ch += 1

    print()