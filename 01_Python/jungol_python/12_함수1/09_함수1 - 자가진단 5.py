# 함수1 - 자가진단 5
# https://jungol.co.kr/problem/9459?cursor=MTYsMTIsOQ==


def func(g, a):
    match g:
        case 'M' | 'm':
            if a >= 20:
                return "MAN"
            else:
                return "BOY"
        case 'F' | 'f':
            if a >= 20:
                return "WOMAN"
            else:
                return "GIRL"

g, a = input().split()
print(func(g, int(a)))