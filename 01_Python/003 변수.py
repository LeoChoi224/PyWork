# 🟦 변수(variable) 은 데이터를 담아두는 공간
# 이름을 정해서 담아둔다.  이 이름을 변수이름 (variable name) 이라한다
# 변수의 데이터는 언제든지 변경할수 있다. (변할수 있다!)

# 변수 사용법
#    변수명 = 값

# 이와 같이 = 연산자를 사용하여 변수에 값을 저장하는 것을 대입(assign) 한다 라고 하며
# = 을 대입연산자 (assignment operator) 라고 한다

# ★★프로그래머는 변수에 어떠한 타입의 어떠한 값이 담겨 있는지 놓치면 안된다!   타입! 값!

# 변수명은 대소문자 구분한다

a = 10   # a 라는 변수에 정수값 int 10 을 대입

print(a)
print(type(a))

print('a 값은', a, ' 입니다')

a = 20 # 기존 a 변수 값 변경
print('a 값은', a, ' 입니다')

a = 3.14 # 기존 a 변수 값 변경
print('a 값은', a, ' 입니다')
print(type(a))

b = 5
print(a + b)

# NameError: name 'c' is not defined
# print(c) # 선언한 적 없는 변수 사용 불가
# print(A) # 변수명. 대소문자 구분. case sensitive

# 🟦 형변환 함수
# int(), float(), str(), bool() ....

my_name = "김만두"

print('제 이름은', my_name, '입니다.')
print('제 이름은 ' + my_name + ' 입니다.')

age = 10 # int 타입
print('제 나이는', age, '살 입니다.')
# print('제 나이는' + age + '살 입니다.') # TypeError: can only concatenate str (not "int") to str
print('제 나이는 ' + str(age) + ' 살 입니다.')

num = "100"
# print(num + 2)
print(int(num) + 2)

print('-'*20)

print(float(10))
print(int(3.14))

print(bool(0))  # 0 --> False
print(bool(1))  # 0이외의 값 -->True

print(int(False))
print(int(True))

# 🟦변수명규칙
#   식별자(identifier) 명명규칙

# 알파벳, 숫자, _  등 사용 가능
# 숫자로는 시작할수 없다
# 변수명에 띄어쓰기 불가
# 특수문자 불가
# 파이썬의 예약어(reserved word)는 변수명으로 사용불가
#      and,  as,  assert,  break,  class,  continue,  def,  del,  elif,  else,  except,  is,  
#      finally,  for, from,  global,  if,  import,  in,  lambda,  nonlocal,  
#      not,  or,  pass,  raise,  return,  try,  while,  with, yield

# 🟦 del() : 변수 제거 # 사용할 일 거의 없음
name = "John"
print(name, type(name))

del(name) # name 변수 제거
# print(name, type(name))

# 🟦 여러 변수를 한줄에 선언하기
a = 10
b = 20
c = 30
print(a, b, c)

a, b, c = 100, 200, 300 # 튜플
print(a, b, c)

# 🟦 기존의 변수값 증감...
a = 10
print('a =', a)

a = a + 1
print('a =', a)
a = a + 1
print('a =', a)
a = a + 1
print('a =', a)

# 복합 대입 연산자
a += 1
print('a =', a)

a *= 2
a -= 1
a %= 2
print('a =', a)

# TypeError: 'b' is an invalid keyword argument for print()
# print(b = 20) # 파이썬은 대입연산자 결과값이 없다.

# :=  ← walrus 연산자. # 가급적 사용 x
#  식 안에서 변수에 값을 대입하면서 동시에 사용할수 있게 함.
print(b := 20)


# 🟦 변수 값 서로 바꾸기 (swap)
a, b = 11, 33
print('a =', a, 'b =', b)

temp = a
a = b
b = temp
print('a =', a, 'b =', b)

a, b = b, a
print('a =', a, 'b =', b)

