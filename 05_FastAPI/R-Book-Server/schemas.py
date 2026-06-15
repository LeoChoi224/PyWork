# Pydantic 모델을 통해 서버가 받을 데이터, 서버가 응답할 데이터
#  생성및 검증

from pydantic import BaseModel, field_serializer
from typing import Optional
from datetime import datetime

"""Pydantic 모델(스키마) 정의"""
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_serializer


class BookCreate(BaseModel):
    """도서 작성 시 전달되는 모델 (POST /board)"""
    title: str = Field(..., max_length=50)
    author: str = Field(..., max_length=40)


class BookUpdate(BaseModel):
    """도서 수정 시 전달되는 모델 (PUT /board)"""
    id: int
    title: str = Field(..., max_length=50)
    author: str = Field(..., max_length=40)


class BookResponse(BaseModel):
    """도서 응답 모델 (목록/상세 조회 시 출력)"""
    # from_attributes=True : ORM 객체(Book) 를 그대로 직렬화할 수 있게 함
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    author: str
    created_at: datetime

        # JSON 응답시 regdate 필드를 직렬화
    @field_serializer('created_at')
    def serialize_datetime(self, dt: datetime, _info):
        # 원하는 포맷 "YYYY-MM-DD HH:mm:ss" 형태
        return dt.strftime("%Y-%m-%d %H:%M:%S")