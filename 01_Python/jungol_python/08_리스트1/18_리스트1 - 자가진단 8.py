# 리스트1 - 자가진단 8
# https://jungol.co.kr/problem/9366?cursor=MTYsOCwxOA==


list_a = []

for i in range(5):
    list_a.append(int(input()))
print(list_a)


for i in range(0, len(list_a), 2):
    print(list_a[i], end=' ')