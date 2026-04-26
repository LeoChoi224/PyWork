# 주석문과 디버깅 - 연습문제 2
# https://jungol.co.kr/problem/9250?cursor=MTYsNCwz


name1, age1 = input().split()
name2, age2 = input().split()

if int(age1) > int(age2):
    print(name1)
else:
    print(name2)
    