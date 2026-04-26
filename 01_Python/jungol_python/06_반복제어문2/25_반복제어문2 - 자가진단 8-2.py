# 반복제어문2 - 자가진단 8-2
# https://jungol.co.kr/problem/9314?cursor=MTYsNiwyNQ==


n = int(input())

for i in range(1, 10, 3):
    for i in range(i, i + 3):
        print(f"{n} * {i} = {n * i}", end='   ')
    print()