# 리스트2 - 자가진단 2
# https://jungol.co.kr/problem/9407?cursor=MTYsMTAsMw==



result = {}

list_a = list(map(int, input().split()))
list_b = [i % 10 for i in list_a]

for i in sorted(set(list_b)):
    print(f"{i} : {list_b.count(i)}")