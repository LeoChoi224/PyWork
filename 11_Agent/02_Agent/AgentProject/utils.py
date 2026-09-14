# 범용적으로 자주 쓰이는 함수, 변수, 클래스들 정의

# html 태그를 제거하는 clean_html() 함수, 
# 텍스트가 너무 긴 경우 잘라내는 truncate_text() 함수 
# RSS의 시간 표기를 정리하는 format_date() 함수를 만들어둡시다.

from datetime import datetime, timedelta
import re

def clean_html(html_text: str) -> str:
    """HTML 태그 제거"""
    if not html_text:
        return ""

    # ① 정규표현식으로 HTML 태그 제거: <태그명>내용</태그명> 패턴 매칭
    #    정규표현식 <?>는 HTML 태그를 찾아서 제거하는 패턴
    clean_text = re.sub("<.*?>", "", html_text)

    # 연속된 공백은 하나의 공백으로 정리
    clean_text = re.sub(r"\s+", " ", clean_text).strip()

    return clean_text


def truncate_text(text:str, max_length: int = 500) -> str:
    """텍스트를 적절한 길이로 자르기"""
    if not text or len(text) <= max_length:
        return text

    return text[:max_length] + "..."

# RSS 피드의 날짜는 보통 RFC-822 형식(예시: "Mon, 25 Dec 2023 10:30:00 GMT")으로 제공. ← 끝에 시간대 정보가 포함된다.
# 여기에 9시간 더해주면 한국시간 된다.
def convert_gmt_to_kst(gmt_time_str: str) -> str:
    """GMT 시간을 KST 로 변환한다."""
    KST_OFFSET_HOURS = 9
    gmt_time = datetime.strptime(gmt_time_str, "%a, %d %b %Y %H:%M:%S GMT")
    kst_time = gmt_time + timedelta(hours=KST_OFFSET_HOURS)
    return kst_time.strftime("%Y-%m-%d %H:%M:%S")

# 테스트
if __name__ == "__main__":
    print(clean_html("   <div> 희준이가 넘어간다...  눈이   감긴다... </div>   "))
    print(convert_gmt_to_kst("Mon, 25 Dec 2023 10:30:00 GMT")) # 2023-12-25 19:30:00
