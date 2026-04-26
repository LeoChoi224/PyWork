print("\n🟦 문자열 메소드")

# 위의 double(), add() 와 같이 단독으로 사용 가능한 함수들도 있고
# 특정 객체에서만 동작하는 함수들도 있다.  (이러한 함수를 메소드(method) 라고도 한다)

# 이러한 메소드 사용(호출) 하는 구문은
#   객체.함수(인자..)

# 객체(object)와 메소드(method)를 정의하고 사용하는 것은 class 단원에서 다룹니다

for d in [
    "\n🟦 upper(), lower()",
    # upper() : 문자열을 전부 대문자로 만드는 함수
    # lower() : 문자열을 전부 소문자로 만드는 함수

    str1 := "Apple",
    (str1.upper(), str1.lower()), # 리턴값이 있기 때문에 원본 변화 없음
    str1, # 원본 변경 안함

    "Car" == "car",  # 대문자와 소문자는 다르다!
    "Car".upper() == "car".upper(),  # True 같은 문자열 (동등성 비교)
    "Car".upper() is "car".upper(),  # False 다른 객체 (동일성 비교)

    # 실제 이는 아래와 같이 동작한다
    # 'car'.upper() => str.upper('car')
    #  적용되는 메소드(함수) 이름은 str.upper 다
    #  이를 map,filter,reduce 등에서 적용 가능하다
    str.upper,
    ('car'.upper(), str.upper('car')),

    "\n🟦 strip()",
    # 문자열의 좌우 공백 제거
    a := "   Hello, World!    ",  
    f"[{a}]",
    f"[{a.strip()}]", # 웹,앱등 서비스 환경에서 입력된 문자열값은 기본적으로 좌우 공백 제거 하도록 하자.
    # str 은 immutable --> str 메소드의 결과로 원본이 변화되진 않는다. 
    # str 메소드의 리턴값이 str 이라면, 메소드 체이닝 (chaining)이 가능하다.
    f"[{a.strip().upper()}]",  


    "\n🟦 replace()",
    # replace(a, b)  문자열 치환
    # 주어진 문자열에서 a 를 찾아 b 로 치환
    a := "Hello World!",
    a.replace('l', 'J'),

    a := "  21,300원  ",
    # 도전
    # "  21,300원 "  --> 정수 21300 으로 바꾸기

    int(a.strip().replace(',', '').replace('원', '')),

    "\n🟦 split(), join()",
    animals := ['야옹이', '먼지', '누렁이', '두부'],

    data := "-".join(animals),
    data.split("-"),

    "강아지 고양이 종달새".split(),  # 매개변수 없으면 공백기준으로 쪼갬.
    "강아지 고양이 종달새".split(" "), # 비추

    "  강아지   고양이   종달새   ".split(),
    "  강아지   고양이   종달새   ".split(" "),

    data := "데이터 분석을 위한 파이썬 프로그래밍",
    # "파이썬" 을 => "Python" 으로 바꾸려면?
    data.replace('파이썬', 'Python'),

    # 위 동작을 join, split 으로 만들 수 있다?
    # data.split('파이썬')
    "Python".join(data.split('파이썬')), # 치환하는 효과

    "\n🟦 index(), find()",
    # 주어진 문자열을 '찾으면' 원본문자열 내의 index 리턴 (0 이상의 값)
    # 못찾으면
    #   index() 는 ValueError
    #   find() 는 -1 리턴

    a := "hello python",

    a.index('lo'),
    a.index('l'),
    a.find('lo'),
    a.find('l'),

    # a.index('x'), # ValueError: substring not found
    a.find('x'), # -1


    "\n🟦 count()",
    # 문자열 내에서 특정 문자열 패턴의 반복 횟수 
    a := "aaabbbababaabbbababbbaaaabab",
    a.count("a"),
    a.count("ba"),

    '\n🟦 startswith(), endswith()',
    # 문자열이 특정 문자열로 시작/종료 하는지 여부
    a := "https://www.nytimes.com/2000/01/01/news/visions-identity-a-generation-s-anthem-smells-like-teen-pressure.html",
    a.startswith('http'),
    a.startswith('ftp'),
    a.endswith('.html'),

    '\n🟦 패딩 zfill(), rjust(), ljust()',
    "1".zfill(4), # 비어있는 자리까지 원하는 자리로 맞춰줌
    "2".zfill(4),
    "34".zfill(4),
    "777".zfill(4),
    "10101".zfill(4),

    "1".rjust(5, '*'), # 비어있는 자리에 원하는 문자로 대체, 우측정렬
    "2".rjust(5, '*'),
    "34".rjust(5),
    "777".rjust(5, '*'),
    "101010".rjust(5, '*'),
    
    "1".ljust(5, '*'), # 비어있는 자리에 원하는 문자로 대체, 좌측정렬
    "2".ljust(5, '*'),
    "34".ljust(5, '*'),
    "777".ljust(5),
    "101010".ljust(5, '*'),

    '\n🟦 ord() chr()',
    # ord() : 문자의 코드값
    # chr() : 코드의 문자값
    (ord('a'), ord('A')), # 97, 65
    (chr(97), chr(65)), # 'a', 'A'

    # 알파벳 개수
    ord('z') - ord('a') + 1,
    # 한글 개수
    ord('힣') - ord('가') +1,
    # (ord('가'), ord('ㄱ')),

    data := [
        "aAaA",   # 1
        "aaAA",   # 2
        "AAaa",   # 3
        "AaAa"    # 4 
    ],
     sorted(data), # 3 - 4 - 1 - 2

]: print(d)


print("\n🟦 계수하기 (갯수 세기)")
# 등장하는 알파벳의 개수 -> dict 결과 만들기
# Dict Comprehension 사용 
# 대소문자 구분 하지 않기, 1개 이상 등장하는 알파벳만
# hint : 알파벳 리스트 , lower, upper, count 

word = "Alice in wonderland"

# {'a': 2,
#  'c': 1,
#  'd': 2,
#  'e': 2,
#  'i': 2,
#  'l': 2,
#  'n': 3,
#  'o': 1,
#  'r': 1,
#  'w': 1}


print(word)

# 방법1: dict 활용, 전통적 방법
result = {}

for ch in word.lower():
    # if 'a' <= ch <= 'z':
    if ch.isalpha():
        if not result.get(ch): # 첫 등장이며
            result[ch] = 1
        else: # 이전에 한번이라도 등장했다면.
            result[ch] += 1
    
    print(f'{ch} -> {result}')

print(result)

print('-' * 20)

# 방법2: get() + default 값 활용
result = {}

for ch in word.lower():
    if ch.isalpha():
        result[ch] = result.get(ch, 0) + 1

print(result)

print('-' * 20)

# 방법3: count()
result = {}

for ch in word.lower():
    if ch.isalpha():
        result[ch] = word.lower().count(ch)

print(result)

print()

# comprehension 사용
print({
    ch: word.lower().count(ch)
    for ch in word.lower()
    if ch.isalpha()
})





print('\n' * 15)