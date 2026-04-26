# 반복제어문3 - 자가진단 3
# https://jungol.co.kr/problem/9330?cursor=MTYsNyw2


n = int(input())

for i in range(n):
    print(' ' * i, end='')
    for j in range(n - i, 0, -1):
        print('*', end='')
    print()