# 리스트2 - 연습문제 7
# https://jungol.co.kr/problem/9416?cursor=MTYsMTAsMTM=


list_a = []
list_b = []
list_c = []

for i in range(3):
    list_a = list(map(int, input().split()))
    list_b = list_b + [list_a]

for i in range(3):
    list_a = list(map(int, input().split()))
    list_c = list_c + [list_a]

for i in range(3):
    for j in range(2):
        print(list_b[i][j] + list_c[i][j], end=' ')
    print()