# 리스트2 - 연습문제 8
# https://jungol.co.kr/problem/9418?cursor=MTYsMTAsMTU=


list =[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    ]

for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j], end=' ')
    print()