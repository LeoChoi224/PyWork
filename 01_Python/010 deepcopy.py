# 대입연산은 
# 주소값을 복사하는 것이다.  (객체 복사가 아니다!)

print('🟦 대입연산')
a = 10 # a라는 값에 10이 저장되어있는 주소값을 참조한다
b = a # 대입연산자는 주소값을 대입3
print(a, b)
print(id(a), id(b)) # 변수의 주소값, 주소값이 같으면 동일 객체 참조, 다르면 다른 객체.
print(a == b)
print(a is b)

a += 1
print(a, b)
print(id(a), id(b))

A = [1, 2, 3]
B = A
print(A, B)
print(id(A), id(B))
print(id(A), id(B))

A[1] = 20
print(A, B)
print(id(A), id(B))


print('\n🟦 id(), is연산자, immutable 객채')
# 중복된 literal, 중복된 immutable 객체는 새로 만들지 않는다
num1 = 10
num2 = num1

print(num1 is num2) # is 연산자, 두 변수가 같은 주소를 참조하는지 여부.

num1 += 2 # 연산결과로 새로운 int 객체(12) 생김 (이유! int 는 immutable 하니까!)
print(num1 is num2)

num3 = 5
print(id(num1), id(num2), id(num3))

num3 *= 2 # 연산결과로 기존의 int 객체(10) 주소를 참조 (이유! int 는 immutable 하니까!)
print(id(num1), id(num2), id(num3))

# 문자열(str) 의 경우
name1 = "John"
print(name1, id(name1))

name2 = 'Jo' + 'hn'
print(name2, id(name2))

jo, hn = 'Jo', 'hn'
print(id(jo), id(hn))
name3 = jo + hn
print(name3, id(name3))

print('\n🟦 is연산자 vs == 비교연산자')
# 파이썬에서 
# == 연산자는 "값의 동등성(equality)" 을 비교
# is 연산자는 "객체의 동일성(identity)" (즉, 메모리 주소가 같은지)을 비교

a = [10, 20, 30]
b = [10, 20, 30]

print(a == b) # 객체가 동등한지 비교 ex) 동명이인은 이름이 같나?
print(a is b) # 객체가 동일한지 비교 ex) 동명이인은 같은 사람인가?


print('\n🟦 얕은복사 (shallow copy)')
# 새로운 인스턴스를 만들고 인스턴스의 '값' 만 복사

# 방법1  copy() 메소드 사용
# 방법2  범위지정 [:]  사용
# 방법3  list() 함수 사용
# 방법4  copy.copy() 사용

# 방법1  copy() 메소드 사용
x = [10, 20, 30]
y1 = x # 대입
y2 = x.copy() # 얕은복사

print(x, y1, y2)
print(x == y1, x == y2, y1 == y2)
print(id(x), id(y1), id(y2))
print(x is y1, x is y2, y1 is y2)

x[1] = 200
print(x, y1, y2)

# 방법2  범위지정 [:]  사용
x = [10, 20, 30]
y1 = x
y2 = x[:] # 슬라이스 연산결과는 얕은 복사 발생
print(x is y1, x is y2, y1 is y2)

# 방법3  list() 함수 사용
x = [10, 20, 30]
y1 = x
y2 = list(x)
print(x is y1, x is y2, y1 is y2)

# 방법4  copy.copy() 사용
import copy
x = [10, 20, 30]
y1 = x
y2 = copy.copy(x)
print(x is y1, x is y2, y1 is y2)

print('\n🟦 얕은 복사의 한계')

x = [1, 2, ['A', 'B', 'C']]
y = x.copy() # 얕은 복사
print(x, y)
print(x == y, x is y)

x[0] = 'python'
print(x, y)

y[-1][-1] = 'F'
print(x, y)

print('\n🟦 깊은 복사(deep copy)')

import copy
x = [1, 2, ['A', 'B', 'C']]
copy.deepcopy(x) # 깊은 복사 발생
print(x, y)
print(x == y,x is y)

x[0] = 'python'
print(x, y)

y[-1][-1] = 'F'
print(x, y)


# 디버깅 (Debugging)
# bug : 프로그램의 논리적인 오류

# step1 : breakpoint 를 잡는다
#      프로그램 디버깅중 일시 중지 할 지점 설정
# step2 : 디버깅 시작
# step3 : breakpoint 에서 멈추면, 디버깅 명령어 실행

#      step over : 한줄씩 실행
#      resume : 다음 break point 까지 진행
#      stop : 디버깅 종료

# 무엇을 확인하나? -> 프로그램이 내 의도대로 동작가는가?
#  - 프로그램의 흐름 
#  - 변수값의 변화
#  - 함수 호출관계

# 'watch' 활용하기
#  - 관찰하고픈 값, 수식 등을 설정하여 확인 가능.

# 'breakpoint' 관리하기





print('\n' * 15)
# 01python(KDT2604)/deepcopy 참고