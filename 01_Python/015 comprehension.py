print("\n🟦 Comprehension 컴프리헨션")
# ※'내포표현식', '내포구문' 이라고도 함.

# ✅ List Comprehension  -->  list 안에 포함된 for문  --> list 생성
#     [표현식 for 항목 in 반복가능객체 (if 조건)]

# ✅ Dict Comprehension  -->  dict 안에 포함된 for문 --> dict 생성
#    {Key:Value for 항목 in 반복가능객체 (if 조건)}

# ✅ Set Comprehension -->  set 안에 포함된 for문 --> set 생성
#    {표현식 for 항목 in 반복가능객체 (if 조건)}

# ✅ Generator expression  --> 해당단위에서 학습 예정.

# Tuple Comprehsion은 없습니다.


# 주어진 리스트의 원소 데이터 들을 * 3 하여 새로운 리스트 작성하기
# ex) [1, 2, 3, 4] ==> [3, 6, 9, 12]

# 일단 지금까지 배운 방법으로 한다면

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)


result = [num * 3 for num in a]
print(result)

#  짝수에만 3을 곱하여 담고 싶다면 다음과 같이 "if 조건"을 사용할 수 있다
# [1, 2, 3, 4] --> [6, 12]

result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [
    num * 3
    for num in a
    if num % 2 == 0
    ]
print(result)

# 아래와 같이 짝수에만 적용되게 하려면? 홀수는 그대로.
# [1, 2, 3, 4]
#  ↓  ↓  ↓  ↓
# [1, 6, 3, 12]   <- 2, 4 에만 x3 적용

result = [num * 3 if num % 2 == 0 else num for num in a]

result = [
    num * 3 if num % 2 == 0 else num # 삼항연산자 사용
    for num in a
    ]
print(result)


print("\n🟦 for문 2개 이상 사용도 가능")

# [표현식 for 항목1 in 반복가능객체1 if 조건1
#         for 항목2 in 반복가능객체2 if 조건2
#         ...
#         for 항목n in 반복가능객체n if 조건n]

a = [2, 4, 6, 8]
b = ['a', 'b', 'c', 'd', 'e']

for i in a:
    for j in b:
        print(f'{i}-{j}')

print([f'{i}-{j}' for i in a for j in b])       
print([
    f'{i}-{j}'
    for i in a 
    for j in b
    ])        


# 구구단의 모든 결과를 담는 리스트
"""
['2 x 1 = 2',
 '2 x 2 = 4',
 ...
 '9 x 7 = 63',
 '9 x 8 = 72',
 '9 x 9 = 81']

"""
None

print([
    f"{i} x {j} = {i * j}"
    for i in range(2, 10)
    for j in range(1, 10)
    ])

print('-' * 20)

a = [10, 20, 30, -20, -3, 50, -70]

# 위 리스트에서 '양수'만 뽑아내어 새로운 리스트 만들기
# List comprehension 사용!
# 결과 -> [10, 20, 30, 50]

print([num for num in a if num > 0])

print([a for a in range(10)])
print(['최홍묵' for a in range(10)])
print([0 for _ in range(10)])

# 주어진 dataset 에서 제곱의 결과가 10보다 큰 결과만 담은 list 작성
# [1, -2, 3, -4, 5]
#  ↓ ↓
# [16, 25]
dataset = [1, -2, 3, -4, 5]

print([
    num ** 2
    for num in dataset
    if (num ** 2) > 10
    ])

print('-' * 20)

print([num % 3 for num in range(10)])
print({num % 3 for num in range(10)}) # Set Comprehension  # 중복 불가

print('-' * 20)

print({num:num % 3 for num in range(10)}) # Dict Comprehension

print({
    x: list(range(x))
    for x in [1, 2, 3, 4, 5]
})

fruits = {"apple": "red", "banana": "yellow", "peach": "pink"}

print(fruits)
for k, v in fruits.items():
    print(k, type(v))

for k in fruits.items():
    print(k, type(k))

print({k:v for k, v in fruits.items() })
print({
    k:v 
    for k, v in fruits.items() 
    })
print({k:v for k, v in fruits.items() if k != 'banana' })

print({k:v for k, v in fruits.items() if 'e' not in k})

print({k:v for k, v in fruits.items() if v != 'red'})




