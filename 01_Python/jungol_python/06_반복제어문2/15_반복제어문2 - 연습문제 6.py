# 반복제어문2 - 연습문제 6
# https://jungol.co.kr/problem/7102?cursor=MTYsNiwxNQ==


n = int(input())

odd, even = 0, 0

for i in range(0, n):
    n = int(input())
    if n % 2 == 0:
        even += 1
    else:
        odd += n

print(odd, even)