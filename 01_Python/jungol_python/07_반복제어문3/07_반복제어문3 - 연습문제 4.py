# 반복제어문3 - 연습문제 4
# https://jungol.co.kr/problem/9331?cursor=MTYsNyw3


for i in range(2, -1, -1):
    print(' ' * i, end='')
    for j in range(1, 6 - (i * 2)):
            print('*', end='')
    print()
print()