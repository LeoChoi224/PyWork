# 파이썬의 가장 기본적인 출력 함수 print()

# print( 출력내용1, 출력내용2, 출력내용3, ...)
#  위와 같이 print() 함수의 parameter 로 출력할 내용들을 기입하면 된다

# print() 함수는 출력한후 자동적으로 "줄바꿈" 됩니다 (디폴트)

print(100)
print('로켓')
print('모카')
print()
print(10, 20, 30)

# end parameter
# end=   : 출력후에 마무리로 출력할 문자열
print('-' * 20)

print(10, end="*")
print("Hello", end='')
print(3.14)


# sep=   : 여러값 출력시 중간에 출력할 문자열
print(10, 20, 30, sep="**")

# 🟦 이스케이프 문자 (escape character)
# '문자열' 내에서 특수한 문자 출력할때 사용
# \와 조합하여 정의됨

# 많이 사용되는 이스케이프 코드
#    \n : 줄바꿈
#    \t : 탭
#    \\ : 역슬래시
#    \' : 홀따옴표
#    \" : 쌍따옴표

print("He \nsays \"I'm fine\"")
print("""
    He says "I'm fine"
      """)


# Windows 의 file seprator 는 back slash \
# Linux, Mac 의 ...           slach /

path = "C:\Program Files\Microsoft\011_python\times"
print(path)

path = "C:\\Program Files\\Microsoft\\011_python\\times"
print(path)

# r-string
# raw-string : 문자열내 escaping 처리 안함
path = r"C:\Program Files\Microsoft\011_python\times"
print(path)


# 🟦 문자열 포맷팅 (formatting)
print()
print("🟦 문자열 포맷팅 (formatting)")

# 방법#1 % 연산자 사용
# 서식지정자(format specifier) 를 포함한 문자열과,
#  각 '서식문자'에 대응하는 데이터들을 연결하여 문자열 완성

# 구문)
#    "서식문자포함문자열" % ( 데이터 튜플 )

a = "Hello %s"
print(a)

a = "Hello %s" % ("파이썬")
print(a)

a = "Hello %s" % ("자바")
print(a)

# a = "My name is %s, I'm %d yrs old" % ("자바") # TypeError: not enough arguments for format string
a = "My name is %s, I'm %d yrs old" % ("최홍묵", 31)
print(a)

# format specifier
#  https://docs.python.org/2/library/string.html

# %d   십진수 정수
# %f   실수
# %s   문자열
# %%   %문자 자체

import math
pi = math.pi # 원주율값
print('pi=', pi)

print("원주율은 %f 입니다" % (pi))
print("원주율은 %.2f 입니다" % (pi))
print("원주율은 %.4f 입니다" % (pi))

a, b, c, d = 10, 100, 1000, 10000
print("%d:%d:%d:%d:" % (a, b, c, d))
print("%5d:%5d:%5d:%5d" % (a, b, c, d))
print("%-5d:%-5d:%-5d:%-5d" % (a, b, c, d))

# 방법#2 .format() 사용
a = "My name is {} , I'm {} yrs old".format("최홍묵", 31)
print(a)

a = "My name is {} , I'm {} yrs old".format(31, "최홍묵")
print(a)

a = "My name is {name} , I'm {age} yrs old".format(age = 31, name = "최홍묵")
print(a)

print("원주율은 {p} 입니다.".format(p = pi))
print("원주율은 {p:.2f} 입니다.".format(p = pi))

# 방법#3  f-string 사용
lang = 'Python'
author = 'Guido van Rossum'

print("Lauguge: %s, Author: %s" % (lang, author))
print("Lauguge: {}, Author: {}".format(lang, author))
print(f"Lauguge: {lang}, Author: {author}")

print(f"원주율은 {pi} 입니다.")
print(f"원주율은 {pi:.2f} 입니다.")

num = 1234567890
print(f'num은 {num} 입니다.')
print(f'num은 {num:,} 입니다.')

# 연습
# 다음 출력 예와 같이 모든 단어를 15칸씩 오른쪽에 맞추어 출력되는 프로그램을 작성하시오.
# [출력결과]
#           Seoul     10,312,545        +91,375
#           Pusan      3,567,910         +5,868
#         Incheon      2,758,296        +64,888
#           Daegu      2,511,676        +17,230
#         Gwangju      1,454,636        +29,774

print("[출력결과]")
area, pop, inc = "Seoul", "10,312,545", "+91,375"
print("%15s%15s%15s" % (area, pop, inc))
area, pop, inc = "Pusan", "3,567,910", "+5,868"
print("%15s%15s%15s" % (area, pop, inc))
area, pop, inc = "Incheon", "2,758,296", "+64,888"
print("%15s%15s%15s" % (area, pop, inc))
area, pop, inc = "Daegu", "2,511,676", "+17,230"
print("%15s%15s%15s" % (area, pop, inc))
area, pop, inc = "Gwangju", "1,454,636", "+29,774"
print("%15s%15s%15s" % (area, pop, inc))


print("[출력결과]")
area, pop, inc = "Seoul", "10,312,545", "+91,375"
print("{:>15}{:>15}{:>15}".format(area, pop, inc))
area, pop, inc = "Pusan", "3,567,910", "+5,868"
print("{:>15}{:>15}{:>15}".format(area, pop, inc))
area, pop, inc = "Incheon", "2,758,296", "+64,888"
print("{:>15}{:>15}{:>15}".format(area, pop, inc))
area, pop, inc = "Daegu", "2,511,676", "+17,230"
print("{:>15}{:>15}{:>15}".format(area, pop, inc))
area, pop, inc = "Gwangju", "1,454,636", "+29,774"
print("{:>15}{:>15}{:>15}".format(area, pop, inc))

print("[출력결과]")
area, pop, inc = "Seoul", "10,312,545", "+91,375"
print(f"{area:>15}{pop:>15}{inc:>15}")
area, pop, inc = "Pusan", "3,567,910", "+5,868"
print(f"{area:>15}{pop:>15}{inc:>15}")
area, pop, inc = "Incheon", "2,758,296", "+64,888"
print(f"{area:>15}{pop:>15}{inc:>15}")
area, pop, inc = "Daegu", "2,511,676", "+17,230"
print(f"{area:>15}{pop:>15}{inc:>15}")
area, pop, inc = "Gwangju", "1,454,636", "+29,774"
print(f"{area:>15}{pop:>15}{inc:>15}")

print("[출력결과]")
data = [
    ("Seoul", "10,312,545", "+91,375"),
    ("Pusan", "3,567,910", "+5,868"),
    ("Incheon", "2,758,296", "+64,888"),
    ("Daegu", "2,511,676", "+17,230"),
    ("Gwangju", "1,454,636", "+29,774")
]

for area, pop, inc in data:
    print(f"{area:>15}{pop:>15}{inc:>15}")
