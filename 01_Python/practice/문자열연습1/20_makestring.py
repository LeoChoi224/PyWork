# *******************************
# 단어의 앞글자로만 만들어진 문자열 생성``
# 

data = [
    "   The community at Code States might be the biggest asset", # -> TcaCSmbtba
    "i am a  PROGRAMMER   ",     # -> iaaP
    "   THAT   ELEPHANT IS BIG ",  # -> TEIB
]

def makeString(sentence):
    
    result = ""

    for word in sentence.strip().split():
        result += word[0]
    return result
    
print(list(map(makeString, data)))

# ↓ 결과 ['TcaCSmbtba', 'iaaP', 'TEIB']