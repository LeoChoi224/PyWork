# 반복제어문2 - 자가진단 7-2
# https://jungol.co.kr/problem/9309?cursor=MTYsNiwyMA==


n = int(input())

for i in range(n):
    for j in range(1, n + 1):
        print(j - 2, end=' ')
    print()