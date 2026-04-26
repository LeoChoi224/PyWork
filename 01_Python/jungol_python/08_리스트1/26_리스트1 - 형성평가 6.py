# 리스트1 - 형성평가 6
# https://jungol.co.kr/problem/9374?cursor=MTYsOCwyNg==


data = []

while True:
    num = int(input())
    if num == 0: break
    data.append(num)

i = 0
odd, even = [], []
while i < len(data):
    even.append(data[i]) if data[i] % 2 == 0 else odd.append(data[i])
    i += 1

print("odd =", odd)
print("even =", even)