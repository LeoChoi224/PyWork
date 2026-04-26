# 반복제어문2 - 형성평가 2
# https://jungol.co.kr/problem/9316?cursor=MTYsNiwyNw==


n , a = map(int, input().split())

if n > a:
    n, a = n, a
else:
    n, a = a, n
for i in range(a, n + 1):
    print(i, end=' ')