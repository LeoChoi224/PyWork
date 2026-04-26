# 반복제어문1 - 자가진단 7-2
# https://jungol.co.kr/problem/9281?cursor=MTYsNSwyNQ==

sum = 0
while True:
    num = int(input())
    if num == 0: break
    elif num > 0:
        sum += num
    else:
        continue
print(sum)