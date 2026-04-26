# 반복제어문2 - 자가진단 6-2
# https://jungol.co.kr/problem/9306?cursor=MTYsNiwxNw==

n = int(input())

i = 0
sum = 0

while i < n: # n번 순환에 유용.
    num = int(input())
    sum += num
    i += 1

print('sum:', sum)
print('avg:', sum / n)