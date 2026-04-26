# 반복제어문3 - 연습문제 3
# https://jungol.co.kr/problem/9329?cursor=MTYsNyw1


for i in range(3, 0, -1):
    for j in range(1,4):
        if j >= i:
            print('*', end='')
        else:
            print(' ', end= '')
    print()
print()