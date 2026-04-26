# 선택제어문 - 자가진단 1-2
# https://jungol.co.kr/problem/9225?cursor=MTYsMywy


n = int(input())
m = int(input())

print(n + m) or print("ODD") if n % 2 != 0 or m % 2 != 0 else print(n + m)