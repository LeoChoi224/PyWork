# *******************************
# 가장 긴 단어 찾기
# 

data = [
    "   I am a Student",        # ->  Student
    "That elephant is big  ",  # -> elephant
]

def longestWord(sentence):
    
    max = " "

    for word in sentence.strip().split():
        max = word if len(word) > len(max) else max

    return max


print(list(map(longestWord, data)))

# ↓ 결과 ['Student', 'elephant']