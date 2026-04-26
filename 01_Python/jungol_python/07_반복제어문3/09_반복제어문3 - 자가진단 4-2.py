# 반복제어문3 - 자가진단 4-2
# https://jungol.co.kr/problem/9333?cursor=MTYsNyw5


n = int(input())

for i in range(0, (n + 1) // 2):
    print(' ' * i * 4, end='')
    for j in range(1, (n + 1) - (i * 2)):
            print('*', end=' ')
    print()

for i in range((n // 2) - 1, -1, -1):
    print(' ' * i * 4, end='')
    for j in range(1, (n + 1) - (i * 2)):
            print('*', end=' ')
    print()


print('=' * 20)
# 파이썬st 코드
n = int(input())
part1 = [" ".join(" " * (n - i)  + "*" * i) for i in range(n, 0, -2)]
part1 += part1[::-1][1:]
print("\n".join(part1))