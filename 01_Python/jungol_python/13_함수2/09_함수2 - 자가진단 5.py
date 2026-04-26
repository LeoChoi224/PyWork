# 함수2 - 자가진단 5
# https://jungol.co.kr/problem/9480?cursor=MTYsMTMsOQ==


# 이 부분에 함수를 작성하시오.
def solve(*agrs):
    return sum(filter(lambda x: x % 2 != 0,agrs))

a, b = map(int, input().split())
print(solve(a, b))

a, b, c, d = map(int, input().split())
print(solve(a, b, c, d))