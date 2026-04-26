# *******************************
# 문자열 시프팅 차이값
# 

data = [
#   [first, second]
    ["hello", "hello"],    # 0
    ["hello", "ohell"],    # 1
    ["hello", "lohel"],    # 2
    ["hello", "llohe"],    # 3
    ["hello", "elloh"],    # 4
    ["hello", "elohl"],    # -1
]

def shiftedDiff(words):
    first = words[0]
    second = words[1]
        
    # TODO : 작성하세요 (for if while 제어문 최대한 억제)
    
    return
    
print(list(map(shiftedDiff, data)))

# ↓ 결과 [0, 1, 2, 3, 4, -1]    