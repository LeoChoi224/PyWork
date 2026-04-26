# 리스트2 - 자가진단 6
# https://jungol.co.kr/problem/9415?cursor=MTYsMTAsMTI=


list_b = []
list_a = []

for i in range(3):
    list_a = list(map(int, input().split()))
    list_b = list_b + [list_a]

row_sum = []
column_sum = []
for i in range(3):
    row, col = 0, 0
    for j in range(3):
        row += list_b[i][j]
        col += list_b[j][i]
    row_sum.append(row)
    column_sum.append(col)

print("row_sum :", end=' ')
for i in row_sum:
    print(i, end=' ')
print()
print("column_sum :", end=' ')
for i in column_sum:
    print(i, end=' ')