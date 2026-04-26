print("🟦 Decorator 데코레이터")
# Decorator 란
# '대상 함수를 wrapping 하고, 이 wrapping 된 함수의 앞뒤에 추가적으로 꾸며질 구문 들을 정의해서 손쉽게 재사용 가능하게 해주는 것이다

# 누군가가 만들어둔 함수 를 확장!

# Python 으로 작성된 Opensource 의 코드들을 보다 보면, 아래와 같이 @ 로 시작하는 구문 들을 볼 수 있다. 


"""
@decorator_
def function():
    print "what is decorator?"
    
@tf.function
def func():
    ...
"""

def send_sms(func):   # func <= crawling   매개변수로 받는 함수가 '대상함수'
    
    def inner_func():        
        result = func()   # result = crawling()   '대상함수' 호출
        print('🌐SMS 를 보냅니다')
        return result  # inner_func가 리턴하는 값이 대상함수 호출의 리턴값이 된다.

    # decorator 는 함수를 리턴해야 하고, 그 함수가 호출된다.
    return inner_func

@send_sms  # decorator
def crawling():
    print("크롤링 합니다.")
    return "크롤링 결과"


result = crawling()  # decorator 가 붙은 함수 (대상함수)를 호출하면  대상함수가 호출되는 것이 아니라
            # decorator 함수가 호출된다.
            # decorator 가 리턴한 함수의 리턴값이 최종 리턴값이 된다.
  
print('result:', result)
# 1. 호출은 crawling()을 하지만, 실제로는 Decorator 인 send_sms(crawling) 이 호출된다!!.  
# 2. send_sms가 리턴한 내부함수가 실행된다.
# 3. 그 내부함수의 리턴값이 최종 리턴값이 된다.

print('-' * 20)

@send_sms
def preprocess():
    print('전처리를 합니다')
    return "전처리 결과"

result = preprocess()
print('result:', result)


print('\n🟦 매개변수와 리턴값을 처리하는 Decorator')

def trace(func):
    def wrapper(x, y):
        r = func(x, y)
        print(f"🎃{func.__name__}(x={x}, y={y}) -> {r}")
        return r

    return wrapper


@trace
def add(a, b):      # 매개변수는 두 개
    return a + b    # 매개변수 두 개를 더해서 반환
 
print(add(10, 20))


@trace
def mul(a, b):
    return a * b
print(mul(5, 9))

print('-' * 20)


def trace(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs) # argument unpacking
        print(f"🔶{func.__name__}(args={args}), kwargs={kwargs}")
        return r

    return wrapper

@trace
def get_max(*args):
    return max(args)

print(get_max(10, 15, 20))
print(get_max(-3, -6, 10, 21, 9))

@trace
def get_min(**kwargs):
    return min(kwargs.values())

print(get_min(x=10, y=20, z=30))

print('-' * 20)


# 경과시간측정 (elapsed time) 하는 Decorator 작성하기
import time
from datetime import timedelta

# laptime 만들기!
def laptime(func):

    def print_time(loop, delay):
        print(f"{func.__name__}() 측정시작")
        start_time = time.time()

        func(loop, delay) # 대상 함수 실행
        
        end_time = time.time()
        print(f"측정종료", end_time - start_time)

    return print_time

@laptime
def countDown(loop, delay):  # countDown 함수는 수정하지 않습니다
    for i in range(loop, 0, -1):
        print(i)
        time.sleep(delay)
    
countDown(3, 2)
print()
countDown(5, 1)
print()

"""
countDown() 측정시작
3
2
1
측정종료 0:00:06.002019

countDown() 측정시작
5
4
3
2
1
측정종료 0:00:05.002277

"""











# TODO 함수 성능 테스트용 데코레이터 만들어보기
print('\n' * 15)