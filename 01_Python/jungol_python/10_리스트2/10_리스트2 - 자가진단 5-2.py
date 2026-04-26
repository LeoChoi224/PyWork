# 리스트2 - 자가진단 5-2
# https://jungol.co.kr/problem/9413?cursor=MTYsMTAsMTA=


list_b = []

ch = ord('A')
for i in range(3):
    list_a = []
    for j in range(3):
        ch = list_a.append(chr(ch)) or ch + 1
    list_b = list_b + [list_a]

for i in range(len(list_b)): print(list_b[i])
print(list_b)