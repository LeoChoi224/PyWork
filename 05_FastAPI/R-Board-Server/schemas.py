"""Pydantic 모델(스키마) 정의"""
from pydantic import BaseModel, ConfigDict, Field, field_serializer
from datetime import datetime
from typing import Optional


class PostCreate(BaseModel):
    """게시글 작성 시 전달되는 모델 (POST /board)"""
    user: str = Field(..., max_length=20)
    subject: str = Field(..., max_length=200)
    content: Optional[str] = Field(None)


class PostUpdate(BaseModel):
    """도게시글서 수정 시 전달되는 모델 (PUT /board)"""
    id: int
    user: str = Field(..., max_length=20)
    subject: str = Field(..., max_length=200)
    content: Optional[str] = Field(None)

class PostResponse(BaseModel):
    """게시글 응답 모델 (목록/상세 조회 시 출력)"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    user: str
    subject: str
    content: str
    viewcnt: int
    created_at: datetime

    # JSON 응답시 regdate 필드를 직렬화
    @field_serializer('created_at')
    def serialize_datetime(self, dt: datetime, _info):
    # 원하는 포맷 "YYYY-MM-DD HH:mm:ss" 형태
        return dt.strftime("%Y-%m-%d %H:%M:%S")