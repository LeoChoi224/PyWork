# 반복제어문1 - 자가진단 5
# https://jungol.co.kr/problem/9274?cursor=MTYsNSwxOA==


n = int(input())
i, sum = 1, 0
while i <= n:
    sum += i
    i += 1

print(sum)