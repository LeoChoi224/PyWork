# 리스트1 - 형성평가 5
# https://jungol.co.kr/problem/9373?cursor=MTYsOCwyNQ==


data = []

while True:
    num = int(input())
    if num == 0: break
    data.append(num)

i = 0
sum = 0
result =[]
while i < len(data):
    if data[i] % 5 == 0:
        result.append(data[i])
        sum += data[i]
    i += 1

# i = 0
# result =[]
# while i < len(data):
#     data[i] % 5 == 0 and result.append(data[i])
#     i += 1

# i = 0
# sum = 0
# while i < len(result):
#     sum += result[i]
#     i += 1

# i = 0
# sum = 0
# result =[]
# while i < len(data):
#     result.append(data[i]) and (sum := sum + data[i]) if data[i] % 5 == 0 else 0
#     i += 1

# i = 0
# sum = 0
# while i < len(data):
#     data[i] % 5 != 0 and del(data[i])
    
#     i += 1

print(result)
print("CNT:", len(result))
print("HAP:", sum)
print("AVG:", sum / len(result))