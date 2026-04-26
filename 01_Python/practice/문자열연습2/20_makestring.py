# *******************************
# 단어의 앞글자로만 만들어진 문자열 생성
# 
from functools import reduce

data = [
    "   The community at Code States might be the biggest asset", # -> TcaCSmbtba
    "i am a  PROGRAMMER   ",     # -> iaaP
    "   THAT   ELEPHANT IS BIG ",  # -> TEIB
]

def makeString(sentence):
    
    return "".join(reduce( # 첫 글짜로 이루어진 리스트의 모든 요소를 ""와 같이 합쳐 문자열로
        lambda list, word: list.append(word[0]) or list, # 리스트에 단어 첫 글짜를 추가(SCE)
        sentence.strip().split(), # 문자열에서 단어를 받아옴
        [] # 초기값 리스트
    ))
    
print(list(map(makeString, data)))

# ↓ 결과 ['TcaCSmbtba', 'iaaP', 'TEIB']