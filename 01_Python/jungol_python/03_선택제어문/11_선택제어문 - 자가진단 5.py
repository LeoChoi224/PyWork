# 선택제어문 - 자가진단 5
# https://jungol.co.kr/problem/9234?cursor=MTYsMywxMQ==


x, y = map(float, input().split())

if x >= 4.0 and y >= 4.0:
    print('A grade')
elif x >= 3.0 and y >= 3.0:
    print('B grade')
else:
    print('F grade')
