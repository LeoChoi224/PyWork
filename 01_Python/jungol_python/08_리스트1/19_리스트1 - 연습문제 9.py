# 리스트1 - 연습문제 9
# https://jungol.co.kr/problem/9367?cursor=MTYsOCwxOQ==

# TODO 선택정렬 이해하기
list_a = [5, 3, 2, 1, 4]

for i in range(len(list_a) - 1):
    min_idx = i
    for j in range(i + 1, len(list_a)):
        if list_a[j] < list_a[min_idx]:
            min_idx = j

    while min_idx > i:
        list_a[min_idx], list_a[min_idx - 1] = list_a[min_idx - 1], list_a[min_idx]
        min_idx -= 1

    print(list_a)