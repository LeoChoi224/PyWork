# 리스트1 - 형성평가 3
# https://jungol.co.kr/problem/9371?cursor=MTYsOCwyMw==



list_a = []
list_b = []

a, b = map(int, input().split())
for i in range(b):
    list_a.append(a)

a, b = map(int, input().split())
for i in range(b):
    list_b.append(a)

print(list_a + list_b)