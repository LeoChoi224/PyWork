# 🟦 reduce() 함수 N개 => 1개
# reduce는 functools 모듈에 있습니다

from functools import reduce

# 구문
# functools.reduce(function, iterable[, initializer])


# function 을 사용해서 iterable을  집계연산 을 통해 '하나의 값'을 리턴한다.
# 위 function 은 '두개의 매개변수'를 받아서 '하나의 값을 리턴'해야 한다.
# initializer 는 주어지면 첫 번째 인자로서 추가됩니다

# reduce() 의 리턴값 은 value 다.

# 주어진 데이터(들) 의 '합' 을 구하기
dataset = [1, 2, 3, 4]

# 기존의 for문으로 구현하는 경우
def total(numbers):
    result = numbers[0]
    i = 1
    for i in range(1, len(numbers)):
        result = result + numbers[i]
    return result

print(total(dataset))

# 0 | 1, 2, 3, 4
#     1
#        3
#            6
#              10

# reduce() 에 적용되는 함수: '두개' 의 입력 -> '하나' 의 결과
def add(x, y):
    return x + y

print(reduce(add, [1, 2, 3, 4, 5]))

# [  1,   2,   3,   4,   5]
#    ↓  ↓
# add(1, 2)
#    ↓
# [  3       3,   4,   5]
#    ↓      ↓
# add(3,    3)
#    ↓
# [   6,         4,   5]
#    ↓         ↓
# add(6,       4)
#    ↓
# [   10,         5]
#    ↓           ↓
# add(10,         5)
#    ↓
#    15   # 결국 하나의 값으로 reduce 된다

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))


print('\n🟦 initializer (초깃값)')
# [1,2,3] ==> [1,4,9]   <- 관점에 따라선 이는 1개짜리 데이터다.  (list 한개)

# 초기값 parameter 예제
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 100))


def func(a, b):  # a: List,  b: 제곱해서 추가할 값  -> 리턴: List
    print(f'func({a}, {b})')  # 중간단계 출력
    a.append(b ** 2)
    return a

print(reduce(func, [1, 2, 3], []))

# print(reduce(func, [1, 2, 3])) # AttributeError: 'int' object has no attribute 'append'
# reduce 기법 -> 랭체인등에서 ai 에서 돌아온 답과 새로운 내용을 합쳐서 재 질문할때 reduce를 이용

#   []   | [1,   2,   3]
#     ↓    ↓
# func([], 1)
#       ↓
#      [1]    2     3
#         ↓   ↓
#    func([1], 2)
#           ↓
#        [1, 4]    3
#            ↓     ↓
#      func([1, 4], 3)
#                ↓
#            [1, 4, 9]

# lambda 사용하기
print(reduce(lambda a, b: a.append(b ** 2) or a, [1, 2, 3], []))

# 도전
dataset = [1, 4, 3, 5, 2]
# reduce + lambda 를 사용하여 최댓값을 찾아보세요
print(reduce(lambda max, x: max if max > x else x, dataset))

print('-' * 20)

# 아이템 계수하기
dataset = ["dog", "dog", "dog", "cat", "cat", "bird"]

# 개수구하기 결과 =>  {'dog': 3, 'cat': 2, 'bird': 1}

# dict.update({k:v})
print(reduce(
    lambda r, e: r.update({e: r.get(e,0) + 1}) or r,
    dataset,
    {}
))
"""
  {} | ["dog", "dog", "dog", "cat", "cat", "bird"]
     ↘   ↓
    {'dog':1} | ["dog", "dog", "cat", "cat", "bird"]  
           ↘   ↓
           {'dog':2} | ["dog", "cat", "cat", "bird"] 
                   ↘   ↓
                 {'dog':3} | ["cat", "cat", "bird"]
                        ↘   ↓
                  {'dog':3, 'cat':1} | ["cat", "bird"]
                                    ↘   ↓
                          {'dog':3, 'cat':2} | ["bird"]
                                            ↘   ↓
                               {'dog':3, 'cat':2, 'bird':1}              

"""

# 문자열연습2 에서 reduce 활용해서 해볼만한 것(여력이 된다면map으로도)

# 17_longest word
# 19_lettercapital
# 20_make string
# 24_unique in order


print('\n' * 15)