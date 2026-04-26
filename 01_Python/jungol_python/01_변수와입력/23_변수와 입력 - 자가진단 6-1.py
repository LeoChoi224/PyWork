# 변수와 입력 - 자가진단 6-1
# https://jungol.co.kr/problem/9193?cursor=MTYsMSwyMw==


name1, age1 = input().split()
name2, age2 = input().split()
print(f"{name1} was born in {age1}")
print(f"{name2} was born in {age2}")
print(f"{name1} is {int(age2) - int(age1)} years older than {name2}")