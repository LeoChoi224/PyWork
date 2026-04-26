# 리스트2 - 형성평가 2
# https://jungol.co.kr/problem/9421?cursor=MTYsMTAsMTg=


count = [0] * 6

for _ in range(6):
    n = int(input())
    count[n - 1] += 1

for i in range(6):
    print(f"{i + 1}: {count[i]}")