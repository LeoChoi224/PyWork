# 반복제어문2 - 연습문제 8
# https://jungol.co.kr/problem/9312?cursor=MTYsNiwyMw==

mul = 1
while mul <= 9:
    dan = 5
    while dan <= 7:
        print(f'{dan} * {mul} = {mul * dan}', end="   ")
        dan += 1
    print()
    mul += 1