# 🟦숫자 (정수, 실수) 데이터
# 소숫점이 없으면 '정수' (int : integer)
# 소숫점이 있으면 '실수' (float)  
# 컴퓨터 프로그래밍에서는 실수를 floating point number 라 함

print(10) # 정수 int
print(10.0) # 실수 float
print(10.) # 10.0
print(.1) # 0.1

print(10 - 2 * 4) # 연산자 우선순위
print((10 - 2) * 4)

print(4 * 5)  # 정수와 정수끼리 연산결과 -> int
print(4 * 5.0) # 실수와 연산결과는 -> float

print(4 / 2) # / 연산 결과는 무조건 float

# 나눗셈 후 소수점 이하를 버리는 연산자 :  // (floordiv)
# 정수 끼리 딱 떨어지는 결과에 대해서는 정수로 결과가 나옴
# 나눗셈 후 소숫점 이하 버리는 연산자

print('-'*20)

print(4 // 2)
print(4 // 2.0)

print(3.42 / 1.12)
print(3.42 // 1.12)

# print(5 / 0)  # 0으로 나누면 에러.

# 나머지 연산자 %
print(13 % 3)  # 13 = 3 * 4 + 1
print(12.5 % 4.1) # 12.5 = 4.1 * 3 + 0.2
    # 📌컴퓨터의 실수 계산 결과는
    # 항상 오차가 있을 수 있다.

# 제곱연산자 **
print(2 ** 4)
print(-3 ** 3)
print(2 ** -1)
print(2 ** (1/2))

# 참고: 제곱근 구하기
import math
print(math.sqrt(2))

#----------------------------------
# 🟦 문자열 타입 : str (string)
# 문자열 리터럴 만드는 방법
# 1. 쌍따옴표 (double quotation)
# 2. 홀따옴표 (single quotation)
# 3. 쌍따옴표3개
# 4. 홀따옴표3개
# 그밖에
#   f-string
#   r-string
#   b-string
#   ..

print()
print('🟦 문자열')
print('Python is fun')
print("Python is fun")
print("""Python is fun""")
print('''Python is fun''')

print("She's gone")
# print('She's gone')

print("""동해물과 백두산이 
마르고 닳도록""")
#print("동해물과 백두산이 
#마르고 닳도록")

print("""
    abcd
      efgh
      iskl
    """)
# print("
#     abcd
#       efgh
#       iskl
#     ")

# print(12 + " monkeys")  # 숫자 + 문자 연산 불가!

# 문자열 반복 연산자 *
print('😀' * 20)

# 문자열 길이 len() 함수 (문자열 안의 문자 개수)
# len(문자열)
# length

print(len('파이썬'))
print(len('hello python')) # 공백도 하나의 문자다!

# 자동 접합 (concat) # 인접해 있으면 그냥 자동으로 붙는다 
print('hello' '로켓')

# 🟦  bool 타입
# True (참) 혹은 False (거짓) 값만 갖는 논리 타입 
print("🟦 bool 타입 ")

print(True)
print(False)

# 비교연산자, 논리연산자 의 결과는 bool 타입니다
# 비교연산자 : == (같다),  != (같지 않다),  >, >=, <, <=
# 논리연산자 : and, or, not

print(20 > 10) # True
print(10 > 10) # False
print(10 >= 10)

print(10 * 2 == 10)
print(10 * 2 != 10)
print(10 / 2 == 5) # 5.0 == 5
print(2.1 + 0.2 == 2.3)
print(2.1 + 0.2)  # ★실수연산결과는 정확하지 않다.  절대 == 비교연산 하지 말자

#─────────────────────────────────────
# 🟦 None 타입
# 아무런 값도 없는 데이터

print("🟦 None 타입 ")
print(None)

#─────────────────────────────────────
# 🟦 type() 함수
# 사용법 type( 타입을 알고자 하는 값/변수/식 )
print("🟦 type() 함수 ")

print(type(10))
print(type(10.0))
print(type("10.0"))
print(type(True))
print(type(None))

# ( )  괄호
# { }  brace
# [ ]  bracket
# < >  angle-bracket


#─────────────────────────────────────
# 🟦 Indentation
# 파이썬은 들여쓰기 열 맞추어야 한다

print(100)
#  print(200)
print(300)

# 줄바꿈 문자 '\n'
print("안녕하세요 파이썬")
print("안녕하세요 \n파이썬")

# print() 는 여러 데이터 출력 가능.
print('abc', 123, 3.14, False)

print('\n' * 12, '🟨 프로그램 종료')