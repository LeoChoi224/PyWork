# *******************************
# 가장 긴 단어 찾기
# 
from functools import reduce

data = [
    "   I am a Student",        # ->  Student
    "That elephant is big  ",  # -> elephant
]

def longestWord(sentence):

    return reduce(
        lambda a, b: a if len(a) > len(b) else b, # 단어 1번째와 2번째를 비교해서 반환
        sentence.strip().split(), # 문자열에서 단어를 받아옴, strip()은 필요 없어도 항상 사용하는 습관!
        )

print(list(map(longestWord, data)))

# ↓ 결과 ['Student', 'elephant']