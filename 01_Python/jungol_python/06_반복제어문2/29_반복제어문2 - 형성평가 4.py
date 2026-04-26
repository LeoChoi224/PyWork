# 반복제어문2 - 형성평가 4
# https://jungol.co.kr/problem/9318?cursor=MTYsNiwyOQ==



n = int(input())

sum = 0
for i in range(n):
    sum += int(input())

print(f"SUM: {sum}\nAVG: {sum // n}")