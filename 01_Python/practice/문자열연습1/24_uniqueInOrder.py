# *******************************
# 연속 중복되지 않는 글자 출력
# 
    
data = [
    "all good tree",    # ['a', 'l', ' ', 'g', 'o', 'd', ' ', 't', 'r', 'e']
    "AAA AAAA AA AAA",  # ['A', ' ', 'A' ,' ', 'A', ' ', 'A']
    "i AM a BOY",       # ['i', ' ', 'A', 'M',' ', 'a', ' ', 'B', 'O', 'Y']    
]

def uniqueInOrder(sentence):

    result = []

    i = 0
    result.append(sentence[0])

    for j in range(1, len(sentence)):
        if sentence[i] != sentence[j]:
            result.append(sentence[j])
        
        i += 1

    return result
    
for s in data:
    print(uniqueInOrder(s))

# ↓ 결과 
# ['a', 'l', ' ', 'g', 'o', 'd', ' ', 't', 'r', 'e']
# ['A', ' ', 'A' ,' ', 'A', ' ', 'A']
# ['i', ' ', 'A', 'M',' ', 'a', ' ', 'B', 'O', 'Y']   