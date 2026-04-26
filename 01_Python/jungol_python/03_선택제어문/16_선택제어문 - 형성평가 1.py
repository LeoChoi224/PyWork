# 선택제어문 - 형성평가 1
# https://jungol.co.kr/problem/9240?cursor=MTYsMywxNg==


num1, num2 = map(int, input().split())
if num1 >= num2:
    print(num1 - num2)
else:
    print(num2 - num1)