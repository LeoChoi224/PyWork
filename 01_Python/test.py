# 문자열을 입력받고 정수를 입력 받아서 문자열의 맨 뒤부터 정수만큼 출력하는 프로그램을 작성하시오.

#  만약 입력받은 정수가 문자열의 길이보다 크다면 맨 뒤부터 맨 처음까지 모두 출력한다.

# (문자열 길이는 최대 100자 이하이다. )

# ==============================

# a, b = input().split()
# print(a[::-1][:int(b)])

# ==============================




# 공백을 포함한 문장을 입력 받아서 홀수 번째 단어를 차례로 출력하는 프로그램을 작성하시오.

# 문장의 길이는 100자 이하이다.

# 입력
# I like you better than him.

# 출력
# I 
# you 
# than


# ==============================

# list = input().split(" ")
# str = "\n".join(list[::2])

# print(str)

# ==============================

n = 5

print('\n1번', '=' * 14, end='\n')
for i in range(n):
    for j in range(0, n):
        if j <= i:
            print('*', end=' ')
    print()
print('=' * 18, end='\n')


print('\n2번', '=' * 14, end='\n')
for i in range(n):
    for j in range(n - i, 0, -1):
        print('*', end=' ')
    print()
print('=' * 18, end='\n')


print('\n3번', '=' * 14, end='\n')
for i in range(n, 0, -1):
    for j in range(1, n + 1):
        if j >= i:
            print('*', end=' ')
        else:
            print(' ', end= ' ')
    print()
print('=' * 18, end='\n')


print('\n4번', '=' * 14, end='\n')
for i in range(n):
    print('  ' * i, end='')
    for j in range(n - i, 0, -1):
        print('*', end=' ')
    print()
print('=' * 18, end='\n')


print('\n5번', '=' * 14, end='\n')
for i in range(n - 1, -1, -1):
    print('  ' * i, end='')
    for j in range(1, (n * 2) - (i * 2)):
            print('*', end=' ')
    print()
print('=' * 18, end='\n')


print('\n6번', '=' * 14, end='\n')
for i in range(n):
    print('  ' * i, end='')
    for j in range(1, (n * 2) - (i * 2)):
            print('*', end=' ')
    print()
print('=' * 18, end='\n')


print('\n7번', '=' * 14, end='\n')
for i in range(0, (n + 1) // 2):
    print(' ' * i * 4, end='')
    for j in range(1, (n + 1) - (i * 2)):
            print('*', end=' ')
    print()

for i in range((n // 2) - 1, -1, -1):
    print(' ' * i * 4, end='')
    for j in range(1, (n + 1) - (i * 2)):
            print('*', end=' ')
    print()
print('=' * 18, end='\n')


print("\n🟦 응용: CSV 파일 데이터 가공")
# CSV 파일 데이터의 형태에서
data = """height,weight,label
140,45,normal
145,72,fat
150,61,fat
137,56,fat
192,48,thin
175,77,fat"""  # <-- excel 에서 확인 가능하다!
print(data, type(data))


# 아래와 같은 리스트로 만들기
# [[140.0, 45.0, 'normal'],
#  [145.0, 72.0, 'fat'],
#  [150.0, 61.0, 'fat'],
#  [137.0, 56.0, 'fat'],
#  [192.0, 48.0, 'thin'],
#  [175.0, 77.0, 'fat']]

# while, for, if 안씁니다
# cond expr 사용 가능.  map 활용
result = []
result = list(map(lambda x: [x] , data.split('\n')))
print(result)


dataset = [1, 4, 3, 5, 2]
# reduce + lambda 를 사용하여 최댓값을 찾아보세요
from functools import reduce
print(reduce(
    lambda a, b: a if a > b else b,
    dataset,
))

# 아이템 계수하기
dataset = ["dog", "dog", "dog", "cat", "cat", "bird"]
print(reduce(
    lambda a, b: a.update({b: a.get(b, 0) + 1}) or a,
    dataset,
    {},
))
# 개수구하기 결과 =>  {'dog': 3, 'cat': 2, 'bird': 1}

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

# 이름 오름차순
print(sorted(data, key=lambda x: x['name']))

# 나이 오름차순
print(data.sort(key=lambda x: x['age']) or data)

# birthdate 오름차순
print(sorted(data, key=lambda x: x['birthdate']))

# 평균 오름차순
print(sorted(data, key=lambda x: sum(x['score']) / len(x['score'])))







