# scope (스코프)
# '이 이름(identifier) 가 사용할수 있는 범위'

# Local Scope : 함수 안에서 정의된 변수. (aka 지역변수), (선언하고 그 함수 안에서만 사용)
# Global Scope : 모듈(파일) 레벨 변수. (aka 전역변수),  (선언후 그 모듈/파일 안에서 사용)
# Enclosing Scope : 중첩함수에서 바깥 함수의 변수
# Built-in Scope : 

# Python 에서는 변수를 찾을때 탐색 우선순위
# L -> E -> G -> B

print('\n🟦 global variable, global scope')
x = 10

def foo():
    print(x) # 함수 안에서 전역변수 '사용' 가능! '읽기 동작'은 가능!

foo()
print(x)

print('\n🟦 local variable, local scope')
def foo():
    y = 10 # foo 의 지역변수
    print(y) # foo 의 지역변수 y 출력

foo() # 함수 종료와 함꺠 지역변수는 소멸
# print(y) # NameError: name 'y' is not defined

print('\n🟦 함수 안에서 전역변수를 수전(쓰기동작) 하려하면?')
z = 10  # 전역변수

def foo():
    z = 20  # z는 foo의 지역변수로 정의. 쓰기동작⭐️⭐️
    print(z) # local 변수 z 를 읽어서 출력 

foo()
print(z) # 전역변수 z 는 변경되지 않았다.

print('\n🟦 매개변수는 local scope')
a = 1

def vartest(a): # 매개변수 a 는 local scope 
    print('vartest] a=', a)

vartest(a) # 호출할떄는 값의 복사가 발생
print('전역] a=', a)

print('\n🟦 주의! UnboundLocalError')
a = 1

def vartest():
    a = a + 1  # 에러!  UnboundLocalError: local variable 'a' referenced before assignment
                # a 에 '쓰기' 동작을 하려 하기 때문에 지역변수로 선언되는데.  a + 1 연산 수행시 에러.
                # 이유 대입연산의 우선순위가 낮아 연산 먼저 수행되는데 그 시점에 a는 선언된 적이 없다
    print('vartest] a=', a)

# vartest()
print('전역] a=', a)

print("\n🟦 함수를 통해 전역변수 값을 '변경'하고 싶다면!")
# 방법1 : return 값 활용 (추천)
# 방법2 : global 키워드 사용 (비추) -> 유지보수 측면에서는 매우 안 좋아서 가급적 x
a = 1

def vartest(a):
    a = a + 1
    return a # 변경된 지역변수 a 를 리턴

a = vartest(a)  # 리턴값으로 전역변수 a 값을 변경
print('전역] a=', a)

print("\n🟦 global 키워드 사용 (비추)")
a = 1
def vartest():
    global a # 이 함수 안에서 'a' 는 전역변수 a 임을 선언.
    a = a + 1
    print('vartest] a =', a)

vartest()
print('전역 a =', a)

print('-' * 20)

print('\n🟦 네임스페이스 (name space)')

import pprint # pretty print

pprint.pprint(locals())  # 전역에서 호출하면 전역 네임스페이스

def foo():
    c, b, d = 10, 20, 40
    pprint.pprint(locals())  # 로컬 안에서 호출하면 로컬 네임스페이스

foo()

# ----------------------
# ★★Python에서는 if, for, while, try, with 블럭(등)에서 새로운 scope를 만들지 않습니다.★★

# 변수는 가장 가까운 함수 단위의 지역 scope를 따르며, 함수 밖에서는 전역(global) scope를 가집니다.
# 즉! 파이썬은 for while if 블럭 안에 선언한 것들을 블럭 밖에서 사용 가능!

# 이 특성은 Java, C, JavaScript의 블럭 스코프(block scope)와는 다른 점입니다.
# 필요하면, nonlocal, global 키워드를 사용해 scope를 조절할 수도 있습니다.

# ▶파이썬의 scope 정리
# for, while, if 등 제어문 블럭	=> 함수 전체 또는 전역 scope
# def, lambda, class  =>	새로운 scope 생성






print('\n' * 15)
