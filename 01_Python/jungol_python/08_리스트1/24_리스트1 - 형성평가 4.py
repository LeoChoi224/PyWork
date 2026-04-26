# 리스트1 - 형성평가 4
# https://jungol.co.kr/problem/9372?cursor=MTYsOCwyNA==


# max = 0
# min = 0

# while True:
#     num = int(input())
#     if num == 0: break
#     (min := num) if min > num else max < num and (max := num )

# print('MAX:', max)
# print('MIN:', min)



data = []

while True:
    n = int(input())
    data.append(n)
    if n == 0: break # 종료조건

max = data[0] # 첫번째 원소를 최댓값 설정
min = data[0] # 첫번째 원소를 최소값 설정
i = 1 # 두번째 원소부터 비교 시작

while i < len(data):
    if max < data[i]: # i번째 원소가 더 크다면
        max = data[i] # 최댓값 갱신
    
    if min > data[i]: # i번째 원소가 더 작다면
        min = data[i] # 최소값 갱신
    
    i += 1

print(f'MAX: {max}')
print(f'MIN: {min}')