# 반복제어문3 - 자가진단 2-2
# https://jungol.co.kr/problem/9326?cursor=MTYsNyw0


n = int(input())

for i in range(n):
    for j in range(n - i, 0, -1):
        print('*', end=' ')
    print()