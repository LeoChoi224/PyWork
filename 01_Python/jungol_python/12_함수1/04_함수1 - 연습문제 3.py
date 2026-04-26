# 함수1 - 연습문제 3
# https://jungol.co.kr/problem/9454?cursor=MTYsMTIsNA==


def func(n, m):
    print(f"두 수의 합 = {n + m}")
    print(f"두 수의 차 = {abs(n - m)}")

n, m = map(int, input().split())
func(n, m)