# 리스트1 - 연습문제 3
# https://jungol.co.kr/problem/9356?cursor=MTYsOCw2


list = list(range(1,6))

print(f"last: {list[-1]}")
del(list[-1])
print(list)
print("len:", len(list))

print(f"\nsecond: {list[1]}")
del(list[1])
print(list)
print("len:", len(list))