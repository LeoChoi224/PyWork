# 선택제어문 - 형성평가 5
# https://jungol.co.kr/problem/9244?cursor=MTYsMywyMA==


month = int(input())

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(31)
    case 4 | 6 | 9 | 11:
        print(30)
    case 2:
        print(28)