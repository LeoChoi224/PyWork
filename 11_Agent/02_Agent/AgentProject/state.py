from typing import Annotated, Any
from pydantic import BaseModel, ConfigDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class NewsState(BaseModel):
    """뉴스 처리 상태를 관리하는 모델"""

    # Pydantic 이 모르는 타입을 허용
    #   Pydantic에서 허용하는 타입(str, int, dict, datetime 등) 이외의 타입을 필드로 선언하면 에러가 납니다. 
    #   NewsState에서는 BaseMessage 타입을 사용하는데 해당 타입은 Pydantic이 모르는 타입입니다. 
    #   그러므로 arbitrary_types_allowed=True 설정을 추가하여 Pydantic이 모르는 타입을 허용해야 합니다.
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # '대화의 이력' 저장.
    messages: Annotated[list[BaseMessage], add_messages] = []

    # raw_news 필드에는 
    #    RSS 피드에서 수집한 원시 뉴스 데이터(들)을 list[dict] 형태로 저장. 
    #    각 뉴스는 dict 형태로 저장됩니다 {제목:..., 링크:..., 설명:..., 등..}. 
    #    초깃값은 빈 리스트입니다.
    raw_news: list[dict[str, Any]] = []

    # summarized_news 필드에는 
    #   AI가 요약한 뉴스 데이터를 저장합니다. 
    #   원시 뉴스 에 '요약 정보'가 '추가'된 형태입니다. 
    #   요약 과정을 거친 후의 데이터를 보관합니다.
    summarized_news: list[dict[str, Any]] = []

    # categorized_news 에는 카테고리별로 분류된 뉴스를 저장합니다. 
    #   자료형이 조금 복잡합니다만, 
    #   카테고리별로 뉴스 데이터가 리스트[딕셔너리] 형태로 들어 있다고 보면 되겠습니다.
    categorized_news: dict[str, list[dict[str, Any]]] = {}

    # final_report에는 최종 생성된 리포트를 문자열로 저장합니다. 
    #   마크다운 형식의 리포트로 저장할 예정입니다.
    final_report: str = ""

    # error_log는 이름에서 유추할 수 있듯, 워크플로 실행 중 발생하는 에러를 기록합니다. 
    # error_log는 리듀서 패턴을 사용하지 않고 직접 append() 함수로 추가합니다.
    error_log: list[str] = []    