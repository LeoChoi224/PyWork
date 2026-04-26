# 리스트1 - 자가진단 6
# https://jungol.co.kr/problem/9361?cursor=MTYsOCwxMw==


list_a = []
list_b = []
list_c = []

list_a = list(map(int, input().split()))

list_b = list_a[::-1]
list_c = list_a[::2] or list_c

print(f"A = {list_a}")
print(f"B = {list_b}")
print(f"C = {list_c}")