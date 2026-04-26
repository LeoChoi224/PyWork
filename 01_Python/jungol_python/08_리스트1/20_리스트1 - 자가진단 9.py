# 리스트1 - 자가진단 9
# https://jungol.co.kr/problem/9368?cursor=MTYsOCwyMA==


list_a = []
n = int(input())

for i in range(n):
    list_a.append(int(input()))

print(sorted(list_a, reverse=True))