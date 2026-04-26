# 반복제어문1 - 자가진단 7-3
# https://jungol.co.kr/problem/9282?cursor=MTYsNSwyNg==


cnt = 0
sum = 0
while True:
    num = int(input())
    if num == 0: break
    
    if 0 > num or 100 < num:
        continue

    sum += num
    cnt += 1

print('count =', cnt)
print('total =', sum)
print('avg =', int(sum / cnt))