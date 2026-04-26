# 선택제어문 - 형성평가 6
# https://jungol.co.kr/problem/9245?cursor=MTYsMywyMQ==


x = int(input())
y = int(input())
o = input()
result = 0

match o:
    case '+':
        result = x + y
    case '-':
        result = x - y
    case '*':
        result = x * y
    case '%':
        result = x % y

print(f"ans = {result}")

