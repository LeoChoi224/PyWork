# 리스트2 - 연습문제 2
# https://jungol.co.kr/problem/9406?cursor=MTYsMTAsMg==


result = {}
list = []
while True:
    n = int(input())    
    if n < 1 or n > 10: break
    list.append(n)

for i in sorted(list):
    result[i] = list.count(i)

for k, v in result.items():
    print(f"{k}: {v}")