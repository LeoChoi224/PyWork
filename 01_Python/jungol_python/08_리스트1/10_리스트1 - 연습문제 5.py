# 리스트1 - 연습문제 5
# https://jungol.co.kr/problem/7103?cursor=MTYsOCwxMA==


list_a = []

for i in range(5):
    list_a.append(int(input()))

list_b = list_a.copy()
list_c = list_a[::-1]

print(list_c)

for i in range(3):
    list_b.append(int(input()))
print(list_b)

print(list_a)