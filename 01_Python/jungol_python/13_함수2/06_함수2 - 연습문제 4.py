# 함수2 - 연습문제 4
# https://jungol.co.kr/problem/9477?cursor=MTYsMTMsNg==

import math

list_a = [ 3.1, 6.2, 7.8, 1.4]
for i in range(len(list_a)):
    list_a[i] = math.floor(list_a[i])

print(list_a)