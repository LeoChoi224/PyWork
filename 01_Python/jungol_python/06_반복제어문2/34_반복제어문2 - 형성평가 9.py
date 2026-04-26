# 반복제어문2 - 형성평가 9
# https://jungol.co.kr/problem/9323?cursor=MTYsNiwzNA==


s = int(input())
e = int(input())

if s > e:
    for i in range(1, 10):
        for j in range(s, e - 1, -1):
            print(f"{j} * {i} = {i * j}", end='   ')
        print()
else:
    for i in range(1, 10):
        for j in range(s, e + 1):
            print(f"{j} * {i} = {i * j}", end='   ')
        print()