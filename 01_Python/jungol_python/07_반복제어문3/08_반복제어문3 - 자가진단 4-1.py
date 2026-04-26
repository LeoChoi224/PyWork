# 반복제어문3 - 자가진단 4-1
# https://jungol.co.kr/problem/9332?cursor=MTYsNyw4


n = int(input())

for i in range(n):
    print(' ' * i, end='')
    for j in range(1, (n * 2) - (i * 2)):
            print('*', end='')
    print()
print()