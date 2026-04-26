# 함수2 - 연습문제 6
# https://jungol.co.kr/problem/9481?cursor=MTYsMTMsMTA=


def func(*agrs):
    nums = []
    for num in agrs:
        nums.append(num)
    print(nums)
    for i in nums:
        print(i, end=' ')

a, b, c, d, e, f, g, h, i, j = map(int, input().split())
func(a, b, c, d, e, f, g, h, i, j)