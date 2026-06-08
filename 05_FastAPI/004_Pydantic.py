# FastAPI에서 Pydantic(파이단틱)은 데이터 검증과 데이터 직렬화를 매우 쉽게 만들어줍니다.

# 데이터 검증(data validation)이란
#   사용자나 다른 시스템이 보내는 데이터가 올바른 형식과 값인지 확인하는 과정입니다.
#   예를 들어, 사용자가 금액을 입력할 때 문자열을 넣으면 이는 올바르지 않은 데이터입니다.
#   데이터 검증을 통해 이런 잘못된 정보를 사전에 차단할 수 있습니다.

# 데이터 직렬화(data serialization)란
#   복잡한 데이터 구조를 바이트나 문자열로 변환해서 다른 시스템과 쉽게 데이터를 교환할 수 있는 형태로 만드는 것입니다.
#   반대 과정을 '역직렬화'라고 하며, 이는 문자열이나 바이트를 원래의 데이터 구조로 되돌리는 것입니다.

# 데이터 검증과 데이트 직렬화는 다음과 같은 이유로 필요합니다.
#   • 데이터 검증: 잘못된 데이터가 처리되는 것을 막아서 버그나 다양한 문제를 예방합니다.
#   • 데이터 직렬화: 서로 다른 시스템끼리 데이터를 쉽게 주고받을 수 있게 해줍니다.

# 특히 FastAPI에서는
# 요청 바디로부터 데이터를 받기 위해 반드시 Pydantic 모델을 사용해야 하는 것은 아니지만, Pydantic 모델을 사용하는 것을 권장합니다.
# 데이터 요청을 위해 자주 사용하는 HTTP POST 메서드는 데이터를 요청 바디에 넣어서 전송하므로,
# POST 메서드로 API를 선언하는 경우에는 Pydantic 모델 사용을 고려할 필요가 있습니다.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"Chapter": "Pydantic model"}

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.post("/items/")
def create_item(item: Item):  # Pydantid model 로 매개변수 받는다
    return {"item": item.model_dump()}

# {"name": "Bread", "price": 3.5, "is_offer": true}     ✅ 200 ok
# {"name": "Bread", "price": "박지원", "is_offer": true}  💢 422 Unprocessable Entity


from typing import Optional

class Book(BaseModel):
    name: str   # 문자열, 필수
    description: Optional[str] = None   # 문자열, 선택적, 기본값 None
    price: float   # 실수, 필수
    tax: float = 0.1  # 실수, 선택적, 기본값 0.1

@app.post("/books/")
async def create_item(book: Book):
    return {"book": book.model_dump()}


# 🟡 필드 제약 조건
# Field는 Pydantic 모델에서 필드에 추가적인 정보나 제약 조건을 지정할 때 사용하는 객체입니다.
# 다양한 인자를 통해 세부 설정을 할 수 있으며 주요 옵션은 다음과 같습니다.

#   - default: 필드의 기본값을 지정합니다. 만약 기본값이 없다면 필수 입력 필드가 됩니다.
#   - alias: JSON 필드의 이름을 파이썬 변수와 다르게 지정할 때 사용합니다.
#   - title: 스키마에서 볼 수 있는 추가적인 정보로, 주로 문서화에 사용됩니다.
#   - description: 필드에 대한 설명을 추가합니다. 주로 API 문서에서 확인할 수 있습니다.
#   - min_length & max_length: 문자열 길이의 최솟값과 최댓값을 지정합니다.
#   - gt(greater than), lt(less than): 숫자의 크기 제약을 추가
#   - regex: 정규 표현식을 통한 패턴 매칭을 할 수 있습니다.

from pydantic import Field
from typing import List


class Pet(BaseModel):
    #'name'은 최소 2자, 최대 50자를 가져야 하며 필수 필드입니다.
    name: str = Field(..., title="Pet Name", min_length=2, max_length=50)

    #description'은 선택 필드이며, 최대 300자까지 가능합니다.
    description: str = Field(None, description="Pet description", max_length=300)
    
    # price 는 '필수'  0보다 큰 실수
    price: float = Field(..., gt=0, description="Price must be greater than zero")

    #`tag`필드는 선택적이며, 기본값으로 빈 리스트를 갖습니다. JSON에서는 'pet-tags'로 나타납니다. 
    tag: List[str] = Field(default=[], alias="pet-tags")

@app.post("/pets/") 
async def create_pet(pet: Pet): 
    # 아이템 생성을 위한 엔드포인트로, 모델 인스턴스의 딕셔너리 표현을 반환합니다. 
    return {"pet": pet.model_dump()}

