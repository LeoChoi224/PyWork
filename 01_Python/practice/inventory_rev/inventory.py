# inventory 도메인 정의
# DB 와 주고 받을 파이썬 데이터 객체 정의.

# EX)
# 사용자 입출력 
# SELECT 읽어올때도 사용
# INSERT 할때도 사용 <- name, price, stock
# UPDATE 할때 사용 <- name, price, stock, id

from typing import Optional
from pyantic import BaseModel, field_validator, ValidationError
from datetime import datetime

class Inventory(BaseModel):
    id: Optional[int] = None
    name: str
    price: int
    stock: int
    reg_date: Optional[datetime] = None

    @field_validator("name")
    def name_must_not_be_empty(name):
        print(f'🏈 name_must_not_be_empty(name={name}) 호출')
        if not name.strip():
            raise ValueError("ERR-2]문자열오류 insert() 이름이 입력되지 않았습니다")
        return name # 실제 세팅될 값은 리턴해주어야 한다

    # mode= : 데이터 검증의 어느 시점에 내 로직을 끼워 넣을 것인가
    
    #   'after' : (기본값) Pydantic의 기본 내부 검증이 끝난 후 실행.
    #             데이터가 이미 해당 타입(int, str 등)으로 변환된 상태

    #   'before' : Pydantic의 기본 내부 검증이 시작되기 전 실행
    #              입력된 가공되지 않은(raw) 데이터를 직접 다룰 때 사용합니다.

    #   'plain' : Pydantic의 기본 검증을 완전히 무시하고 실행
    #          오직 사용자가 정의한 로직으로만 검증하며, 직접 타입을 변환해야 함.
    #   'wrap' : 기본 검증 로직을 감싸서(wrapping) 실행
    #         기본 검증 전후에 로직을 넣거나, 검증 실패(Exception)를 직접 핸들링할 수 있습니다.

    @field_validator("price", mode='before')
    def price_must_be_gte_0(price):
        print(f'🏐 price_must_be_gte_0(price={price}) 호출')

        try:
            price = int(price)
        except ValueError:
            raise ValueError("올바른 가격값이 아닙니다")

        if price < 0:
            raise ValueError("ERR-3]가격 오류 insert() 가격에 정상적인 입력이 되지 않았습니다.:")
        return price

    @field_validator("stock", mode='before')
    def stock_must_be_gte_0(stock):
        print(f'🏀 stock_must_be_gte_0(stock={stock}) 호출')
        try:
            int(stock)
        except ValueError:
            raise ValueError("ERR-4]stock 값 입력 오류 ")

        return stock

# 동작테스트
if __name__ == "__main__":
    try:
        # print(Inventory(id = 1, name='aaa', price=10000, stock=10, reg_date=datetime(2025,4,30,9,41,33)))    
        # print(Inventory(name='aaa', price=10000, stock=10))
        # print(Inventory(name='      ', price=10000, stock=10))
        # print(Inventory(name='bbb', price=-2, stock=10))
        # print(Inventory(name='bbb', price="홍목", stock=10))
        print(Inventory(name='bbb', price=-100, stock="정준"))
    except ValidationError as e:
        print('💥 Error:', e)
        print('🟡', e.errors())  # ValidationError 객체
            # list 형태의 구조화된 정보
            # [
            #     {
            #         'type': 'value_error',
            #         'loc': ('age',),
            #         'msg': '나이는 음수가 될 수 없습니다',
            #         'input': -1,
            #     },
            #     ...
            # ]
            # 
        for error in e.errors():
            print('🐶', error['msg'])
            print('🎃', error['loc'])        
