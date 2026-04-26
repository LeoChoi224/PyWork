# 🟦 순환문
# 특정 코드를 일정 회수 혹은 특정 조건을 만족하는 동안 반복수행하는 경우 사용하는 구문
# 순환문(loop) 혹은 반복문(iteration) 이라고 한다

# 파이썬에는 while, for 순환문이 제공됩니다

print('\n🟦 while 순환문')
# while 순환문 구조,  조건문이 '참' 인 동안 수행문장을 반복수행

# while <조건식>:
#     <수행할 문장1>
#     <수행할 문장2>
#     <수행할 문장3>
#     ...
# else: *** 절대 사용 x ***
#      순환문 빠져나오기 전에 수행

num = 0
while num < 5:
    print(num)
    num += 1

print('종료 num =', num)

print('-' * 20)

num = 0
while num < 5:
    print(num)
    num += 1

print('종료 num =', num)

# 순환문에서 중요한 것은
# 1. 몇번 순환을 하는가?
# 2. 순환하는 동안 변수값의 변화 범위는?
# 3. 순환문 종료후 변수값은?

# 위 순환문의 경우
# 1. 총 5번 순환을 했고
# 2. 순환하는 동안 num 변수값은 0 부터 4 까지 변화
# 3. 순환문 종료시점에서 num 값은 5

# 10 ~ 20 출력
i = 10
while i <= 20:
    print(i, end= " ")
    i += 2

print('\n종료')

# 20 ~ 10 출력
i = 20
while i >= 10:
    print(i, end= " ")
    i -= 1

print('\n종료')

# 구구단 2단을 출력해보자, while  사용
"""
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
"""

i = 1

while i <= 9:
    print(f'2 x {i} = {2 * i}')
    i += 1


# 1 ~ n 까지의 숫자 중에서
# 3과 7의 공배수만 출력
#  => 21 42 63 84

n = 100
i = 1

while i <= n:
    if i % 3 == 0 and i % 7 == 0:
        print(i, end= " ")
    i += 1

print()


print("\n🟦 중첩 순환문 (nested loop)")
# 조건문 안에 조건문 블럭이 들어갈수 있듯이
# 순환문 안에도 얼마든지 순환문이 포함될수 있다..
# 조건문과 순환문 의 어떠한 조합도 가능하다

# 구구단 출력 : 2단 ~ 9단
# 중첩된 while 문

'''
2 x 1 = 2
2 x 2 = 4
...
2 x 9 = 18
3 x 1 = 3
...
4 x 1 = 4
…
...
9 x 9 = 81
'''


i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(f'{i} x {j} = {i * j}')
        j += 1
    print()
    i = i + 1


print('\n🟦 break')
# break
# 순환문 (while, for) 안 에서 순환문을 강제로 종료시키는 키워드

# break 는 감싸고 있는 가장 가까운 순환문을 종료합니다

n = 1
while True: # 무한 루프
    print(n, end=" ")
    
    if n == 100: break
    
    n += 1


print("\n🟦 continue")
# continue
# 순환문 처음으로 돌아가기
# 순환문은 종료하지 않되, 특정 조건만 skip 하는 경우 사용

num = 1
while num <= 10:
    num += 1
    
    if num % 2 == 1:
        continue
    
    print(num)
# num = 1
# while num <= 10:
    # 무한 루프
#     if num % 2 == 1:
#         continue
    
#     num += 1
#     print(num)
