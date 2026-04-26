# 반복제어문3 - 자가진단 6
# https://jungol.co.kr/problem/9338?cursor=MTYsNywxNA==


n = int(input())

a = ord('a')

for i in range(0, n):
    for j in range(a, a + (n - i)):
        print(chr(a), end=' ')
        a += 1
    print()