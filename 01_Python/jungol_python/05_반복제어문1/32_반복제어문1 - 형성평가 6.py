# 반복제어문1 - 형성평가 6
# https://jungol.co.kr/problem/9288?cursor=MTYsNSwzMg==


cnt, sum = 0, 0

while True:
    n = int(input())
    if n == 0: break
    cnt += 1
    sum += n

print(f"cnt = {cnt}\nsum = {sum}")
