print('\n🟦 정규표현식 regular expression') # 파이썬 내에서 다루는 방식

# 문자열 검색, 치환  등의 동작에 있어서
# 단순한 '문자열 비교' 를 하는 것이 아니라 
# 특정 '패턴'과 비교하고자 할때 이를 단 몇줄의 코드로 구현 가능!
# 주어진 문자열에서 패턴을 찾아내는 것을 '패턴 매칭(pattern matching)' 이라 함

# 사용자가 입력한 문자열 패턴 유효성 체크 등에 많이 사용
#  		ex) 주민등록번호, URL, email, 비밀번호, 
#  			날짜포맷(yyyy-mm-dd) 
#  			전화번호(010-xxxx-xxxx) ... 

# 장점: 코딩량 저감, 거의 대부분의 언어에서 공용으로 사용.
# 단점: 처음에 배우기 어렵고, 코드 가독성 떨어뜨림.

# 정규표현식 연습 사이트 추천 TODO
# : https://regexr.com/    (정규식 , 문자열 매칭 연습)
# : https://regexone.com/  ( step by step 으로 연습 하기 좋음)
# : https://regexper.com/  (특징: 시각화, 정규식을 이미지로 다운가능)
# : https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html  (오라클 공식)

print("\n🟦 정규표현식 기본 모듈 re")

# 정규표현식 패턴문자열 -> re.compile -> Pattern 객체 생성
# Pattern 객체의 메소드를 사용하여 패턴 매칭 (검색, 치환) --> Match 객체 결과

import re

print('\n🟦 대표적인 정규표현식')
#  ^ 문자열 시작
#  $ 문자열 종료
#  . 임의의 문자 [단 ‘'는 넣을 수 없습니다.]
#  * 앞 문자가 0개 이상의 개수가 존재할 수 있습니다.
#  + 앞 문자가 1개 이상의 개수가 존재할 수 있습니다.
#  ? 앞 문자가 없거나 하나 있을 수 있습니다.
#  [] 문자의 집합이나 범위를 표현합니다. -기호를 통해 범위를 나타낼 수 있습니다. ^가 존재하면 not을 나타냅니다.
#  {} 횟수 또는 범위를 나타냅니다.
#  () 괄호안의 문자를 하나의 문자로 인식합니다. (그룹)
#  | 패턴을 OR 연산을 수행할 때 사용합니다.
#  \s 공백 문자
#  \S 공백 문자가 아닌 나머지 문자
#  \w 알파벳이나 숫자
#  \W 알파벳이나 숫자를 제외한 문자
#  \d [0-9] 숫자
#  \D 숫자를 제외한 모든 문자

regex = 'My....'  # My 로 시작하고 임의의 문자 4개에 매칭
# "My1234", "My abc", "My%$#@"   <- 전체 매칭!
# "my1234", "My123", "asdfasdfed"  <- 매칭 없슴
# "aaaaaMybbbbbb"  <- 부분 매칭
# "MyAlbum MyGoods My Birthday" <- <- 매칭은 여러개 발생 가능.

print("\n🟦 Pattern, Match 객체")
pat = re.compile(regex)  # Pattern 객체 생성 <- 정규표현식 문자열
print(pat, type(pat))

# 입력문자열
str_input = "-My1234-"

match = pat.search(str_input)  # 입력문자열에 대해 정규표현식 패턴매칭 수행 -> Match 객체 리턴.
print(match)

match = pat.search("hello") # 매칭되는게 없으면 None 리턴
print(match)

str_input = "MyAlbum MyGoods My Birthday" 
match = pat.search(str_input) # 첫번째 매칭 결과만 리턴
print(match)

print(pat.findall(str_input))  # 매칭된 모든 결과들을 (Match 객체들)의 list 리턴

print(pat.finditer(str_input))  # 매칭된 모든 결과들을 (Match 객체들)의 iterable 리턴

for match in pat.finditer(str_input):
    print(match)


print('\n🟦 Match 객체의 메소드들')

# 어떤 문자열이 매치되었는가?
# 매치된 문자열의 인덱스는 어디서부터 어디까지인가?

# group()	매치된 문자열을 리턴한다.
# start()	매치된 문자열의 시작 위치를 리턴한다.
# end()	매치된 문자열의 끝 위치를 리턴한다.
# span()	매치된 문자열의 (시작, 끝) 에 해당되는 튜플을 리턴한다.

m = pat.search('-My1234-')
print(m)

print(m.group())
print(m.start())
print(m.end())
print(m.span())

# 패턴안의 여러 그룹.

# 종규표현식 패턴 안에서 ( ) (괄호) 로 묶으면 '그룹'이 된다
p = re.compile('(My)(....)')

m = p.match("-My1234-")  # '전체' 매칭 수행
print(m)  # None

m = p.search("-My1234-")  # '전체' 매칭 수행
print(m.group())
print(m.start())
print(m.end())
print(m.span())

print(m.group(1)) # 1번 그룹
print(m.start(1))
print(m.end(1))
print(m.span(1))

print(m.group(2)) # 2번 그룹
print(m.start(2))
print(m.end(2))
print(m.span(2))

print()
print(m.group(0)) # 0 은 default, 매개변수 없을때와 동일
print(m.start(0))
print(m.end(0))
print(m.span(0))


print("\n🟦 re 의 함수")
# re.match(), re.search(), re.findall(), re.finditer()
# re.compile + match() 의 축약형

m = re.match('My....', 'My1234')
print(m)

m = re.search('My....', '-My1234-')
print(m)

print(re.findall('My....', str_input))


# 패턴을 명시할 때, r 문자를 사용하는 것을 볼 수있다. 

p = re.compile(r'(\d+)/(\d+)/(\d+)') 

# r 문자는 raw string으로 백슬래시 문자를 escaping하지 않고 남겨두기 때문에 정규표현식과 같은 곳에 유용하다. 
# 예를 들어 r문자를 사용하지 않는다면

p = re.compile('(\\d+)/(\\d+)/(\\d+)') 
# 와 같이 길어 백슬래시를 두 번 사용해야 하는 불편함이 있다. 그래서 보통 r문자를 붙여준다.


print('\n🟦 정규표현식을 활용한 치환')
#  re.compile() + sub()
#  re.sub()

a = "123456-1234567"
print(re.search("-", a))
print(re.sub("-", "", a))

# 숫자 문자 한개 \d
print(re.sub(r'\d', '*', a))    

# 숫자 문자 한개 \D
print(re.sub(r'\D', "*", a))

# 부정기호 [^]
print(re.sub(r'[^\D]', "*", a))


data = """
park 800905-1049118
kim  700905-1059119
"""


print(data)
p = re.compile(r"(\d{6})[-]\d{7}")
print(p.sub(r'\g<1>-*******', data))

print(re.sub(r"(\d{6})[-]\d{7}", r'\g<1>-*******', data))

data = """
    동해물과 백두산이
    마르고 닳도록
    
    하느님이 보우하사
    우리나라 만 세~
"""

print(data)

print(data.split())
print(data.split("이"))

print(re.split('이', data))
print(re.split(r'\s+', data.strip()))



print('\n' * 15)