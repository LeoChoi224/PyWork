# 🟦 for 순환문
# 기존의 다른 프로그래밍 언어의 for 문에 비해 파이썬은 매우 직관적이고 사용하기 편리

# 구문]
# for 변수 in iterable객체: 
#     수행할 문장1
#     수행할 문장2
#     ....
# else: *** 절대 사용 x ***
#      순환문 빠져나오기 전에 수행

# iterable한 객체들 => range(숫자), str, list, set, tuple, dict ... 

print(range(3))  # 0, 1, 2 가 담긴 iterable 객체 생성

for i in range(3):
    print('hello world', i)

print('-' * 20)

for i in range(5, 8): # 5, 6, 7 #5부터 8전까지
    print('hello world', i)

print('-' * 20)

for i in range(4, 15, 3): # 4, 7, 10, 13 #step값 3
    print('hello world', i)

print('-' * 20)

for i in range(10, 0, -2):
    print('🐹', i)

# 구구단 2단
for i in range(1,10): # x1 ~ x9
    print(f'2 x {i} =', 2 * i)

#  연습
# for문으로 구구단 출력 2단 ~ 9단
# range() 사용
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')
    print()
        

print()
for i in range(0, 10):
    print("/", end=" ")
    for i in range(0, 10):
        print('*', end='')
    print()

print('\n🟦 for문 + iterable 순환문')
animals = ["dog", "cat", "bird", "puppy", "kitty"]

for animal in animals:
    print('❤️ I love', animal)

for ch in "Hello":
    print(ch, end = ',')
print()

data = [11, 22, 33, 44]
# [22, 44, 66, 88]  <- 각 원소에 x 2 연산한 결과가 담긴 리스트 만들기

result = []
for d in data:
    result.append(d * 2)

print(result)

data = [11, 22, 33, 44]
# [22, 44]  <-- 짝수만 걸러낸 리스트 만들기

result = []
for d in data:
    d % 2 == 0 and result.append(d)

print(result)

# dict 는 for문에서 key 값이 순환됨.
my_dict = {'name':'hong', 'age':24, 'grade':4}

for key in my_dict:
    print(key, ':', my_dict[key])


# dict.keys() : key 들로만 구성된 iterable 객체 리턴
# dict.values() : value 들로만 구성된 iterable 객체 리턴
# dict.items() : key-value 쌍들로 구성된 iterable 객체 리턴

print(my_dict.items()) # ⭐️ 반환값이 튜플, 0번이 key, 1번이 value

for item in my_dict.items():
    print(type(item), item)

    # assignment unpacking ⭐️
for key, value in my_dict.items():
    print(key, ':', value)

print()
# break, continue --> for 순환문에서도 사용 가능.

for x in  range(10):
    print(x, end= ' ')
    if x == 5: break

print("\n🟦 enumerate(iterable)") # 리스트를 인덱스를 쓸 수 있게 튜플로
# (index, data) 쌍의 iterable 객체 리턴 ⭐️
print(animals)
print(list(enumerate(animals)))

for idx, animal in enumerate(animals):
    print(idx, animal)

print("\n🟦 zip()")
# zip(iterable, iterable, ...)
# 매개변수 iterable 데이터들의 각 아이템들을 묶은 tuple들의 iterable 객체 생성

print(list(zip([10, 20, 30], ['a', 'b', 'c'])))

for x in zip([10, 20, 30], ['a', 'b', 'c'], "김수림"):
    print(x)