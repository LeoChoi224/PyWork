# 반복제어문3 - 형성평가 3
# https://jungol.co.kr/problem/9343?cursor=MTYsNywxOQ==


n = int(input())

for i in range(2, (n * 2) + 1, 2):
    for j in range((n * 2) - i, 0, -1):
        print(' ', end= '')

    for j in range(1, (i // 2) + 1):
        print(j, end=' ')

    print()
