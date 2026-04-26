# *******************************
# 연속 중복되지 않는 글자 출력
# 
from functools import reduce

data = [
    "all good tree",    # ['a', 'l', ' ', 'g', 'o', 'd', ' ', 't', 'r', 'e']
    "AAA AAAA AA AAA",  # ['A', ' ', 'A' ,' ', 'A', ' ', 'A']
    "i AM a BOY",       # ['i', ' ', 'A', 'M',' ', 'a', ' ', 'B', 'O', 'Y']    
]

def uniqueInOrder(sentence):

    return reduce( 
        lambda list, ch: list if list and list[-1] == ch else (list.append(ch) or list),
        # 리스트(초기값)에 값이 없으면 False(이유: 초기값은 빈 리스트여서 인덱스 오류 방지)
        # 있으면 and(SCE)로 마지막 값과 ch 값 비교 -> 서로 다르다면 or로 추가
        sentence, # 문자열
        []
    )
    
for s in data:
    print(uniqueInOrder(s))

# ↓ 결과 
# ['a', 'l', ' ', 'g', 'o', 'd', ' ', 't', 'r', 'e']
# ['A', ' ', 'A' ,' ', 'A', ' ', 'A']
# ['i', ' ', 'A', 'M',' ', 'a', ' ', 'B', 'O', 'Y']   