# 반복제어문2 - 형성평가 8
# https://jungol.co.kr/problem/9322?cursor=MTYsNiwzMw==


n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"({i}, {j}) ", end='')
    print()