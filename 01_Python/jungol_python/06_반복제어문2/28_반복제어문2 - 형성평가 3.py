# 반복제어문2 - 형성평가 3
# https://jungol.co.kr/problem/9317?cursor=MTYsNiwyOA==


n = int(input())

sum = 0
for i in range(1, n +1):
    if i % 5 == 0:
        print(i, end=' ')
        sum += i

print(f"\n{sum}")