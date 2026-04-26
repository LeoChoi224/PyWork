# 함수2 - 자가진단 7
# https://jungol.co.kr/problem/9484?cursor=MTYsMTMsMTM=


def func(nums):

    for i in range(len(nums)):
        if max(list_a) == nums[i]:
            print(i, end=' ')

list_a = list(map(int, input().split()))
func(list_a)