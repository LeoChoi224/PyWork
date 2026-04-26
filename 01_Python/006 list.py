# 🟦 여러개의 데이터를 담는 집합 데이터 타입들.. (aka. collection)
#1. list   :  순서있다.  중복허용,  mutable
#2. tuple  :  순서있다,  중복허용,  immutable
#3. set : 순서없다,  중복허용안함
#4. dict : key, value 쌍으로 구성,  (Python 3.7 부터 key 저장순서 유지됨)

# 🟦 list
# list 는   [   ]  으로 만든다
# 데이터(원소) 들은 , 콤마로 구분한다
# 각 데이터(원소) 들은 어떠한 타입도 가능하다

animals = ['dog', 'cat', 'bird', 'fish']
print(animals)
print(type(animals))

animals = [
    'dog',
    'cat',
    'bird',
    'fish', # 마지막 원소 뒤에 콤마 붙여도 ok
    ]

# 순서가 있다 -> 인덱싱 (index)
print(animals[0]) # 첫번째 원소는 index 0 부터 시작 0-base index
print(animals[2])
# print(animals[4]) # IndexError: list index out of range

print(animals[-1])  # 음수 인덱싱 가능.
print('🟦' * 20)

# 데이터 내용 변경 가능 (list는 mutable 하다.)
animals[2] = 'mouse'
print(animals)

# len() : 리스트의 원소 개수
print(len(animals))

# 데이터 중복 허용
fruits = ["apple", "banana", "apple", "kiwi"]

print("🟦 슬라이싱(slicing)")
# 일부분 추출.
# slice 연산자 [:] 사용 (aka 범위 연산자, slice 연산자, colon 연산자)
# step 값 사용가능

animals = ['dog', 'mouse', 'cat', 'bird', 'fish']
print(animals)

print(animals[0:3]) # 0 부터 3 전까지
print(animals[1:4]) # 1 부터 4 전까지
print(animals[:2]) # 처음부터 2 전까지
print(animals[2:]) # 2부터 끝까지

print(animals[-2:]) # -2부터(뒤에서시작) 끝까지
print(animals[:]) # 전체

print(animals[0:100]) # slicing 은 index 범위 벗어나도 ok

i = 2
print(animals[:i], animals[i:])

# step 값
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[1:7])
print(my_list[1:7:2]) # step 2. 건너뛰는 값

print(my_list[3::3]) # 3부터 전체, 스템:
print(my_list[::]) # 전체
print(my_list[::2]) # 전체, 스템:2

print(my_list[5:0])  # []
print(my_list[5:0:-1]) # 5부터 0전까지 -1 step 값
print(my_list[::-1]) # 역순, 뒤집기 

print('-' * 20)

# slice 결과에 대입
a = [1, 2, 3, 4, 5]
print(a)
a[1:4] = [20, 30, 40] # 치환됨
print(a)

print('-' * 20)
a = [1, 2, 3, 4, 5]
print(a)
a[1:4] = ['루비', '이브'] # 길이는 확장 / 축소 될 수 있다.
print(a)

print('-' * 20)
a = [1, 2, 3, 4, 5]
print(a)
a[2:2] = ['루비', '이브'] # 삽입
print(a)

print('-' * 20)
a = [1, 2, 3, 4, 5]
print(a)
a[1:4] = [] # 삭제
print(a)

print('🟦' * 20)

# 🟦 append() :  데이터 (원소) 추가 , 리스트 뒤에 
#  ※ list 는 mutable 하기 때문에 가능

print(animals)
animals.append('tiger')
print(animals)

# 원소 삭제: del()
del(animals[1])
print(animals)

# list 연산자 +, *

print(fruits)
print(animals + fruits) # list + list

print(fruits * 2)

print('🟦' * 20)
# 1차원 리스트 : 인덱스를 하나만 사용하는 리스트
print(fruits[0], fruits[1])

# 리스트의 원소는 '어떠한 타입'도 가능.  심지어 리스트도 가능
my_list = [100, 200, 'John', 0.29, False, None]

# n차원 리스트 (다차원 리스트)
# list 의 원소가 list
# 인덱스를 여러개 사용할 수 있다.

data = [
    [1, 2, 3],
    [10, 20, 30],
    [40, 50, 60],
]

print(len(data))
print(data[0])
print(data[1])
print(data[2])

print(data[0][1]) # [][] 인덱스를 2개 사용 (2차원 리스트)
print(data[2][1])

# data --> 2 차원 list
# data[0] --> 1차원 list
# data[0][0] --> 0차원, scalar 값

# ※ 인덱싱을 한다는 것은 차원 -1 축소 발생

# ※ 슬라이싱 결과는 차원 축소 발생 안함.



# 2차원 리스트의 원소는 1차원 리스트
# 3 ..           ..   2 ..
# 99 ..          ..   98 .. 
# n 차원 리스트의 원소는 n-1 차원 리스트

data = [
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [11, 22, 33, 44, 55]
]

print(data[0:2])
print(data[1][:2])


print('🟦' * 20)
print(animals)

animals.remove('bird') # 원본 변경
print(animals)
animals.insert(2, 'eagle') # 원본 변경
print(animals)

animals.sort() # 오름차순 정렬 # 원본 변경
print(animals)

animals.sort(reverse=True) # 내림차순 정렬
print(animals)

print(animals[::-1]) # 원본 변경 안함.
print(animals)

# sorted() 함수와 list
# sorted(iterable, key=key, reverse=reverse)
#    iterable : sort 대상 (list, dict, tuple 등..)
#   key : 대소비교를 하는 함수 (디폴트 None)
#   reverse : False 오름차순 (디폴트), True 내림차순

# 리턴값 : 정렬된 list 
a = ["b", "g", "a", "d", "f", "c", "h", "e"]
print(sorted(a))
print(a.sort(reverse=True))

x = sorted(a) # 원본 변경 안함
print(x)
print(a)

# in 연산자
print("dog" in animals) # True
print("shark" in animals)

print('\n🟦 str 의 index, slice, in')
# str 도 list 와 마찬가지로 iterable 객체다

str2 = "hello python"
print(str2[0]) # str 에 index 가능
print(str2[1])
print(str2[11])

print(str2[3:10])
print(str2[::2])
print(str2[::-1])

dd = "2026-04-10"

year = dd[:4]
month = dd[5:7]
day = dd[8:]

print(year, month, day) # -> 2026 04 10

# in 연산자
print("py" in str2) # 존재하면 True
print("py" not in str2) # 존재하지 않으면 True

# sorted() -> 정렬된 리스트
print(sorted(str2))

print(str2)
# str2[0] = 'Y' # str 은 immutable 하다!

print("\n🟦 str 과 list")
print(animals)

# str.join() : list -> 하나의 str
result = "-".join(animals)
print(result)

# str.split() : list 로 쪼갬. 결과는 list
print(result.split("-"))

# split() 에 매개변수 없이 사용하면 공백 기준으로 문자열 쪼개짐
# 공백 : 띄어쓰기, 탭, 줄바꿈...

my_str = "      Hello   \n\t      Python      \n2026"
print(my_str.split())

print(dd)
print(dd.split("-"))

# ※ 위와 같이 특정 문자열을 기준으로 동작할때
#  그러한 역할을 하는 문자열을 delimiter 라고 한다.

print('\n🟦 형변환 함수 list()')
# list(iterable)

print(str2)
print(list(str2))



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
