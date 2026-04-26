# 가령 다음과 같은 기능을 하는 함수들를 만드려고 한다

#      (입력)        (리턴)
# 1. [1, 2, 3] => [1, 4, 9]        <-- 제곱을 하는 함수

# 2. [-1, 2, -3] => [1, 2, 3]      <--  절대값을 구하는 함수


# 즉, 집합데이터형을 입력 받아서 '각 원소'들에게 '무언가 적용' 한 결과를 만드는 함수!!

def get_square_list(numbers):
    result = []

    for number in numbers:
        result.append(number ** 2)

    return result

print(get_square_list([3, 4, -6]))

def get_absolute_list(numbers):
    result = []

    for number in numbers:
        result.append(abs(number))

    return result

print(get_absolute_list([3, 4, -6]))

#------------------
def square(x):
    return x ** 2

def absolute(x):
    return x if x >= 0 else -x

# func 함수를 매개변수 받는 함수 정의
#   func 은 매개변수 한개를 받아서 연산수행한 결과를 리턴
def apply_func_to_list(numbers, func):  
    # result = []
    # for number in numbers:
    #     result.append(func(number)) # ⭐️ 매개변수로 받은 함수 호출 (이러한 동작을 callback(콜백``) 이라고 한다)
    # return result

    return [func(number) for number in numbers]

print(apply_func_to_list([3, -2, 7], square))  # 호출시 함수 square 를 func 에 전달
print(apply_func_to_list([3, -2, 7], absolute))

print("\n🟦람다 (lambda)")
# '이름이 없는(익명)' inline 함수 정의
# 구문: lambda [parameters]: expression

f1 = lambda x: x * 2
print(f1(2), f1(3), type(f1))

print((lambda x: x * 10)(100))

print((lambda x, y: x + y)(23, 400))

print((lambda : "문태현")()) # 매개변수 없는 람다

print((lambda a, b, c: print(f"{a}-{b}-{c}"))(44, 55, 66))

print('-' * 20)

print(apply_func_to_list([3, -2, 7], lambda x: x ** 2))
print(apply_func_to_list([3, -2, 7], lambda x: x if x >= 0 else -x))
# print(apply_func_to_list([3, -2, 7], lambda x: abs(x)))

# 파이썬은 람다함수에 여러문장 작성 불가!
# lambda name, age: print(name); print(age)


# map(), filter(), reduce() 등에서 lambda 활용 많이 함.

# map: N -> N  (N개의 입력을 받아 '어떠한 동작을' 적용하여 N개의 결괏값을 생성)
# filter: N -> N' (N' <= N) ('어떠한 동작을' 적용하여 True만 결과값을 리턴)
# reduce: N -> 1  # 집계연산


print('\n🟦 map() 함수 N개 => N개')
# '집합데이터' 에 ~~한 동작/연산을 수행/적용하는 함수' 를 세트로 주어
# 일괄 처리 할수 있다
# 파이썬에는 이와 같은 일을 처리하는 함수가 있다.
# 바로 map() 이다

# 구문
#  map(함수, iterable 데이터)     #<-- 이때 data 는 iterable 해야 한다

#  map() 결과 리턴값은 'map객체' 이고 이 또한 iterable 하다!

m = map(square, [1, 2, 3])
print(m)
print(list(m))
print(list(map(square, [1, 2, 3])))

# "apple" -> ["A", "P", "P", "L", "E"]

print(list("apple".upper()))

print("apple".upper(), str.upper("apple"))

print(list(map(str.upper, "apple")))

print(list(map(lambda x: x ** 2, [1, 2, 3])))
print(list(map(lambda x: x ** (1 / 2), [1, 2, 3])))

# 도전
# 주어진 리스트의 멤버들을 제곱해서 음수값 내기
# lambda 와 map 사용

#[3, 2, -4]  --->  [-9, -4, -16]

print(list(map(lambda x: -(x ** 2), [3, 2, -4])))


print("\n🟦 응용: CSV 파일 데이터 가공")
# CSV 파일 데이터의 형태에서
data = """height,weight,label
140,45,normal
145,72,fat
150,61,fat
137,56,fat
192,48,thin
175,77,fat"""  # <-- excel 에서 확인 가능하다!
print(data)


# 아래와 같은 리스트로 만들기
# [[140.0, 45.0, 'normal'],
#  [145.0, 72.0, 'fat'],
#  [150.0, 61.0, 'fat'],
#  [137.0, 56.0, 'fat'],
#  [192.0, 48.0, 'thin'],
#  [175.0, 77.0, 'fat']]

# while, for, if 안씁니다
# cond expr 사용 가능.  map 활용

print(data)

# 방법1 : map 사용하지 않고 for, if 사용한다면?
lines = data.split('\n')
# print('🤪', lines)  # 확인용

result = []
for line in lines[1:]:
    # print('🐹', line)

    items = line.strip().split(',')
    # print('👿', items)  # ['140', '45', 'normal']
  
    line_result = [] # [140.0, 45.0, 'normal']
    for item in items:
        line_result.append(float(item) if item.isdigit() else item)
          
    # print('🌐', line_result)
    result.append(line_result)

print('🧡', result)

print('-' * 20)

# 방법2 : map 사용

rows = data.split()[1:]  # 컬럼헤더 제외한 데이터들
print(rows)

lines = list(map(lambda row: row.split(','), rows))
print('✨', lines) # 확인용

result = list(map(lambda line : [float(line[0]), float(line[1]), line[2]], lines))

print('✅', result)

data2 = "  200 , 400  , 700, hello"
# => [200, 400, 700, "hello"]  로 만들기
print(list(map(
    lambda x: int(x) if x.strip().isdigit() else x.strip(),
    data2.strip().split(',')
    )))

print('-' * 20)

# 방법1
# print(list(map(lambda item : int(item) if item.strip().isdigit() else item.strip(), data2.strip().split(','))))

print(data2.split(","))

print(list(map(
    lambda x: x.strip(), 
    data2.split(","))))

print(list(map(
    lambda x: int(x) if x.strip().isdigit() else x.strip(), 
    data2.split(",")
    )))

print('-' * 20)

a = "1.2 2.5 3.7 7.86"
print(a.split())
print(list(map(float, a.split())))


print("\n🟦 filter() : N => N' (N' <= N)")
# 구문 : filter(function, iterable)

# filter에 인자로 사용되는 function은 처리되는 각각의 요소에 대해 참/거짓 값을 반환합니다. 
# '참'을 반환하면 그 요소는 남게 되고, '거짓'을 반환하면 그 요소는 제거 됩니다

# filter() 결과는 filter 객체  (이또한 iterable 하다)

data = [3, 7, 9, 8]

# data 에서 3의 배수만 담은 리스트 만들기

result = []
for d in data:
    if d % 3 == 0:
        result.append(d)

print(result)


# 주어진 숫자 x 가 3의 배수이면 True 아니면 False 리턴하는 함수.
def multiple3(x):
    return x % 3 == 0

print(multiple3(8), multiple3(9))

print(filter(multiple3, data))  # filter() 객체는 filter 객체 (iterable)

print(list(filter(multiple3, data)))

#  입력:  [3,   7,   9,  8]
#         ↓     ↓    ↓   ↓
#  적용:   multiple3(x)
#         ↓     ↓    ↓   ↓
#         T     F    T   F
#         ↓          ↓
#  결과:  [3,        9]

print(list(filter(lambda x: x % 3 == 0, data)))

data = [1, -2, 3, -4, 5]

# 양수인것만 걸러내기 filter + lambda

print(list(filter(lambda x: x > 0, data))) # map 과 filter 의 차이
print(list(map(lambda x: x > 0, data)))

print(list(map(lambda x: x > 0, data)))

print('-' * 20)
# data 에서 양수인 숫자들을 제곱한 결과  => [1, 9, 25]

# 1) 함수로 만들어 보고
def get_positive_list(data):
    num = []

    for d in data:
        if d > 0: num.append(d ** 2)
    
    return num

print(get_positive_list(data))

# 2) lambda, map, filter 로도 만들어 보자
positive_set = filter(lambda x: x > 0, data)
print(list(map(lambda x: x ** 2, positive_set)))
print(list(map(
    lambda x: x ** 2 ,
    (filter(
        lambda x: x > 0,
        data,
        ))
    )))

# 3) list comprehension 으로도 도전해보자
print([x ** 2  for x in data if x > 0])


print('\n🟦 all(iterable), any(iterable)')

# any(iterable) 함수
# iterable 안에 True로 평가되는 값이 하나라도 있으면 → True
# 전부 False이면 → False

# all(iterable) 함수
# iterable 안의 모든 요소가 True → True
# 하나라도 False → False

for d in [
    any([False, False, True]),  # True
    any([0, "", None]),  # False
    
    all([True, True, True]),  # True
    all([True, True, {}]),  # False

    numbers := [1, -2, 4, -4, 5],
    # 전부다 짝수인가?
    # all + map
    # list(map(lambda x: x % 2 == 0, numbers)),
    all(list(map(lambda n: n % 2 == 0, numbers))),
    any(list(map(
        lambda n: n % 2 == 0,
        numbers
        ))),

    # comprehension
    any([n % 2 == 0 for n in numbers]),
    
    # generator expression
    any(n % 2 == 0 for n in numbers),

]: print(d)


print("\n🟦 iterable 을 매개변수 받는 함수에 generator expression 사용 가능") # list expression 과 차이점: generator expression는 메모리 차지 x

# sum(iterable), max(iterable)....
orders = [
    {"item": "Laptop", "price": 1200},
    {"item": "Mouse", "price": 25},
    {"item": "Monitor", "price": 300},
]

# 가격만 뽑아서 합산
print(sum(order['price'] for order in orders))
# 가장 비싼 가격
print(max(order['price'] for order in orders))

print(" | ".join(order['item'] for order in orders)) # join에 generator expression 많이 사용


print('\n' * 15)