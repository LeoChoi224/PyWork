print('🟦 함수 Function')

print("안녕하세요")
print("제 이름은 최한빈 입니다")

print("안녕하세요")
print("제 이름은 이승원 입니다")

print("안녕하세요")
print("제 이름은 김기현 입니다")

print("안녕하세요")
print("제 이름은 김유진 입니다")

# 반복되는 코드들이 보인다...

print('\n🟦 함수는 왜 만드나?')

# 프로그래밍에서 동일한(혹은 거의 비슷한) 내용의 코드가 반복될때가 있다.
# 바로 이러한 코드 낭비를 없애기 위해
# 반복되는 코드를 묶어서 하나의 함수로 정의해 놓고 사용하는 것이다

# 즉, 반복되는 부분이 있을 경우 "반복적으로 사용되는 가치 있는 부분"을 
# 한 뭉치로 묶어서 
# "1. 어떤 입력값을 주었을 때, 
#  2. 어떠한 일을 수행하고, 
#  3. 어떤 결과값을 돌려준다" 라는식의 
# 함수로 작성하는 것이 현명하다.

# ✅ 함수 만들기 (함수 정의 : Function Definition)

# def 키워드로 작성

# def 함수이름( 매개변수 들):
#     함수 본체 <수행할 문장1>
#     함수 본체 <수행할 문장2>
#     ...

# 함수의 동작 정의
#   입력(매개변수) -> 본체 수행 -> 결과(리턴)

# 함수이름은 변수 이름 작성과 거의 동일한 규칙

#----------------------------------------------------------

# ✅ 함수 호출 (함수 사용 )  Function call, invoke
# 함수호출시 넘겨지는 인자(parameter) 값들은
# 함수의 매개변수(argument)들이 받습니다.
# 매개변수는 0개, 한개, 여러개 있을수 있을수 있습니다

# 함수에는 리턴값이 있다.
# 리턴값은 함수를 호출(call) 한쪽에 돌려준다
# return 키워드로 리턴값을
# 함수 본체 수행중 return 을 만나면 함수를 종료 하게 됩니다
# 어떠한 타입도 리턴할수 있다.
# 리턴값은 없을수도 있다. None 리턴

# 함수정의
def say_anthem():
    print('동해물과 백두산이')
    print("마르고 닳도록")
    print("하느님이 보우하사")
    print("우리나라 만세")

# 함수호출
say_anthem()
print('💚' * 10)
say_anthem()
print('🧡' * 10)

# 함수도 '데이터 타입' 이다!
print(type(say_anthem)) # function타입

uuu = say_anthem
uuu()

print('\n🟦매개변수(parameter, argument)') # 정확한 명칭은 함수 정의 시 매개변수-parameter, 함수 호출 시 인자-argument

def say_name(name): # 매개변수 name, '함수의 입력' 이라고도 함
    print("안녕하세요")
    print(f"제 이름은 {name}입니다.")

# 매개변수 지정된 함수는 호출시 
# 반드시 매개변수에 넘겨줄 값 (인자값)이 있어야 한다

# sayName(인자값들...)

say_name('박수연')
say_name('권용현')
say_name('박지원')

# say_name() # 호출할때 빼먹으면 에러!
# TypeError: say_name() missing 1 required positional argument: 'name'

def say_age(age):
    print("제 나이는요...")
    print(age, "살 입니다.")

say_age(100)
say_age(23)
say_age(77)

# 함수 안에서 다른 함수 호출 쌉가능.
def say_hello(name, age):
    print('-' * 20)
    say_name(name)
    say_age(age)
    print('-' * 20)

say_hello("박지원", 30) # 정의된 순서대로 전달 positional argument
say_hello("양정운", 22)
say_hello("장희준", 27)

# 함수 호출 시 매개변수 명시 가능.  keyword argument.
say_hello(name='김정준', age=28)
say_hello(age=28, name='김정준')

say_hello(28, '김정준')

# say_hello('신하석')
# say_hello(name='신하석', age=36, address='서울')
# TypeError: say_hello() got an unexpected keyword argument 'address'

# say_hello(age=39)
say_hello('이희본', age=39)

# 함수 호출 관련 디버깅 명령
# step into : 실행할 함수 내부로 이동
# step out : 실행중인 함수 리턴까지 진행
# 호출스택 (call stack) : 함수 호출관계 모니터링

"""
함수이름 작명
- 관례적으로 소문자로 시작.
- 복합단어인 경우 _(underbar) 사용
    say_name - Python    sayName - java,c#,JS...
- 동사로 시작하는 걸 권장.
"""

print("\n🟦 return [값]")
#  -- 함수 종료
#  -- 호출한 쪽으로 '값 하나' 을 돌려준다 

def code_everyday():
    print("파이썬 열공중")
    print("Life is short")
    print("You need Python")
    return

code_everyday()

def code_everyday(): # 함수 재정의 (덮어쓰기)
    print("파이썬 열공중")
    print("Life is short")
    return # 함수 종료.
    print("You need Python")

code_everyday()

# 입력: 두개의 수를 입력 받아서 
# 수행: 덧셈을 수행한뒤
# 리턴: 덧셈 결과를 리턴

def add(a, b):
    result = a + b
    return result # 리턴값

t = add(10, 20)
print(t)
print(add(11, 22))

print(add(100, add(10, 20)))

#              add(10, 20)
#                  ↓ return
#     add(100,    30)
#           ↓ return
#  print(  130  )

stopword_list = ['바보', '멍충이'] # 금지어 

def register_comment(comment):
    for stopword in stopword_list:
        if stopword in comment:
            print('💥등록 불가 댓글')
            return
        
    print('✔ 댓글 등록 진행 합니다')

register_comment('안녕하세요 좋은 아침입니다')
register_comment('이 바보같은 하루')

print('\n🟦 함수의 리턴값은 여러개다?')
# 결론적으로 말하자면 함수의 리턴 값은 오직 '하나' 다
# 그런데 파이썬에선 여러개의 값도 리턴이 가능했다!  어떻게 가능?  tuple 로 리턴하면 가능하다.
# 기술적으로는 tuple 하나 만 리턴했지만, tuple 안에 값이 여러개 있기 때문에
# 여러개의 값을 리턴한것과 같은 효과를 보는것이다

def sum_and_mul(a, b):
    return a + b, a * b # 두개를 리턴한게 아니라. 두개의 값이 담긴 tuple 하나를 리턴한거다!

result = sum_and_mul(4, 3)
print(result, type(result))
print(f'합 {result[0]} 곱 {result[1]}')

s, m = sum_and_mul(30, 40)
print(f'합 {s}, 곲 {m}')

# 파이썬 내장 함수 중에도 리턴값이 tuple 로 하는 함수들 많~~다.
quotient, remainder = divmod(10, 3) # 나눈 '몫' 과 '나머지' 리턴
print(quotient, remainder)

print('-' * 20)

def get_name(animal):
    return animal['name']

dog = {'name': '흰둥이'}
print(get_name(dog))

dog = None
# print(get_name(dog)) # 에러

print('\n🟦 매개변수 검증에 SCE 활용 가능')
# 매개변수 검증
def get_name(animal):
    if animal and animal.get('name'):
        return animal['name']

print(get_name(dog))

def get_name(animal):
    name = animal and animal.get('name')
    return name or '이름이 없는 동물'

print(get_name(dog))

dog = {'color': 'brown'}
print(get_name(dog))

dog = {'color': 'brown', 'name': '댕댕이'}
print(get_name(dog))

print("\n🟦 디폴트 매개변수 (Default Arguments)")

# 함수정의시 매개변수에 디폴트 값을 지정해 주면,  호출시 생략가능하다
# 생략된 상태에서 호출되면 디폴트 값으로 작동된다

# 디폴트 매개변수 작성 구문
#    def 함수명(매개변수명=디폴트값)

def say_myself(name, old, gender='M'):
    print(f"제 이름은 {name} 입니다")
    print(f'나이는 {old} 입니다')
    
    # (gender == 'M') and print('남자입니다')
    # (gender == 'F') and print('여자입니다')

    # match gender:
    #     case 'M': print('남자입니다')
    #     case 'F': print('여자입니다')

    print({'M': '남자입니다', 'F': "여자입니다"}[gender])
    
    print()

say_myself('고길동', 43, 'M')
say_myself('홍길동', 25)

print('\n🟦 Argument Packing')

# ✅ positional argument packing
# def 함수이름(*매개변수): 
#     <수행할 문장>
#     ...

# argument packing
# 입력값이 몇개가 올른지 모르는 경우, 임의 개수의 positional argument 를 packing 하여 받는다

# 함수 호출시 전달된 복수개의 매개변수를 하나의 tuple 의 형태로 묶여서(packing) 받을수 있다.
# 매개변수 이름은 어떠한 이름으로도 가능하긴 하나  관례적으로 args (arguments) 를 많이 사용한다

def var_args(*args):
    print(type(args), args)

var_args(10)
var_args(10, 20, 30)
var_args()

def sum_many(*args):
    result = 0
    for num in args:
        result += num
    return result

print(sum_many(10, 20, 30))
print(sum_many(0.1, 10.4, 213.3435, -455.33))

# ✅ keyword arguments packing
#   kwargs : keyword arguments 약자

# def 함수이름(**매개변수):
#     <수행할 문장>
#     ...

# 함수호출시 함수의 인수로 key = value 형태로 주어지면
# 함수에선 kwargs 가 dict 형태로 packing 하여 받아옴

def func_kwargs(**kwargs):
    print(type(kwargs), kwargs)

# func_kwargs('john')
func_kwargs(name = 'John')    
func_kwargs(name = 'John', age = 32, address='Seoul')

def func(*args, **kwargs):
    print(args, kwargs)

func('john')
func('john', 1, 2, 3, name='Foo', age=4)
# func('john', 1, 2, 3, name='Foo', age=4, 100)
# ↑ 함수 호출시 keyword argument  다음에 positional argument  명시 불가

# 키워드 형태의 인수뒤에 키워드 형태가 아닌 인수는 올 수 없음
# def func(*args, **kwargs):
#     print(args, kwargs)

print("\n🟦Argument Unpacking")
# 함수 호출할때 *iterable  -> unpacking 되어 positional argument 로 함수에 전달

# 함수 호출할때 **dict  -> unpacking 되어 keyword argument 로 함수에 전달

def print_val(kor, eng, math):
    print(kor, eng, math)
    print('총점=', kor + eng + math)

print_val(10, 20, 30)

score = [11, 22, 33]

# print_val(score) # 에러  score -> kor 에만 전달
print_val(score[0], score[1], score[2])
print_val(*score) # -> print_val(11, 22, 33) argument unpacking
print(*(100, 200, 300))

student = {"name": "Sam", "email": "sam@mail.com"}

def print_dict(name, email):
    print(name, email)

print_dict(name = student['name'], email = student['email'])
# print_dict(student)
print_dict(**student) # dict 를 ** 로 unpacking => print_dict(name="Sam", email="sam@mail.com")

print_dict(*student) # dict 를 * 로 unpacking? -> (key1, key2, ...) 형태로 호출

# log(10, 20, 30) 호출하면
# print(10, 20, 30) 으로 동작하게 하려면?

def log(*args, **kwargs):   # packing
    print(*args, **kwargs)  # unpacking

log(10, 20, 30)
log(1, 2, 4, 5, 5, end=' ', sep='🐹')

print("\n🟦 키워드 전용 인자 (Keyword-only argument)")
# 함수정의시 매개변수에 "*" 를 명시하면 ⭐️
# 이후의 매개변수에 대해서는 반드시 명시적으로 매개변수명을 사용하여 호출하든지 (keyword argument)
# dict 를 unpacking하여 호출해야 한다

def print_dict(idx, *, name, email):
    print(idx, name, email)

# 이후의 매개변수에 대해서는 반드시 명시적으로 매개변수명을 사용하여 호출
print_dict(10, name="hone", email="hhh@mail.com")
# print_dict(10,"hone", "hhh@mail.com")

# dict 를 unpacking하여 호출
dict2 = {'name': "Kim", "email": 'kim@mail.net'}
print_dict(22, **dict2)

print("\n🟦 재귀호출 (recursive call)")
#- 함수가 자기 자신을 다시 호출하는 구조
#- 장점: 프로그램을 구조적으로 작성, 복잡한 문제를 단순화! 추상화!
#- 단점; 메모리 부담 발생

# def recursive(n): # RecursionError: maximum recursion depth exceeded
#     print(n, end=' ')
#     recursive(n + 1) # 재귀호출
#     print('종료') # 영원히 루프함

# recursive(1)

# factorial
# 4! => 4 x 3 x 2 x 1
# 1! => 1
# 0! => 1

# n! = n x (n -1) * (n -2) * ... * 1
# n! = n x (n -1)!  <- factorial 을 factorial 로 정의 (재귀적 정의)

def factorial(n):
    if n == 0: return 1 # 종료 조건 0! = 1

    if n < 0:
        print('💢음수 팩토리얼은 불가!')
        return 0
    
    return n * factorial(n - 1) # 재귀호출 결과 리턴

for i in range(1, 11):
    print(f"{i}! = {factorial(i)}")

print(factorial(4))
#       4 x factorial(3)
#             3  x factorial(2)
#                     2  x factorial(1)
#                              1 x factorial(0)


# https://jungol.co.kr/problem/231?cursor=MiwxMiwxMw==

def print_num(k):
    if k < 1 : return

    print_num(k // 2)

    print(k, end = " ")

n =100
print_num(n)

print("\n🟦 파이썬의 내장함수( built-in functions)")
# 별도의 import 없이 바로 사용 가능한 함수들.

# 레퍼런스 :  https://docs.python.org/3/library/functions.html
        
# abs()	dict()	help()	min()	setattr()
# all()	dir()	hex()	next()	slice()
# any()	divmod()	id()	object()	sorted()
# ascii()	enumerate()	input()	oct()	staticmethod()
# bin()	eval()	int()	open()	str()
# bool()	exec()	isinstance()	ord()	sum()
# bytearray()	filter()	issubclass()	pow()	super()
# bytes()	float()	iter()	print()	tuple()
# callable()	format()	len()	property()	type()
# chr()	frozenset()	list()	range()	vars()
# classmethod()	getattr()	locals()	repr()	zip()
# compile()	globals()	map()	reversed()	__import__()
# complex()	hasattr()	max()	round()	 
# delattr()	hash()	memoryview()	set()	 

print(abs(-111))
data = [10, 20, 30, 40]
print(min(data), max(data), sum(data))

print(type(sum))

# 실수로 내장함수를 덮어쓰기 한 경우..
print(sum([10, 20]))

sum = 10 + 20
# print(sum([10, 20])) # 에러

sum = __builtins__.sum # 복원
print(sum([10, 30]))

print('\n' * 15)