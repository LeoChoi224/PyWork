# 반복제어문3 - 형성평가 2
# https://jungol.co.kr/problem/9342?cursor=MTYsNywxOA==


# n = int(input())
n = 5
for i in range(n, 0, -2):
    for j in range(1, n + 1):
        if j >= i:
            print('*', end='')
        else:
            print(' ', end= '')
    print()
for i in range(2, n, 2):
    print(' ' * i, end='')
    for j in range(n - i, 0, -1):
        print('*', end='')
    print()