# 리스트2 - 자가진단 4
# https://jungol.co.kr/problem/9410?cursor=MTYsMTAsNw==



list_a = list(map(int, input().split()))
list_b = []

for n in list_a:
    if n % 5 == 0 or n % 3 == 0: list_b.append(n)
    
print(list_b)
print("합계:", sum(list_b))