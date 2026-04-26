print('\n🟦 대표적인 정규표현식')
#  ^   문자열 시작
#  $   문자열 종료
#  .   임의의 문자한개에 매칭
#  *   앞 문자 0개 이상에 매칭
#  +   앞 문자 1개 이상에 매칭
#  ?   앞 문자가 없거나 한개에 매칭
#  []  문자의 집합이나 범위를 표현합니다. -기호를 통해 범위를 나타낼 수 있습니다. ^가 존재하면 not을 나타냅니다.
#  {}  횟수 또는 범위를 나타냅니다.
#  ()  괄호안의 문자를 하나의 문자로 인식합니다. (그룹)
#  |  패턴을 OR 연산을 수행할 때 사용합니다.
#  \s  공백 문자
#  \S  공백 문자가 아닌 나머지 문자
#  \w  알파벳이나 숫자
#  \W  알파벳이나 숫자를 제외한 문자
#  \d  [0-9] 숫자
#  \D  숫자를 제외한 모든 문자
#  (?i)  대소문자를 구분하지 않습니다

import re

# 테스트 도우미 함수
def regexp_test(regex, input_list):
    
    for s in input_list:    
        print("[정규표현식 매칭 테스트]-----------------")
        print("정규표현식: " + regex)
        print("입력문자열: " + s)

        match_count = 0
        for match in re.finditer(regex, s):
            match_count += 1
            print(f'   ✅매치{match_count}: {match.group()} {match.span()}')

            # 패턴에 그룹이 있었다면 그룹별로 출력
            group_size = len(match.groups())
            for i in range(1, group_size + 1):
                print(f'\t    group{i}: {match.group(i)} ({match.start(i)} - {match.end(i)})')

        match_count == 0 and print("    🤯매치 없슴🤯")
        print()

# ------------------------------
title = "^ : 바로 문자뒤의 문자열로 시작됨"
regex = r"^The"  # The 로 시작하는 패턴 # 무조건 해당 단어로 시작인 경우 매칭
input_list = [
    "The Things",   # ok
    "On The Things",# x
    " The The The",  # x
    "The The The",  # ok
]

title = "$ : 문자열의 마지막이 이 문자열로 마무리 됨"
regex = r"Man$"  # Man 으로 끝나는 패턴 # 무조건 해당 단어로 끝인 경우 매칭
input_list = [
    "SuperMan",   # ok
    "AquaMan",    # ok
    "WonderWoman", # x
    "WonderWoMan", # OK
    "PostMan ",  # x
]

title = "^표현식$ : 정확하게 전체패턴매칭되는 문자열"
regex = r'^SuperMan$' # 무조건 해당 단어인 경우 매칭
input_list = [
    "SuperMan",  # OK
    "Super Man",  # x
    " SuperMan",  # x
    "SuperMan "   # x
]

title = " . : 어떤 문자든지 임의의 '한문자'에 매칭"
regex = r"x.z" # x 와 z 사이의 한문자 만 오는 경우 매칭
input_list = [
    "xyz",   # xyz
    "xxzdfdk",  # xxz
    "aa10x9zbxbz", #x9z, xbz
    "xz",  # 💥
    "90x zxx_zdf", # "x z", "x_z"
    "xbz",  # xbz
    "xyyz"  # 💥
]

title = " * : 바로 앞의 문자가 없거나 한개 이상에 매칭"
regex = r"ab*" # a가 무조건 있고 b가 있거나 없을 경우 b가 끝날떄까지 매칭
regex = r"ab*"
input_list = [
    "a",  # "a"
    "abc", # "ab"
    "ab", # "ab"
    "abbbaaaabababbab", # 8개
    "bbba",  # a
    "cdef"  # 💥  
]

title = " + : 바로 앞의 문자가 한개 혹은 그 이상을 매칭"
regex = r"ab+" # ab가 둘 다 있을때 b가 끝날때까지
input_list = [
    "a",    # 💥
    "abc",  # ab
    "ab",   # ab
    "abbbaaaabababbab",  # 5개
    "bbba", # 💥
    "cdef"   # 💥
]

title = " ? : 바로 앞의 문자가 한개 있거나 없는것을 매칭"
regex = r"ab?" # 
input_list = [
    "a",   # a
    "abc",  # ab
    "kkabcc", # ab
    "abbbaaaabababbab",  # 8개 
    "bbba"  # a
]

title = " [] : 안에 존재하는 문자들중 한 문자만을 매칭"
regex = r"[abc]" # a 또는 b 또는 c 중에 한 문자에 매칭
input_list = [
    "able",   # a, b
    "bible",  # b, b
    "cable",  # c, a, b
    "xenosys",  # 💥
]
regex = r"[abc]+" # a 또는 b 또는 c 중에 한 문자 이상 있다면 해당문자가 포함되는 경우 매칭
regex = r"[a-z]" # a 부터 z 까지 (1개 이상)
regex = r"[a-z]+"  # a 부터 z까지 (1개 이상)
input_list = [
    "abc100",    # 
    "abcDefGHIUJ-KLM123opQrstuz"   # 
]
regex = r"[a-zA-Z]+"
regex = r"[a-zA-Z0-9]+"
regex = r"[a-zA-Z0-9-]+" # - hyphen 도 매칭
regex = r"[0-9]+"
regex = r"[^0-9]+" # ^  not

title = " {} : 앞에 있는 문자나 문자열의 등장개수를 정함"
regex = r"ab{2}" # a로 시작하고 b가 x2번 등장하는 패턴
input_list = [
    "abb",  # abb
    "abbb", # abb
    "abbbabbbbbbbbabaabab", # 2개
]

regex = r"ab{2,}" # b가 2개 이상의 패턴에 매칭
regex = r"ab{3,5}"  # b가 3개에서 5개까지 매칭

title = " () : ()안에 있는 글자들을 그룹화 "
regex = r"a(b,c)*" # (bc) 가 없거나 한개 이상 매칭, 그룹 전체가 한 묶음
input_list = [
    "abc",  # abc
    "abcbcbbac",  # "abcbc", "a"
    "abcabcabc",  # 3개
]

title = " | : OR 연산자  역할"
regex = r"a|b"   # a 또는 b 둘중 하나
input_list = [
    "a",
    "b",
    "ab",
    "xyz"
]

regex = r"(a|b)+"

title = "(?i)  : 대소문자 구분안하고 매칭 ";  # Python ONLY
regex = r"(?i)abc"
input_list = [
    "abc",
    "Abc",
    "ABC",
]

title = r"\s : 공백,  \S : 공백아닌 문자"
regex = r'\s+'
input_list = [
    "Hello My World",   # 2
    "He \tllo My World",  # 3
    "\n\t Hello My World\n\n",  # 4
]

regex = r'\S+'
title = r"\w : 알파벳이나 숫자, \W 알파벳이나 숫자를 제외한 문자"
regex = r'\w+'
input_list = [
    "This is 2022-09-23 !!"
]

regex = r'\w+'

title = r"\d : [0-9] 숫자, \D 숫자를 제외한 모든 문자"
regex = r'\d+'
regex = r'\D+'

title = "excaped character 매칭 시키기"
regex = r'.+'  # 전체 문자가 매칭...
regex = r'[.]+'
regex = r'\.+'
input_list = [
    "My name is .."
]

# Tip: # 으로 시작하는 주석만 제거
# 찾기  ^\s*#.*\n?
# 바꾸기 (빈칸)

# 코드 뒤에 달린 주석 제거
# 찾기 \s+#.*
# 바꾸기 (빈칸)



print(title)
regexp_test(regex, input_list)


print('\n' * 15)