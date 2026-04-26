# 🟦 제어문 (Control)
#     프로그램의 기본 흐름 변경
#   1. 조건문 Conditional, Branch
#       - if, match~case

#   2. 순환문 Loop, Iteration
#       - for, while


print("🟦 조건문 (if ~ elif ~ else)")


# if 조건식:
#    참일때 수행 구문 블록  (블록이란 문장들의 집합)


# if 조건식:
#    참일때 수행 구문 블록
# else:
#    거짓일때 수행 구문 블록


# if 조건식1:
#    조건식1 참일때 수행 구문 블록
# elif 조건식2:
#    조건식2 참일때 수행 구문 블록
# elif 조건식3:
#    조건식3 참일때 수행 구문 블록
# else:
#    어떤 조건식도 거짓일때 수행 구문 블록


# 각 블록은 반드시 동일한 인덴트로 작성되어야 한다

# 조건식에는 비교연산자와 논리연산자 등을 잘 활용해야 한다
# 비교연산자 <, >, ==, !=, >=, <=
# 논리연산자 and, or, not


a = 10
if a > 0:
    print('변수 a 값은')
    print(a, '는 양수입니다')

print('if 종료')

print()

a = 4

if a % 2 == 0:
    print('변수의 값은')
    print("짝수입니다")
else:
    print('a 의 값은')
    print("홀수입니다")

print('if~else 종료')

print()

a = -10
if a > 0:
    print('양수입니다')
elif a == 0:
    print('0 입니다')
else:
    print('음수입니다')

print('if~elif 종료')


print('\n🟦 비교연산자, 논리연산자')
# 🟦 조건식에 사용가능한 비교연산자, 논리연산자
# 비교연산자 : >, >=, <, <=, !=, ==
# 논리연산자 : and, or, not, ^ (xor)
# 위 연산자들의 결과값은 항상 True / False
#      and : 둘다 '참' 일때 '참'
#      or : 둘중 하나만 '참' 이면 '참'
#      not : 참 -> 거짓, 거짓 -> 참
#      ^ : eXclusive OR (XOR, 배타적 논리합)
#          같으면 거짓, 다르면 참 

d = 10

result = d > 2
result = d > 10 # F
result = d >= 10 # T
result = d == 100 # F
result = d != 100 # T

result = True and True # T
result = True and False # F
result = False or False # F
result = True ^ True # F
result = True ^ False # T
result = not True # F

result = d % 2 == 0 and d % 5 == 0 # d가 2의 배수이고, 또한 5의 배수이면 참.

if result:
    print(result, '입니다.')
else:
    print(result, '입니다.')




print("\n🟦 비교연산자 chaining")
# 비교연산자는 임의로 chaining 된다
# a <= x <= b 표현 가능

# 유효한 점수값은 0 <= ~ <= 100
score = 93

if 0 <= score and score <= 100:
    print(score, '✅유효한 점수입니다')
else:
    print(score, '💢유효하지 않은 점수입니다')

if 0 <= score <= 100:
    print(score, '✅유효한 점수입니다')
else:
    print(score, '💢유효하지 않은 점수입니다')


print(False == True == False) # False == True and True == False


print('\n🟦 중첩된 if (nested-if)')
# if 블럭 안에 다시 if 블럭 (중첩된 if, nested-if)


print('\n🟦 dict 사용')
day = 1

if day == 0:
  result = '월요일'
elif day == 1:
  result = '화요일'
elif day == 2:
  result = '수요일'
print(result)

print()

day = 0

weekday = {
    0: "월요일",
    1: "화요일",
    2: "수요일",
}

result = weekday[day]
print(result)

print()

result = {
    0: "월요일",
    1: "화요일",
    2: "수요일",
}[day]
print(result)


print('\n🟦 Conditional expressions')
# Conditional expressions
# aka삼항연산자 (ternary operator)

# 구문 (참일때의 값) if (조건식) else (거짓일때의 값)

n = 3

result = "짝수" if n % 2 == 0 else "홀수"
print(result)

# 두 숫자 간의 차이값 (difference)
a = 54
b = 72
diff = (a - b) if a > b else (b - a)
print(diff)


print("\n🟦 조건식의 참 / 거짓 판정")

# 조건문,  순환문 등에 사용되는  '조건식' 은 참, 거짓이 판정되어야 하는데
# 파이썬에서는 bool 타입 외에도 조건식에서 참, 거짓 판정이 된다.

#           │     참     │   거짓
# ───────────────────
# bool 타입 :     True         False
# 숫자 타입 :  0 아닌 숫자      0
# str  타입 :      "abc"        ""   빈문자열
# list 타입 :    [1, 2, 3]      []
# tuple 타입 :   (1, 2, 3)      ()
# dict 타입 :    {"name":"john"}    {}

# None 타입 :   무조건 거짓

result = 0.001 # T
result = 0 # F
result = 0.0 # F
result = 'abc' # T
result = '' # F
result = ' ' # T
result = not ' ' # F, not 연산 결과는 bool 타입
result = bool("박영진") # T
result = [1, 2, 3] # T
result = [] # F
result = (0) # F, int
result = (0,) # T, tuple
result = (0,) # T, tuple
result = {"name": "hong"} # T
result = {} # F
result = None # F
result = 2.1 + 0.2 - 2.3 # F

if result:
    print('😀 참', type(result), result)
else:
    print('👿 거짓', type(result), result)

print('-'*20)

print('\n🟦 SCE : Short-circuit evaluation') # 숏-셔킷 이벨리션
# 논리연산자 and, or 의 결과

#논리 연산자 and, or 표현식과의 관계
#참, 거짓 판정에 이어 논리연산자의 결과는 
# expression 값이 된다.
# 이를 -circuit evalutaitoshortn (SCE) 혹은 
# lazy evalutation 이라 한다

# or 
# 왼쪽이 참인 경우 '왼쪽' 수행결과값 리턴
# 왼쪽이 거짓인 경우 '오른쪽' 수행결과값 리턴

# and 
# 왼쪽이 참인 경우 '오른쪽' 수행결과값 리턴
# 왼쪽이 거짓인 경우 '왼쪽' 수행결과값 리턴


result = True or False # T
result = True and False # F

result = 0 or 100 # 100
result = 'Hello' or 'Python' # Hello
result = 'Hello' and 'Python' # P
result = [] and 'Python'

if result:
    print('😀 참', type(result), result)
else:
    print('👿 거짓', type(result), result)

result = print("'Hello")
print(result)

n = 10
if n % 5 == 0:
    print(n, '은 5의 배수입니다.')

n % 5 == 0 and print(n, '은 5의 배수입니다.')

n % 5 == 0 or print(n, '은 5의 배수거 아닙니다.')

# ↓과연 결과가 어떻게 될까?
print('AAA') and print('BBB')

print('CCC') or print('DDD')

# 객체 원본을 변화시키는 함수(메소드)는 대부분 None 을 리턴하고, 
# 이렇게 변화된 원본을 수식에서 그대로 리턴하고자 할때 SCE 활용 함

# dict.update(), list.append(), list.extend(), list.insert()  list.remove()

a = { 'name': '이브'}
result = a.update({'gender': 'male'}) or a
print(result)

a = ['루비짱~']
result = a.append('하이~!') or a
print(result)


print('\n🟦 is 연산자')
# 타입 확인

a = 10
a = 3.14
a = "hello"

print(type(a) is str)
print(type(a) is tuple)


print('\n🟦 pass 키워드')
# 아무문장도 없는 블럭에 명시! -> Todo 로 많이 사용 

data = [10, 20, 30]

# if 40 in data:
# <-- 아무것도 안한다고 이렇게 블럭을 비워두면 에러! IndentationError
# else:
#     print('없습니다.')

if 40 in data:
    pass
else:
    print('없습니다.')

# ... (ellipsis) 사용해도 된다.
if 40 in data:
    ...
else:
    print('없습니다.')

print('\n🟦 블럭이 한문장으로만 구성되어 있다면')
# : 다음에 한줄로 작성해도 된다.

if 10 in (10, 20, 30): 
    print("있습니다")
else: 
    print("없습니다")

if 10 in (10, 20, 30): print("있습니다")
else: print("없습니다")


print('\n🟦 scope: for while if 블럭 안에 선언한 것들을 블럭 밖에서 사용 가능')
# 파이썬은 for while if 블럭 안에 선언한 것들을 블럭 밖에서 사용 가능!

# for, while, if 등 제어문 블럭	=> 함수 전체 또는 전역 scope
# def, lambda, class  =>	새로운 scope 생성

if 'a' in "abc":
    zz = 'a' * 2   
    print(zz)

print('-' * 20)
print(zz) # if 블럭 바깥에서도 사용 가능!

i = input()