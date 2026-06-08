# FastAPI 응답 모델은 클라이언트에 반환되는 데이터의 구조를 정의하는 데 
# 사용되는 강력한 기능입니다. 
# 응답 모델을 정의함으로써 API는 반환되는 데이터의 유효성을 보장하고, 
# OpenAPI 스키마(자동 문서화)를 생성하여 API 사용자에게 명확한 정보를 제공합니다.

# FastAPI에서 응답 모델은 필수는 아니지만, 매우 권장되는 기능입니다. 
# 응답 모델을 사용하면 API가 반환하는 데이터의 구조를 명확하게 정의하고, 
# API 문서를 자동으로 생성하여 사용자에게 제공할 수 있으며 
# 반환 데이터의 유효성 검사를 자동으로 수행할 수 있습니다.

# FastAPI의 경로 연산에서 response_model 매개변수를 사용하여 응답 모델을 지정할 수 있습니다. 
# 이 매개변수는 경로 연산 함수에 의해 반환되는 데이터의 형태를 Pydantic 모델로 정의하게 해줍니다. 
# 이 모델은 반환된 데이터가 클라이언트로 전송되기 전에 시리얼라이즈되는 방식을 결정합니다. 
# 여기서 시리얼라이즈(serialize)라는 용어는 데이터를 일련의 비트로 변환하여 파일, 메모리, 네트워크를 통해 저장하거나 전송할 수 있는 형식으로 만드는 과정을 말합니다.

from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float

def get_item_from_db(id): 
    # 테스트용: 간단한 아이템 반환 
    return { 
        "name": f"Simple Item:{id}", 
        "description": "A simple item description",
        "price": 51.0, 
        "dis_price": 45.0
    }

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = get_item_from_db(item_id)
    return item

# response_model= 이 없는 경우에는 item 의 모든 key 들이 response 되나.
# response_model=Item 이 지정된 후에는 Item 모델의 필드들만 resposne 된다.

# 🟡 response_model 을 사용하는 장점
# • 데이터 검증: 반환되는 데이터가 response_model에 정의된 모델의 필드 및 타입과 일치하는지 FastAPI에 의해 자동으로 검증됩니다.
# • 자동 문서 생성: FastAPI는 response_model을 사용하여 API 문서에 정확한 응답 형식을 표시합니다. 이는 API 사용자가 기대할 수 있는 응답의 구조를 이해하는 데 도움이 됩니다.
# • 보안: response_model은 경로 연산이 노출할 데이터를 제한하는 데 사용할 수 있습니다. 예를 들어, 모델에서 반환하지 않아야 하는 내부 정보를 숨길 수 있습니다.


# 🟡 주요 '응답 모델'의 종류

# • 기본 응답 모델: 가장 일반적인 형태.
#   Pydantic 클래스를 이용해 모델을 정의할 수 있습니다.

# •Generic 응답 모델:
#   제네릭 타입을 활용하여 다양한 타입의 응답을 동일한 엔드포인트에서 다룰 수 있습니다.

# • Union 응답 모델:
#   여러 가능한 모델 중 하나가 될 수 있는 경우에 유용합니다.

# • List 응답 모델: 리스트 형태의 데이터를 반환할 때 사용합니다.

# 응답 모델은 FastAPI에서 클라이언트에게 반환될 데이터의 구조를 선언적으로 정의합니다.
# 이를 통해 데이터의 유효성 검사, 자동 문서화, 그리고 클라이언트로 보낼 데이터의 시리얼라이즈가 이루어집니다.


# 🟦 기본 응답 모델

# Pydantic의 BaseModel을 상속하여 API 응답으로 사용할 데이터 모델을 정의합니다.
# FastAPI 경로 연산에서 response_model 매개변수를 이용해 이 모델을 지정하면,
# 해당 경로 연산은 지정된 모델에 따라 응답 데이터를 검증하고 시리얼라이즈 합니다.

# Pydantic 모델을 정의합니다. 이 모델은 으답 데이터의 구조를 나타냅니다.
class Product(BaseModel):
    name: str # 이름 필드
    price: float # 가격 필드

@app.get("/product/", response_model=Product)
def get_product():
    return {"name": "milk", "price": 3.5}


# 🟦 Generic 응답 모델

# Generic 응답 모델은 FastAPI에서 타입 매개 변수를 이용하여 유연한 응답 타입을 정의할 수 있게 합니다.
# 이는 다양한 데이터 타입에 대해 재사용 가능한 응답 모델을 만들고자 할떄 유용합니다.

from typing import TypeVar, Generic
from pydantic.generics import GenericModel

# 제네릭 타입 매개변수 선언
T = TypeVar("T")

class GenericItem(GenericModel, Generic[T]):
    data: T # T 타입필드 data 선언

@app.get("/generic_item/", response_model=GenericItem[str])
async def get_genric_item():
    return {"data": "str_item"}
    # return {"data": 123456}

@app.get("/generic_item2/", response_model=GenericItem[int])
async def get_generic_item():
    return {"data": 12345}


# 🟦 Union 응답 모델

# Union 응답 모델은 파이썬의 typing 모듈에 있는 Union 타입을 사용하여
# 하나의 경로 연산에서 여러 다른 모델 중 하나를 반환할 수 있도록 합니다.
# 이는 API가 다양한 가능성 중 하나를 선택해서 반환해야 할 때 매우 유용합니다.
# Union은 타입 힌트로 사용되며, 여기에 지정된 모델 중 하나가 응답 데이터로 사용될 수 있음을 나타냅니다.

from typing import Union

class Cat(BaseModel):
    name: str
    color: str

class Dog(BaseModel):
    name: str
    weight: float

@app.get("/animal/", response_model=Union[Cat, Dog])
async def get_animal(animal: str):
    if animal == "cat":
        return Cat(name="Whiskers", color="white")
    elif animal == "dog":
        return Dog(name="Fodo", weight=17.9)

    return {'name': '김정준', 'grade': 1}
    # return {'name': '김정준', 'grade': 1, 'weight': 80.0}


# 🟦 List 응답 모델

# List 응답 모델은 FastAPI에서 리스트 형태의 데이터를 반환할 때 사용합니다.
# 이 모델은 List 타입 힌트와 함께 사용되며, 반환되는 데이터가 리스트의 각 항목이 특정 모델을 준수하는지를 검증합니다.
# 이를 통해 API 사용자는 반환된 데이터가 일정한 구조를 가지는 배열임을 기대할 수 있습니다.

from typing import List

class Profile(BaseModel):
    name: str

@app.get("/profiles", response_model=List[Profile])
async def get_profiles():
    return [{"name": "장희준"}, {"name": "문태현"}]
