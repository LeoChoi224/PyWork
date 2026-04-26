# 함수1 - 연습문제 5
# https://jungol.co.kr/problem/9458?cursor=MTYsMTIsOA==


def func(n):
    if n == 0:
        print(f"zero")
    else:
        print("positive") if n > 0 else print("negative")

func(int(input()))