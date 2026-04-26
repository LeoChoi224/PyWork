# 리스트2 - 자가진단 1
# https://jungol.co.kr/problem/9405?cursor=MTYsMTAsMQ==



list_a = list(map(int, input().split()))
print(list_a)

for i in range(len(list_a)):
    print(list_a[i], end=' ')


print("\nhap =", sum(list_a))
