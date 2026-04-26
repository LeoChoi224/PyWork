# 리스트2 - 형성평가 7
# https://jungol.co.kr/problem/9426?cursor=MTYsMTAsMjM=


n = int(input())
list = [[1] * i for i in range(1, n + 1)]

for i in range(1, len(list)):
    for j in range(1, len(list[i - 1])):
        list[i][j] = list[i - 1][j] + list[i - 1][j - 1]



for i in range(len(list) - 1, 0, -1):
    for j in range(len(list[i])):
        print(list[i][j], end=' ')
    print()
print(list[0][0])