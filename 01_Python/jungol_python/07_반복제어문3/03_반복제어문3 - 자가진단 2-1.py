# 반복제어문3 - 자가진단 2-1
# https://jungol.co.kr/problem/9328?cursor=MTYsNywz


n = int(input())

for i in range(1, n + 1):
    print('*' * i)
for i in range(n, 0, -1):
    print('*' * i)
