# Inventory 도메인 정의

from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional

# SELECT 읽어올때도 사용
# INSERT 할때도 사용 <- name, price, stock
# UPDATE 할때 사용 <- name, price, stock, id
class Inventory(BaseModel):
    id: Optional[int] = None
    name: str = Field(...)
    price: int # 필수
    stock: int = 0
    regDate: datetime = datetime.now()

    # 'name' 에 대한 validator
    @field_validator("name")
    def name_must_be_positive(cls, v):
        if not v:
            raise ValueError("ERR-2문자열오류 insert() 이름이 입력되지 않았습니다. :")
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