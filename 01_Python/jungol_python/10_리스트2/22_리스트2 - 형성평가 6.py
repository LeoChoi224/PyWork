# 리스트2 - 형성평가 6
# https://jungol.co.kr/problem/9425?cursor=MTYsMTAsMjI=


list_a = []

for i in range(3):
    list_a.append(list(input().split()))

for i in range(len(list_a)):
    for j in range(len(list_a[i])):
        print(chr(ord(list_a[i][j]) + 32), end=' ')
    print()