# 리스트2 - 연습문제 5
# https://jungol.co.kr/problem/9411?cursor=MTYsMTAsOA==


list_a = []
list_b = []

for i in range(2):
    list_a = list(map(int, input().split()))
    list_b = list_b + [list_a]

print(list_b)
print(list_b[0])
print(list_b[1])
for i in list_b[0]:
    print(i, end=' ')
print()
for i in list_b[1]:
    print(i, end=' ')