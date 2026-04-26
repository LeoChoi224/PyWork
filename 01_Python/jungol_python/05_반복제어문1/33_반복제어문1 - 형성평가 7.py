# 반복제어문1 - 형성평가 7
# https://jungol.co.kr/problem/9289?cursor=MTYsNSwzMw==


cnt, sum = 0, 0

while True:
    n = int(input())

    if n < 1 or n > 5:
        break
    elif n % 2 == 0:
        cnt += 1
        sum += n
    else:
        continue

print(int(sum // cnt))