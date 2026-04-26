# 선택제어문 - 자가진단 7
# https://jungol.co.kr/problem/9239?cursor=MTYsMywxNQ==


min, a, b = map(int, input().split())

if min > a:
    print(b) if a > b else print(a)
else:
    print(b) if min > b else print(min)