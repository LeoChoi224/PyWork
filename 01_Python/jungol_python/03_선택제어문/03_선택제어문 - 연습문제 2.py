# 선택제어문 - 연습문제 2
# https://jungol.co.kr/problem/9226?cursor=MTYsMywz


a, b = map(int, input().split())
if a > b:
    a, b = b, a
print(a)
print(b)
