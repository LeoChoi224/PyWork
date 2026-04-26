import re

string = '정가 14,500원'

# 도전
# 정규표현식 사용하여 int 값 14500 을 추출하기
# hint: sub() 사용

print(int(re.sub(r'\D', '', string)))
print(int(re.sub(r'[^0-9]', '', string)))

# print(int(''.join(re.findall(r'\d', string))))


print('\n🟦 실습] 쿠폰 검증')
"""
 정규표현식 연습

 이번에 우리 쇼핑몰에서 할인 쿠폰을 발행하려 한다.
 발행되는 쿠폰의 일련번호 형식은 다음과 같다.

    알파벳두자리-숫자4자리-숫자3자리-알파벳3자리

 알파벳은 대소문자 구문 없슴
 숫자는 0으로 시작하면 안됨.
 사용자는 발급받은 쿠폰번호를 입력해야 하는데,
 위와 같은 형식만 받아들일수 있도록 만들자

 허용예]
 	Ab-7890-786-zuy
 	ki-2010-893-Zip

 불가]
 	xX-1200-089-zuy
 	p9-324-389-zopl

 쿠폰번호를 계속해서 입력 받으면서
 "유효한 쿠폰입니다"  혹은 "유효한 쿠폰이 아닙니다" 판정결과를 출력

 'quit' 입력하면 프로그램 종료
"""

import re
valid, invalid = "유효한 쿠폰입니다.", "유효한 쿠폰이 아닙니다."
# regex = r'([a-zA-Z]..)[-]([1-9].[0-9]...)[-]([1-9].[0-9]..)[-]([a-zA-Z]..)'
regex = r'^[a-z]{2}[-][1-9]\d{3}[-][1-9]\d{2}[-][a-z]{3}$'
while True:    
    coupon = input().lower()
    if coupon == 'quit': break
    # TODO 이진수
   #  pat = re.compile(regex)
   #  match = pat.match(coupon)
    print(re.match(regex, coupon))



# import re
# valid, invalid = "유효한 쿠폰입니다.", "유효한 쿠폰이 아닙니다."
# regex = r'^[a-z]{2}[-][1-9]\d{3}[-][1-9]\d{2}[-][a-z]{3}$'
# while True:    
#     coupon = input().lower()
#     if coupon == 'quit': break
#     print(valid if re.match(regex, coupon) else invalid)
    