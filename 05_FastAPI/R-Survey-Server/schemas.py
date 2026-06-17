"""Pydantic 모델(스키마) 정의"""
from pydantic import BaseModel, ConfigDict, Field, field_serializer
from datetime import datetime

class SurveyCreate(BaseModel):
    """설문 작성 시 전달되는 모델 (POST)"""
    name: str = Field(..., max_length=20)
    age: int = Field(..., gt=0)
    gender: str = Field("MALE")
    area: str = Field(...)
    favorite: str = Field(..., max_length=100)

class SurveyUpdate(BaseModel):
    """설문 수정 시 전달되는 모델 (PUT)"""
    id: int
    gender: str = Field("MALE")
    area: str = Field(...)
    favorite: str = Field(..., max_length=100)

class SurveyResponse(BaseModel):
    """설문 응답 모델 (목록/상세 조회 시 출력)"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    age: int
    gender: str
    area: str
    favorite: str
    created_at: datetime

    # JSON 응답시 regdate 필드를 직렬화
    @field_serializer('created_at')
    def serialize_datetime(self, dt: datetime, _info):
    # 원하는 포맷 "YYYY-MM-DD HH:mm:ss" 형태
        return dt.strftime("%Y-%m-%d %H:%M:%S")