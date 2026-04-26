# 🟦 여러개의 데이터를 담는 집합 데이터 타입들.. (aka. collection)
#1. list   :  순서있다.  중복허용,  mutable
#2. tuple  :  순서있다,  중복허용,  immutable
#3. set : 순서없다,  중복허용안함
#4. dict : key, value 쌍으로 구성,  (Python 3.7 부터 key 저장순서 유지됨)


# dict : 딕셔너리

# dictionary 데이터 타입은  key-value 쌍으로 저장되는 데이터 집합이다.

# {Key1:Value1, Key2:Value2, Key3:Value3 ...}
# "이름" = "홍길동", "생일" = "몇 월 몇 일"   과 같은 자료형 담음

# 기존의 list, tuple 등은 value 중심
# 그러나 이 또한 알고 보면 key-value 쌍으로 구성

# key 는 중복 안된다.
# ★ Python 3.7 버전부터는 dict 의 키 저장 순서 유지됨. 순회할때에도 저장된 순서대로 리턴됨.

student = {"name": "최현진", "email": "choi@mail.com"}
print(student)
print(type(student))
print(len(student)) # key-value  쌍의 개수

print(student['name']) # 방법1
print(student['email'])
print(student.get('name')) # 방법2

# 존재하지 않는 key의 경우
# print(student['age']) # KeyError: 'age'
print(student.get('age')) # None

# get()  을 사용하면 예외적인 상황에서도
# 동작 가능하게 처리 가능
# student.get(key, default) : key 값이 없으면 default 값으로 리턴
print(student.get('age', 20)) 

# 수정하기
student['name'] = '이희본'
print(student)

# 추가하기
student['address'] = '동탄시'  # 기존에 없던 key-value 쌍 추가
print(student)

# 삭제하기
del(student['email'])
print(student)

print('-' * 20)

# 🟦 dict.update()
# 해당 key값 업데이트
# 해당 key 가 없으면 새로이 추가

student.update({'name': '양정운'}) # 원본변화
print(student)

print(student.update({'age': 22}) )
print(student)

# 🟦 dict 의 key, value 타입
# value는 어떠한 타입이라도 가능 
# key : ...  hash 가능한 타입만 가능    (ex: int, float, str, bool, tuple, ..)

data = {
    1: "haha",
    2: "hoho",
    2: "hehe", # key 중복 불가

    "two": {
        3.14: "pi",
        "pi": 3.14,
    },

    False: [10, 20, 30],
    # [1, 2]: 3.14, # TypeError: unhashable type: 'list'
    (1, 2): 3.14, # tuple 은 key 로 사용 가능!
}

print(data)
print(data[1], type(data[1]))
print(data["two"], type(data["two"]))
print(data["two"][3.14], type(data["two"][3.14]))
print(data["two"]['pi'], type(data["two"]['pi']))
print(data[False], type(data[False]))
print(data[False][1], type(data[False][1]))
print(data[(1, 2)], type(data[(1, 2)]))
print(data[1, 2], type(data[1, 2]))

print("🟦 keys(), values(), items()")
# dict.keys() : key 들로만 구성된 iterable 객체 리턴
# dict.values() : value 들로만 구성된 iterable 객체 리턴
# dict.items() : key-value 쌍들로 구성된 iterable 객체 리턴

student = {
        "name":"최현진", 
        "email":"choi@mail.com",
        "age": 23,
        "addr": "서울",
        }

print(student.keys())
print(student.values())
print(student.items())

# dict의 in 연산자
# key 가 존재하는지 여부

print("name" in student)
print("서울" in student)

print("\n🟦 dict() 함수로 dict 생성하기")

print(dict(a=1,b=2)) # {'a': 1, 'b': 2}

# tuple (key,value)의 list 사용 가능
print(dict[('name', 'kim'), ('age', 24)])


print("\n🟦 빈(empty) 데이터 만들기")
a = [] # list
print(a, len(a))

a = "" # str
print(a, len(a))

a = () # tuple
print(a, len(a))

a = {} # dict
print(a, len(a))

a = set() # set
print(a, len(a))

# empty 데이터는 bool 변환시 False 로 변환
print(bool([]), bool([1]))



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
