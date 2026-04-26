# 리스트1 - 형성평가 7
# https://jungol.co.kr/problem/9375?cursor=MTYsOCwyNw==


list_a = []

n = int(input())
for i in range(n):
    list_a.append(int(input()))

is_sort = 1

for i in range(len(list_a)):
    if i != 0:
        if list_a[i - 1] >= list_a[i]:
            is_sort -= 1
            break

print("YES" if is_sort else "NO")