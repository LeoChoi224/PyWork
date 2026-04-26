# 🟦 여러개의 데이터를 담는 집합 데이터 타입들.. (aka. collection)
#1. list   :  순서있다.  중복허용,  mutable
#2. tuple  :  순서있다,  중복허용,  immutable
#3. set : 순서없다,  중복허용안함
#4. dict : key, value 쌍으로 구성,  (Python 3.7 부터 key 저장순서 유지됨)


# set
# 만드는 방법
# 1.set(iterable)  함수로 만들수도 있고
# 2. {  } 으로 만들수도 있다.

animals = {"dog", "dog", "cat", "bird"}
print(animals)
print(type(animals))
print(len(animals))

# animals[0]  # TypeError: 'set' object is not subscriptable

data = "abcdefg"
print(list(data))
print(tuple(data))
print(set(data))

print('-' * 20)

# 빈 set 만들기
a = {}   # 이건 dict 다! 주의!
print(a, type(a), len(a))
a = { }
print(a, type(a), len(a))
a = set()  # 요렇게 만들어야 한다.
print(a, type(a), len(a))

# add() : 추가
# remove() : 삭제

a.add("박세정")
print(a)

a.add("박지원")
print(a)

a.add("박지원")
print(a)

a.add("문태현")
print(a)

a.remove("박세정")
print(a)

# in 연산자 사용 가능
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 합집합 구하기 |
print(set1 | set2)



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
