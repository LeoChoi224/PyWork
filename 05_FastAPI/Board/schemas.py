# Pydantic 모델을 통해 서버가 받을 데이터, 서버가 응답할 데이터
#  생성및 검증

from pydantic import BaseModel, field_serializer
from typing import Optional
from datetime import datetime

# 게시글 작성
class PostCreate(BaseModel):
    user: str
    subject: str
    content: Optional[str] = None
    

# 게시글 응답 모델
class PostResponse(BaseModel):
    id: int
    user: str
    subject: str
    content: Optional[str]
    viewcnt: int
    regdate: datetime 

    # JSON 응답시 regdate 필드를 직렬화
    @field_serializer('regdate')
    def serialize_datetime(self, dt: datetime, _info):
        # 원하는 포맷 "YYYY-MM-DD HH:mm:ss" 형태
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    # 기본적으로 Pydantic 은 dict 으로 모델을 만든다
    # 그러나! dict 가 아닌 객체의 속성(attribute)에서 데이터를 읽어오게 하는 설정
    class Config:
        from_attribute = True


# 게시글 수정
#  압력: id, subject, content
class PostUpdate(BaseModel):
    id: int
    subject: str
    content: Optional[str] = None