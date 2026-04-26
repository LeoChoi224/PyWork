# 리스트1 - 어디어디 숨었나
# https://jungol.co.kr/problem/9375?cursor=MTYsOCwyNw==



list_a = []
n = int(input())

for i in range(n):
    list = list_a.append(int(input()))

k = int(input())

for i in range(len(list_a)):
    if list_a[i] == k:
        print(i + 1, end=' ')