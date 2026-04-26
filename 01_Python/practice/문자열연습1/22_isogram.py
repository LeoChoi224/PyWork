# *******************************
# isogram : 중복글자 없는 단어
# isogram 여부 판단하기 (true/false)
# 

data = [
    "Dermatoglyphics", # -> True
    "programmer",      # -> False
    "Cocktail",        # -> False  대소문자 동일
    "isogram",         # -> True
]

def isIsogram(word):

    dict = {}

    for ch in word.lower():
        if ch.isalpha():
            dict[ch] = dict.get(ch, 0) + 1

    # return sum(dict.values()) == len(dict.values())

    for cnt in dict.values():
        if cnt > 1:
            word = "False"
            break
        else:
            word = "True"

    return word 

# def isIsogram(word):
#     word = word.lower()                     # word리스트 안에있는 문자열들을 전부 대소문자 통일
#     return len(word) == len(set(word)) 
    
print(list(map(isIsogram, data)))

# ↓ 결과 [True, False, False, True]