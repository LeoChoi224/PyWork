print("\n🟦 match ~ case 문")
# 파이썬 3.10 부터 도입
# C, Java 등의 switch-case 문과 비슷하지만 더 강력
# 공식명칭: 구조적 패턴 매칭 (Structural Pattern Matching)
#        https://peps.python.org/pep-0636/
#        https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching

# match-case 는 if-elif-else 를 대체하는 더 직관적인 문법
# 구조 패턴 매칭 가능 → 튜플, 리스트, 클래스, 딕셔너리 등 복잡한 데이터에도 적용
# |, _, if 등을 이용해 다양한 조건 표현 가능

# match <값> 형태로 시작
# 내부에는 case 블록이 여러 개.
# 위에서부터 차례대로 패턴이 매칭되면 해당 블록이 실행.

""" 구문
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
"""
None

print("\n🟦 match ~ case")

n = 2
# n = 7 아무 dace 블럭도 실행 안된다

match n:
    case 1:  # n 값이 1 인 경우 수행하는 블럭
        print('월요일')
    case 2:
        print('화요일')
    case 3:
        print('수요일')

print('종료')

print("\n🟦 _ 와일드카드")
# _ 는 와일드 카드 (무엇이든 매칭) 역할 수행
# 마지막 case 에만 사용 가능

n = 7

match n:
    case 1:  # n 값이 1 인 경우 수행하는 블럭
        print('월요일')
    case 2:
        print('화요일')
    case 3:
        print('수요일')
    case _:
        print('기타 요일')

print('종료')


print('\n🟦 여러값 매칭')
# | 연산자로 여러 패턴을 묶을 수 있습니다.  OR 연결 (pipe, vertical)

command = "run"

match command:
    case "start" | "run":
        print("시작합니다")
    case "stop" | "end":
        print("종료합니다")
    case _:
        print("알수 없는 명령")

print('종료')


print("\n🟦 구조적 매칭 (튜플, 리스트등)")
# 데이터의 형태(구조) 에 따라 분기할 수 있습니다.
point = (-4, 10) 

match point:
    case (0, 0):
        print('원점')
    case (0, y):
        print(f'y축 위 (y={y})')
    case (x, 0):
        print(f'x축 위 (x={x})')
    case (x, y): # x, y = (-4, 10)
        print(f'좌표: ({x}, {y})')

        
print("\n🟦 조건부 매칭 (가드, guard)")
# if 조건을 case 와 함께 쓸 수 있습니다.

number = 15

match number:
    case n if n % 2 == 0:
        print(n, "짝수")
    case n if n % 2 == 1:
        print(n, "홀수")
        

print("\n🟦 딕셔너리 매칭")
# 딕셔너리에서도 특정 키와 값을 매칭할 수 있습니다.

user = {"id": 1, "name": "Alice"}

match user: 
    case {"id": 1, "name": name}:
        print(f'id 1:{name} 유저 발견!')
    case {"id": user_id, "name": _}:
        print(f'id= {user_id} 인 다른 유저')
