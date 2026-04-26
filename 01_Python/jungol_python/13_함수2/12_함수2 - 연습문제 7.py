# 함수2 - 연습문제 7
# https://jungol.co.kr/problem/9483?cursor=MTYsMTMsMTI=


# TODO 알고리즘 확인
def func(a, b, c):
    for i in range(a + 1):
        for j in range(b + 1):
            if (i * 2) + (j * 3) == c:
                return "YES"
    
    return "NO"

t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    print(func(a, b, c))