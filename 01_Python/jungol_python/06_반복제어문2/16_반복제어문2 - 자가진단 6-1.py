# 반복제어문2 - 자가진단 6-1
# https://jungol.co.kr/problem/9305?cursor=MTYsNiwxNg==


n = int(input())

i = 0
two, three = 0, 0

while i < n:
    num = int(input())
    (two := two + 1) and (three := three + 1) if num % 3 == 0 else (two := two + 1) if num % 2 == 0 else num % 3 == 0 and (three := three + 1)
    i += 1
# # ==================Todo====================
# while i < n:
#     num = int(input())
#     two_cnt, three_cnt = (two := two + 1), (three := three + 1)
#     two_cnt and three_cnt if num % 3 == 0 else two_cnt if num % 2 == 0 else num % 3 == 0 and three_cnt
#     i += 1
# # ========================================

# while i < n:
#     num = int(input())
#     if num % 2 == 0:
#         two += 1ㄱ
#     if num % 3 == 0:
#         three += 1
#     i += 1

# while i < n:
#     num = int(input())
#     (two := two + 1) if num % 2 == 0 else 0
#     (three := three + 1) if num % 3 == 0 else 0
#     i += 1

# while i < n:
#     num = int(input())
#     num % 2 == 0 and (two := two + 1)
#     num % 3 == 0 and (three := three + 1)
#     i += 1

print('2의 배수:', two)
print('3의 배수:', three)