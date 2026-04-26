# 반복제어문3 - 형성평가 5
# https://jungol.co.kr/problem/9345?cursor=MTYsNywyMQ==


n = int(input())

for i in range(n, 0, -1):
    for j in range(0, n - i + 1):
        print('#', end= ' ')
    print()

for i in range(n, 0, -1):
    for j in range(0, n - i + 1):
        print(' ', end= ' ')
    for j in range(n - j - 1):
        print('#', end=' ')
    print()