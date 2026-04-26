# 리스트2 - 형성평가 5
# https://jungol.co.kr/problem/9424?cursor=MTYsMTAsMjE=


list = [[0] * 5 for n in range(5)]

for i in range(0, 5, 2):
    list[0][i] = 1

for i in range(1, len(list)):
    for j in range(len(list[i])):
        if j <= 0:
            list[i][j] = list[i - 1][j + 1]
        elif j >= len(list[i]) - 1:
            list[i][j] = list[i - 1][j - 1]
        else:
            list[i][j] = list[i - 1][j - 1] + list[i - 1][j + 1]

for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j], end=' ')
    print()