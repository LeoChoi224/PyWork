# 리스트2 - 자가진단 8
# https://jungol.co.kr/problem/9419?cursor=MTYsMTAsMTY=

# TODO 파스칼 삼각형

list = [[0] * 5 for n in range(5)]

print(list)

for i in range(5):
    for j in range(5):
        if i == 0 or j == 0:
            list[i][j] = 1
        else:
            list[i][j] = list[i-1][j] + list[i][j-1]

for row in list:
    for num in row:
        print(num, end=' ')
    print()