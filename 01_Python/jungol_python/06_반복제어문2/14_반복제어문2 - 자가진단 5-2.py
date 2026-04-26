# 반복제어문2 - 자가진단 5-2
# https://jungol.co.kr/problem/9304?cursor=MTYsNiwxNA==


n = int(input())

cnt = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        cnt += 1

print(cnt)