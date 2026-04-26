# 리스트1 - 자가진단 1-2
# https://jungol.co.kr/problem/9352?cursor=MTYsOCwy


list = []

for i in range(50):
    list.append(int(input()))

for i in range(1, len(list) + 1):
    print(list[-i], end=' ')
