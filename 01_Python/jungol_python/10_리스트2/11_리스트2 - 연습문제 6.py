# 리스트2 - 연습문제 6
# https://jungol.co.kr/problem/9414?cursor=MTYsMTAsMTE=

list = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0 ,0]]
list[0][0] = 1
list[1][1] = 2
list[2][2] = 3
list[1][3] = 4
list[0][4] = 5

for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j], end=' ')
    print()