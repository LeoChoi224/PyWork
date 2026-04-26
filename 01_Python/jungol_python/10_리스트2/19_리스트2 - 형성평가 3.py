# 리스트2 - 형성평가 3
# https://jungol.co.kr/problem/9422?cursor=MTYsMTAsMTk=


list = list(map(int, input().split()))
dict = {}

for i in range(len(list)):
    list[i] = (list[i] // 10) * 10

for n in sorted(list, reverse=True):
    dict[n] = list.count(n)

for k, v in dict.items():
    print(f"{k}: {v} person")