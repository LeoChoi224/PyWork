# 함수2 - 형성평가 1
# https://jungol.co.kr/problem/9485?cursor=MTYsMTMsMTQ=


def func(list_a):
    list_b = []

    for i in range(len(list_a)):
        if list_a[i] == max(list_a) or list_a[i] == min(list_a):
            list_b.append(list_a[i])

    for i in list_b:
        print(i)

    # return n

print(map(int, input().split()))