# 선택제어문 - 형성평가 3
# https://jungol.co.kr/problem/9242?cursor=MTYsMywxOA==


year = int(input())

if year % 4 == 0:
    print("common year") if year % 100 == 0 and year % 400 != 0 else print("leap year") 
else:
    print("common year")