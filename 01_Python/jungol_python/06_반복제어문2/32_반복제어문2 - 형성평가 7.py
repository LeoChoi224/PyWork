# 반복제어문2 - 형성평가 7
# https://jungol.co.kr/problem/9321?cursor=MTYsNiwzMg==


c , r = map(int, input().split())

for i in range(1, c + 1):
    for j in range(1, r + 1):
        print(j * i, end=' ')
    print()