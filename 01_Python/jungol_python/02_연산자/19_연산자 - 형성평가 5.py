# 연산자 - 형성평가 5
# https://jungol.co.kr/problem/9221?cursor=MTYsMiwxOQ==


minjea_age, minjea_height = map(int, input().split())
minyoung_age, minyoung_height = map(int, input().split())

print(minyoung_age > minjea_age and minyoung_height > minjea_height)