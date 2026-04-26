# 함수2 - 자가진단 2
# https://jungol.co.kr/problem/9474?cursor=MTYsMTMsMw==


def func(a, b):
    if type(1) == type(a):
        if abs(a) > abs(b):
            return a 
        else:
            return b
    else:
       if abs(a) > abs(b):
        return b
       else:
        return a

n, m = map(int, input().split())
print(func(n, m))
n, m = map(float, input().split())
print(func(n, m))