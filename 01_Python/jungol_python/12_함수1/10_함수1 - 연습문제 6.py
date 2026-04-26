# 함수1 - 연습문제 6
# https://jungol.co.kr/problem/9460?cursor=MTYsMTIsMTA=


def func(a, b):
    a, b = b, a
    print(f"함수 내부: a = {a}, b = {b}")

a, b = map(int, input().split())
func(a, b)
print(f"함수 외부: a = {a}, b = {b}")
func(a, b)
print(f"함수 외부: a = {b}, b = {a}")