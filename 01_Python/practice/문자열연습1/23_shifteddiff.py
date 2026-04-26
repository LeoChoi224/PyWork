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

    # return (first * 2).find(first)

    cnt = 0
    for i in second:
        if first == second:
            break;
        else:
            second = second[1:] + second[:1]
            cnt += 1

    return cnt if cnt < len(second) else -1
    
print(list(map(shiftedDiff, data)))

# ↓ 결과 [0, 1, 2, 3, 4, -1]    