# 주석문과 디버깅 - 형성평가 2
# https://jungol.co.kr/problem/9253?cursor=MTYsNCw2


a, b = input().split()
a, b = int(a), int(b)
if a > b:
    c = a - b 
else:
    c = b - a 
print(c)    # 3 5가 입력되었을 때 출력은 2가 나와야 한다.