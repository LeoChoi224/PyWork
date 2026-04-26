# 선택제어문 - 자가진단 4
# https://jungol.co.kr/problem/9232?cursor=MTYsMyw5

weight = float(input())

if weight <= 50.80:
    print('Flyweight')
elif weight <= 61.23:
    print('Lightweight')
elif weight <= 72.57:
    print('Middleweight')
elif weight <= 88.45:
    print('Cruiserweight')
else:
    print('Heavyweight')


if weight > 88.45:
    print('Heavyweight')
elif weight > 72.57:
    print('Cruiserweight')
elif weight > 61.23:
    print('Middleweight')
elif weight > 50.45:
    print('Lightweight')
else:
    print('Flyweight')
