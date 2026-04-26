# *******************************
# 문장에서 각 단어 첫글자만 대문자 만들기
# 

data = [
    "  i am a   PROGRAMMER",     # -> I Am A Programmer
    "  THAT ELEPHANT IS BIG  ",  # -> That Elephant Is Big
]

def letterCapitalize(sentence):
    
    #       str.capitalize 함수 쓰지 마세요

#     # 방법 1
#     result = []

#     for word in sentence.strip().lower().split():
#         result.append(word[0].upper() + word[1:])

#     return " ".join(result)


    # 방법 2 map 사용
    # return " ".join(map(lambda w: w[0].upper() + w[1:].lower(), sentence.split()))

    # 방법 3 reduce 사용
    from functools import reduce
    return " ".join(reduce(
        lambda prev, w: prev.append(w[0].upper() + w[1:].lower()) or prev,
        sentence.split(),
        [],
    ))

print(list(map(letterCapitalize, data)))

# ↓ 결과 ['I Am A Programmer', 'That Elephant Is Big']