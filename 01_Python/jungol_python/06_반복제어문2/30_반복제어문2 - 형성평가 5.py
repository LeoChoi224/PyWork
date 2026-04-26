# 반복제어문2 - 형성평가 5
# https://jungol.co.kr/problem/9319?cursor=MTYsNiwzMA==


n , a = map(int, input().split())

if n > a:
    n, a = n, a
else:
    n, a = a, n

sum, cnt = 0, 0

for i in range(a, n + 1):
    if i % 3 == 0 or i % 5== 0:
        sum += i
        cnt += 1
print(f"""
CNT: {cnt}
SUM: {sum}
""")