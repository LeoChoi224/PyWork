# 🟦 여러개의 데이터를 담는 집합 데이터 타입들.. (aka. collection)
#1. list   :  순서있다.  중복허용,  mutable
#2. tuple  :  순서있다,  중복허용,  immutable
#3. set : 순서없다,  중복허용안함
#4. dict : key, value 쌍으로 구성,  (Python 3.7 부터 key 저장순서 유지됨)

# tuple 튜플 데이터 타입
# 콤마 ,  로 구분된 집합 데이터 타입

animals = ("dog", "dog", "cat", "bird")

print(animals)
print(type(animals))

student = "이민재", "최홍묵", "문태형", "장희준", 3
print(student)
print(type(student))
print(len(student))

# 주의! 원소 '하나;짜리 tuple을 만드려면...
# 반드시 원소뒤에 콤마하나 붙여주세요
animals = ("dog")
print(type(animals), animals, len(animals))

animals = ("dog",)
animals = "dog", # () 없어도 가능
print(type(animals), animals, len(animals))

print(student[0])
print(student[-1])
print(student[1:3])
print('-' * 20)

# tuple 은 immutable 하다  <-- 값을 변경할수 없다
# student[0] = '김수림' # TypeError: 'tuple' object does not support item assignment

# 내용 변경하는 동작이 없다.
# student.append('박세정') # AttributeError: 'tuple' object has no attribute 'append'

# tuple 은 언제 사용하나?
# 1. 변경되지 말아야 할 데이터들
# 2. 복수의 값 '전달' 목적으로. 

print("\n🟦 Assignment Unpacking")
# tuple 은 iterable 객체다
# 대입연산자와 iterable 을 사용하여 여러 개의 변수에 대입 가능 (이를 Assignment unpacking 이라 함)

a, b, c, d = 1, 2, 3, 4 # tuple
print(a, b, c, d)

a, b, c, d = [1, 2, 3, 4] # list
print(a, b, c, d)

a, b, c, d = "주술회전" # str
print(a, b, c, d)


# 사각형의 width, height 값을 담고 있는
rec = [100, 200]
width = rec[0]
height = rec[1]
# 한 줄로 해결 가능
width, height = rec
print(width, height)

a, b = ((10, 20), (30, 40))
print(a, b)

(a1, a2), (b1, b2) = ((10, 20), (30, 40))
print(a1, a2, b1, b2)

# a, b, c  = [1, 2, 3, 4] # ValueError: too many values to unpack (expected 3)

# starred expression 사용하면 unpack 되는 값들보다 적은수의 변수들로도 list 로 받아낼수 있다.

a, *b, c = [1, 2, 3, 4, 5, 6]
print(a)
print(b)
print(c)

# unpack 하여 받아내기만 하고 사용하지 않을 변수는
# 관레적으로 '_' 으로 선언
_, a, _, b,  = [1, 2, 3, 4]
print(a)
print(b)

print('🟦' * 20)

# count() 함수
data = [10, 20, 30, 10, 10, 10, 20, 20]
print(data.count(10))

data = 10, 20, 30, 10, 10, 10, 20, 20
print(data.count(10))

data = "aaaaabbbbdcccccddbbaaababb"
print(data.count("b"))



# 	파이썬의 기본 데이터타입들 (Datatype, 자료형)

# 	1. 정수형 : int			ex) 10, 2, 512, 256 ...
# 	2. 실수형 : float		ex) 3.14   100.0  -234.3455 ...
# 	3. 문자열 : str			ex) "Hello"  '한국'   ...
# 	4. 부울 : bool			ex) True  , False
# 	5. 리스트 : list			ex) []  [10, 20]   ['Abc', 'ddd', 'ccc']
# 	6. 튜플 : tuple			ex) ()   (10, 20)  ('aaa', 'bbb', 'ccc')
# 	7. 딕셔너리 : dictionary  ex) {}   {'name':'pey', 'age': 10]
#   8. 세트 : set             ex) {}   {10, 20, 30}
# 	9. None
