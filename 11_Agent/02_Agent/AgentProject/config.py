import os

from dotenv import load_dotenv

# .env 를 읽어 환경변수로 올린다.
# 아래 클래스 본문의 os.getenv() 는 import 시점에 한 번만 평가되므로,
# 반드시 class Config 정의보다 먼저 호출되어야 한다.
load_dotenv()


class Config:
    """프로젝트 설정 관리 클래스"""

    # 환경변수 설정
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', "")

    # 모델 파라미터
    MODEL_NAME: str = 'gpt-4o'
    MAX_TOKENS: int = 150

    # LLM 요약작업 호출시 병렬 호출을 위해 
    # 동시에 호출할 batch 크기
    BATCH_SIZE: int = 10

    # 뉴스를 분류할 카테고리 목록 정의 
    NEWS_CATEGORIES: list[str] = [
        "정치",
        "경제",
        "사회",
        "문화/연예",
        "IT/과학",
        "스포츠",
        "국제",
        "생활/건강",
        "기타",  # <- 위 카테고리로 분류되지 않은 뉴스들은 '기타' 로 처리
    ]

    NEWS_PER_CATEGORY: int = 30   # 카테고리별 표시할 뉴스 개수.

    # 프로젝트 루트 디렉토리 설정
    ROOT_DIR: str = os.path.dirname(os.path.abspath(__file__))

    # 출력파일들을 저장할 디렉토리 설정
    OUTPUT_DIR: str = f"{ROOT_DIR}/outputs"


    # 설정의 유효성 검사 메소드
    @classmethod
    def validate(cls) -> bool:
        """설정 유효성 검사"""
        if not cls.OPENAI_API_KEY:
            print("💢OpenAI API 키가 설정되지 않았습니다.")
            print("  환경변수 OPENAI_API_KEY를 설정하거나 실행 시 입력하세요.")
            return False
        return True





