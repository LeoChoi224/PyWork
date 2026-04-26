# 리스트2 - 형성평가 4
# https://jungol.co.kr/problem/9423?cursor=MTYsMTAsMjA=


list = list(map(int, input().split()))

for i in range(1, 9):
    list.append((list[i-1] + list[i]) % 10)

for i in list:
    print(i, end=' ')