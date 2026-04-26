# 리스트1 - 자가진단 5
# https://jungol.co.kr/problem/7104?cursor=MTYsOCwxMQ==


list_a = []

for i in range(5):
    list_a.append(int(input()))

list_b = list_a[::-1]
list_c = list_b.copy()
list_c.append(int(input()))

print(f"A = {list_a}")
print(f"B = {list_b}")
print(f"C = {list_c}")