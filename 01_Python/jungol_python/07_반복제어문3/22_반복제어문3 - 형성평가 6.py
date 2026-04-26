# 반복제어문3 - 형성평가 6
# https://jungol.co.kr/problem/9346?cursor=MTYsNywyMg==


n = int(input())
odd = 1

for i in range(n):
    for j in range(n):
        print(odd, end= ' ')
        odd = (odd + 2) % 10
    print()