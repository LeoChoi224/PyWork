# 리스트2 - 자가진단 7
# https://jungol.co.kr/problem/9417?cursor=MTYsMTAsMTQ=


list_a = []
list_b = []
list_c = []

for i in range(2):
    list_a = list(map(int, input().split()))
    list_b = list_b + [list_a]

for i in range(2):
    list_a = list(map(int, input().split()))
    list_c = list_c + [list_a]

for i in range(2):
    list_a = []
    for j in range(4):
        list_a.append(list_b[i][j] * list_c[i][j])
    print(list_a)