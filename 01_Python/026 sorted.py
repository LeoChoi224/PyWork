print('\n🟦 sorted() 함수')
#   sorted(iterable, /, *, key=None, reverse=False)
#   https://docs.python.org/ko/3/library/functions.html#sorted

#   iterable 의 항목들을 정렬하여 '리스트'를 리턴
#   key= 에 정렬 조건을 '식' 이나 '함수'로 지정해줄수 있다.
#       함수의 경우 매개변수 1개, 리턴값 1개 형태

#  list.sort() vs sorted()
#     같은점  key= 와 reverse= 매개변수 있다.
#     다른점  
#         list.sort 는 원본 변화  -> None 리턴
#         sorted() 는 원본 변화 없음 -> 정렬결과 리턴

"""
sorted

(function)
def
sorted ( iterable: Iterable[SupportsRichComparisonT@sorted],
/, -> 여기까지가 포지셔닝 아규먼트
*, -> 여기서부터 키워드 아규먼트
key: None = None,
reverse: bool = False
list [SupportsRichComparisonT@sorted]:..
def
sorted ( iterable: Iterablel Tasortedl.
"""

dataset = [5, 4, 2, 8, 1]
print(dataset)
print(dataset.sort()) # 원본 변경
print(dataset)

dataset = [5, 4, 2, 8, 1]
print(dataset)
print(sorted(dataset)) # 원본 변화 안됨.
print(dataset)

print('-' * 20)

# dataset = [('aas', 400), ('aasd', 300), ('aaad', 100), ('dasd', 200)] # 확인용
dataset = [('c', 400), ('a', 300), ('b', 100), ('d', 200)]
print(dataset)
dataset.sort() # 원소가 iterable 인 경우, '첫번째 원소'로 비교, sorted()도 동일
print(dataset)

dataset.sort(key=lambda item: item[1])
print(dataset)

dataset.sort(key=lambda item: item[1], reverse=True)
print(dataset)

print(sorted(dataset))
print(sorted(dataset, key=lambda item: item[1]))
print(sorted(dataset, key=lambda item: item[1], reverse=True))
print(dataset)

print('\n🟦 dict 정렬하여 출력하기')

# key 로 정렬하여 출력
# value 로 정렬하여 출력

a_dict = {"b": 5, "c": 3, "a": 2}
# a_dict.sort()  # .sort() 없다 !대신 sorted() 있다

# key 오름차순 결과
print(sorted(a_dict))

dict_items = a_dict.items()  # (key, value) 쌍으로 이루어진 iterable 객체

print(sorted(dict_items)) # key 오름 차순 정렬 (기본)
print(sorted(dict_items, reverse=True))  # key 내림차순

print(sorted(dict_items, key=lambda x: x[1])) # value 오름차순
print(sorted(dict_items, key=lambda x: x[1], reverse=True)) # value 내림차순


print('-' * 20)

from datetime import date
data = [
    {
        'name': 'James',  
        'age': 34,
        'birthdate': date(2021, 3, 4),
        'score': [100, 89, 88],
    },
    {
        'name': 'Amy',
        'age': 41,
        'birthdate': date(2005, 6, 21),
        'score': [56, 13, 97],
    },
    {
        'name': 'Kevin',
        'age': 23,
        'birthdate': date(1999, 11, 5),
        'score': [96, 88, 59],
    },    
]

for d in data: print(d)

# TypeError: '<' not supported between instances of 'dict' and 'dict'
# print(sorted(data)) # dict 는 대소 비교가 안된다

print('-' * 20)

# print(data.split().items(), type(data))
# print(data.split())

# 이름 오름차순
print(sorted(data, key=lambda x: x['name']))
        
# print(sorted(map(lambda x : x, data), key=lambda a: [1]))
# print(list(map(lambda x : x, data)))
# print(sorted(map(lambda x : x[1], data)))

# 나이 오름차순
print(sorted(data, key=lambda x: x['age']))

# birthdate 오름차순
print(sorted(data, key=lambda x: x['birthdate']))

# 평균 오름차순
print(sorted(data, key=lambda x: sum(x['score']) / len(x['score']) ))



print('\n' * 15)


