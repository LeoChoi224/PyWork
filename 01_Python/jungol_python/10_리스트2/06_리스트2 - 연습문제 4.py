# 리스트2 - 연습문제 4
# https://jungol.co.kr/problem/9408?cursor=MTYsMTAsNg==


list_a = ["Rose", "SunFlower", "Tulip", "Carnation"]
list_b = []

for flower in list_a:
    if len(flower) <= 5: list_b.append(flower)

print(list_b)