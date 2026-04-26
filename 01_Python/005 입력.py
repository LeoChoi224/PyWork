# 🟦 파이썬 기본입력 함수 input()
# 기본적으로 input() 함수는 키보드로 부터 입력받아
# 문자열(str) 으로 리턴합니다

# a = input()

# print('입력하신 값은', a)
# print(int(a) + 100)


# num1 = int(input())
# num2 = int(input())
# print(f"{num1} + {num2} = {num1 + num2}")
# print(f"{num1} - {num2} = {num1 - num2}")
# print(f"{num1} * {num2} = {num1 * num2}")
# print(f"{num1} / {num2} = {num1 / num2}")

# 변수명 변경시 rename 기능 (커스텀 단축키 Shift + F6) 사용!

#------------------------------------
# prompt 를 사용한 input 입력

# height = float(input("키를 입력하세요 cm : "))
# print(f"입력한 키는 {height / 100:.1f}m")

# 연습: 단위변환
# 1야드(yd)는 91.44cm이고 1인치(in)는 2.54cm이다.
# 처음에는 야드를 입력받고, 두번째는 인치를 입력받아 
# 각각 cm로 변환하여 다음 형식에 맞추어 소수 둘째자리까지 출력하시오.​

# [실행예]
# yard 입력: 23.45
# inch 입력: 41.273
# 23.45 yard 는 2144.27cm
# 41.27 inch 는 104.83cm


yard = float(input("yard 입력: "))
inch = float(input("inch 입력: "))
print(f"{yard:.2f} yard 는 {yard * 91.44:.2f}cm")
print(f"{inch:.2f} inch 는 {inch * 2.54:.2f}cm")

# input() 은 한번에 여러개 입력 못받는다.
# a, b, c = input("3개 입력하세요")

# 여러개 입력받기
# 방법1: input().split() - 

a, b, c = input("3개 입력하세요").split()
print(f"a={a}, b={b}, c={c}")
