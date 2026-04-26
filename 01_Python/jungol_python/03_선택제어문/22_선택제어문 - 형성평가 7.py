# 선택제어문 - 형성평가 7
# https://jungol.co.kr/problem/9246?cursor=MTYsMywyMg==


a, b, c = map(int, input().split())
max, min = a , a

if max < b:
    if b < c:
        max = c
    else:
        max = b
else:
    if max < c:
        max = c

if min > b:
    print(max - c) if b > c else print(max -  b)
else:
    print(max - c) if min > c else print(max - min)