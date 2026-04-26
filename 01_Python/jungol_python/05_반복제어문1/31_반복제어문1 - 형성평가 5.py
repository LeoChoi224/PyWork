# 반복제어문1 - 형성평가 5
# https://jungol.co.kr/problem/9287?cursor=MTYsNSwzMQ==


a, b = map(int, input().split())

sum = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        sum += i 
print(sum)