# 선택제어문 - 연습문제 6
# https://jungol.co.kr/problem/9235?cursor=MTYsMywxMg==


num1, num2, num3 = map(int, input().split())

if num1 > num2:
    if num1 > num3:
        print(f"MAX:", num1)
    else:
        print(f"MAX:", num3)
elif num2 > num3:
    print(f"MAX:", num2)
else:
    print(f"MAX:", num3)
    

# a, b, c = map(int, input().split())

# if b > a:
#     if c > b:
#         max = c
#     else:
#         max = b
# else:
#     if c > a:
#         max = c
#     else:
#         max = a


# print(f'MAX: {max}')
        