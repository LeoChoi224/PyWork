# Book 도메인 정의

from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional

class Book(BaseModel):
    id: Optional[int] = None
    title: str = Field(...)
    author: str = Field(...)
    price: int # 필수
    stock: int = 0
    published_year: int
    regDate: datetime = datetime.now()


    # 'title' 에 대한 validator
    @field_validator("title")
    def title_must_be_positive(cls, v):
        if not v:
            raise ValueError("ERR-2문자열오류 insert()제목이 입력되지 않았습니다. :")
        return v
    
    # 'author' 에 대한 validator
    @field_validator("author")
    def author_must_be_positive(cls, v):
        if not v:
            raise ValueError("ERR-2문자열오류 insert() 작가가 입력되지 않았습니다. :")
        return v

    # 'price' 에 대한 validator
    @field_validator("price")
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("ERR-4]가격 오류 insert() 가격에 정상적인 입력이 되지 않았습니다. :")
        return v
    
    # 'stock' 에 대한 validator
    @field_validator("stock")
    def stock_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("ERR-5 수량 오류 insert() 수량은 0 이상이어야 합니다. :")
        return v

    # 'published_year' 에 대한 validator
    @field_validator("published_year")
    def published_year_must_be_positive(cls, v):
        if v < 2026 and v > 1899:
            raise ValueError("ERR-5 연도 오류 insert() 연도는 1900년 ~ 2026년 사이입니다. :")
        return v