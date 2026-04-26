# 반복제어문2 - 홀수
# https://jungol.co.kr/problem/1392?cursor=MTYsNiwzNg==


sum, min = 0, 100

for i in range(7):
    n = int(input())
    if n % 2 != 0:
        sum += n
        if n < min:
            min = n
print(-1 if sum == 0 else f"{sum}\n{min}")
