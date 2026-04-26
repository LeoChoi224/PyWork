# 함수2 - 연습문제 5
# https://jungol.co.kr/problem/9479?cursor=MTYsMTMsOA==


def func(*agrs):
    for i in range(len(agrs)):
        print(" ".join(agrs[0:i+1]))

func("apple", 'banana', "coconut")