# 리스트1 - 자가진단 3
# https://jungol.co.kr/problem/9357?cursor=MTYsOCw3


list = []

for i in range(5):
    list.append(int(input()))

print(list)
del(list[-2:])
print(list)