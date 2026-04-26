print("\n🟦 Inner function (nested function)")
# 파이썬은 함수 '안'에서 함수가 정의되는 것을 허용 
# 이를 inner function 혹은 nested function 이라 한다

# def 함수이름1():
#     코드
#     def 함수이름2():
#         코드

def print_hello():
    hello = 'Hello, world!'

    def print_message(): # 함수안에서 정의된 함수
        print(hello)

    print_message()

print_hello()


print('\n🟦 함수를 리턴하는 함수')

# '곱하는 함수'를 만드는 함수

def multiplexer(x):
    def something(n):
        return x * n
    
    return something #inner func 자체를 리턴

print(multiplexer(3))

# multiplexer(3) ... def something(n): return 3 * n
# multiplexer(2) ... def something(n): return 2 * n

triple = multiplexer(3)
double = multiplexer(2)

print(triple(100), triple(10), triple(1000))
print(double(100), double(10), double(1000))


print('\n🟦inner function 에서 scope 의 문제')
# 기본적으로 inner function 은 outer function 의 local 변수 사용 가능. (aka Enclosing scope 의 변수)

# 안쪽 함수 print_message에서는 바깥쪽 함수 print_hello의 지역 변수 hello를 사용할 수 있습니다.
# 즉, 바깥쪽 함수의 지역 변수는 그 안에 속한 모든 함수에서 접근할 수 있습니다
def greetings(x):
    def say_hi():
        print(x)  # 바깥쪽 함수의 지역변수 x 읽기

    say_hi()

greetings('안녕하세요?')


print("\n🟦 외부 scope 변수 '변경' 하려면?")

def foo():
    x = 10

    def zoo():
        x = 20 # zoo() 의 로컬 변수
    zoo()

    print('foo 의 x =', x)

foo()    

print('-' * 20) 

def count(x):
    def increment():
        x = x + 1
        print(x)

    # increment() 호출하면 에러
    
count(5)


print("\n🟦 outer(enclosing) func 의 변수를 변경하려면?")
# 방법1: return 활용 (추천)
# 방법2: nonlocal 키워드 활용 (비추)

def count(x):
    def increment(x):
        x = x + 1
        print('increment x =', x)
        return x

    x = increment(x)
    print('count x =', x)
    
count(5)


print('\n🟦 nonlocal 키워드 사용 (비추)')
def count(x):
    def increment():
        nonlocal x
        x = x + 1
        print('increment x=', x)

    increment()
    print('count x=', x)
    
count(5)

print('-' * 20)

print('\n🟦 closuer 클로져')
# 🔹 클로저 란?
# 클로저(closure)는 “자신이 만들어질 때의 환경(변수들)을 기억하는 함수”입니다.
# 함수가 자신이 정의될 당시의 스코프(특히 바깥 함수의 변수)를 함께 묶어서 기억하는 것을 의미

# 보통 함수 안에서 함수를 만들면, 안쪽 함수는 바깥 함수의 변수를 사용할 수 있습니다.
# 이때 바깥 함수가 끝난 뒤에도 그 변수를 계속 기억하고 있다면 → 그게 바로 closure입니다.

# 🔹 클로저의 핵심 조건
# 클로저가 되려면 보통 이 3가지가 필요합니다:
# - 함수 안에 함수가 있어야 함 (중첩 함수)
# - 내부 함수가 외부 함수의 변수를 사용해야 함
# - 외부 함수가 끝난 후에도 내부 함수가 살아 있어야 함

# 🔹 클로저는 언제/왜 사용하는가?
# ↑ closure 가 무슨 내부 '상태값' 을 갖는 것처럼 동작하게 만들수 있으며, 이는 외부에서 접근 못하게 한다.
#  1.전역변수에 의존하지 않기 때문에 변수값의 변경에 대한 책임권한도 명확해 지고
#  2. 전역변수 사용시 발생할수 있는 충돌 문제로부터 자유롭다
#  3. 사용환경(context)에 맞게 임의대로 내부구조를 조정할 수 있다

def calc():
    a = 3
    b = 5

    def inner(x):
        return a * x + b
    
    return inner  # 내부 함수 리턴

c = calc() # calc() 리턴과 함께 지역변수 a, b는 소멸되었을터?
print(c(1), c(2), c(3), c(4), c(5)) # 그런데! a, b 가 살아서 동작한다?

print() # -----------------------------------

# 호출 횟수를 세는 함수 만들기

# cnt = 0

# def counter():

#     def inner():
#         global cnt
#         cnt += 1
#         return cnt

#     return inner 

# c = counter()
# for i in range(10):
#     print(c(), end=' ')

def counter():
    cnt = 0

    def inner():
        nonlocal cnt
        cnt += 1
        return cnt

    return inner 

c = counter()
for i in range(10):
    print(c(), end=' ')

print()

d = counter()
for i in range(10):
    print(d(), end=' ')






print('\n' * 15)