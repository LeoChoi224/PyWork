# 리스트1 - 자가진단 7-2
# https://jungol.co.kr/problem/9364?cursor=MTYsOCwxNg==


list_a = []
list_a = list(input().split())
print(list_a)

list_a += list_a[1:]
list_a += list_a[1]

print(list_a)