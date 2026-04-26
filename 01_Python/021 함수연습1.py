import math

# 반지름은 입력받아
# 원의 둘레를 계산하여 리턴하는 함수를 작성하세요
# 정의, 호출

def circle_circumference(radius):
    return radius * 2 * math.pi

# 반지름은 입력받아
# 원의 면적를 계산하여 리턴하는 함수를 작성하세요
# 정의, 호출 

def circle_area(radius):
    return (radius ** 2) * math.pi

# 직사각형의 '가로', '세로' 의 크기를 입력받아
# 직사각형의 넒이를 구하는 함수를 작성하세요
# 정의, 호출

def quadrangle_area(width, height):
    return width * height

# 직각삼각형의 '밑변'과 '높이'가 주어졌을때
# 빗변의 길이를 구하는 함수를 작성하세요
# 정의, 호출

def quadrangle_hypotenuse(bottom, height):
    return math.sqrt((bottom ** 2) + (height ** 2))

# 반지름은 입력받아
# 원의 '둘레'와 '면적'을 계산하여 리턴하는 함수를 작성하세요
# 정의, 호출 

def circle_circumference_arer(radius):
    return circle_circumference(radius), circle_area(radius)

print(quadrangle_area(3, 4))
print(quadrangle_hypotenuse(3, 4))
print(circle_circumference_arer(5))