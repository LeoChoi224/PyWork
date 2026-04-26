# 반복제어문2 - 자가진단 7-4
# https://jungol.co.kr/problem/9311?cursor=MTYsNiwyMg==


n = int(input())

for i in range(n):
    for j in range(n, 0, -1):
        print(j - n + i, end=' ')
    print()