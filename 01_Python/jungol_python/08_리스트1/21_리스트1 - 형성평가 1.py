# 리스트1 - 형성평가 1
# https://jungol.co.kr/problem/9369?cursor=MTYsOCwyMQ==


list_a = []

for i in range(100):
    list_a.append(int(input()))
    if list_a[-1] == -1: break

for i in list_a[-4:-1]:
    print(i, end=' ')