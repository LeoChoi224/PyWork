# 선택제어문 - 연습문제 5
# https://jungol.co.kr/problem/9233?cursor=MTYsMywxMA==


a = int(input())
b = int(input())

if a >= 3 and b >= 3:
    print('High')
elif a < 3 or b < 3:
    print('Low')
else:
    print('Mid')

# if a >= 3 and b >= 3:
#     print('High')
# elif a >= 3 or b >= 3:
#     print('Mid')
# else:
#     print('Low')