# *******************************
# 문장에서 각 단어 첫글자만 대문자 만들기
# 
from functools import reduce

data = [
    "  i am a   PROGRAMMER",     # -> I Am A Programmer
    "  THAT ELEPHANT IS BIG  ",  # -> That Elephant Is Big
]

def letterCapitalize(sentence):
    
    return " ".join(reduce(
        lambda prev, w: prev.append(w[0].upper() + w[1:].lower()) or prev,
        sentence.split(),
        [],
    ))

print(list(map(letterCapitalize, data)))

# ↓ 결과 ['I Am A Programmer', 'That Elephant Is Big']