# 리스트2 - 자가진단 5-1
# https://jungol.co.kr/problem/9412?cursor=MTYsMTAsOQ==


list_b = []

for i in range(0, 20, 5):
    list_a = []
    for j in range(1, 6):
        list_a.append(j + i)
    list_b.append(list_a)
        
for i in range(len(list_b)):
    for j in list_b[i]:
        print(f"{j:>2}", end='   ')
    print()