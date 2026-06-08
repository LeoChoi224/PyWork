# FastAPI에서 Pydantic(파이단틱)은 데이터 검증과 데이터 직렬화를 매우 쉽게 만들어줍니다.

# 데이터 검증(data validation)이란
#   사용자나 다른 시스템이 보내는 데이터가 올바른 형식과 값인지 확인하는 과정입니다.
#   예를 들어, 사용자가 금액을 입력할 때 문자열을 넣으면 이는 올바르지 않은 데이터입니다.
#   데이터 검증을 통해 이런 잘못된 정보를 사전에 차단할 수 있습니다.

# 데이터 직렬화(data serialization)란
#   복잡한 데이터 구조를 바이트나 문자열로 변환해서 다른 시스템과 쉽게 데이터를 교환할 수 있는 형태로 만드는 것입니다.
#   반대 과정을 '역직렬화'라고 하며, 이는 문자열이나 바이트를 원래의 데이터 구조로 되돌리는 것입니다.

# 데이터 검증과 데이트 직렬화는 다음과 같은 이유로 필요합니다.
#   - 데이터 검증: 잘못된 데이터가 처리되는 것을 막아서 버그나 다양한 문제를 예방합니다.
#   - 데이터 직렬화: 서로 다른 시스템끼리 데이터를 쉽게 주고받을 수 있게 해줍니다.

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
    # 'name'은 최소 2자, 최대 50자를 가져야 하며 필수 필드입니다.
    name: str = Field(..., title="Pet Name", min_length=2, max_length=50)

    # description'은 선택 필드이며, 최대 300자까지 가능합니다.
    description: str = Field(None, description="Pet description", max_length=300)
    
    # price 는 '필수'  0보다 큰 실수
    price: float = Field(..., gt=0, description="Price must be greater than zero")

    # `tag`필드는 선택적이며, 기본값으로 빈 리스트를 갖습니다. JSON에서는 'pet-tags'로 나타납니다. 
    tag: List[str] = Field(default=[], alias="pet-tags")

@app.post("/pets/") 
async def create_pet(pet: Pet): 
    # 아이템 생성을 위한 엔드포인트로, 모델 인스턴스의 딕셔너리 표현을 반환합니다. 
    return {"pet": pet.model_dump()}

# 🟦 중첩된 모델: 복잡한 형태의 데이터 모델링 할때 유용

class Image(BaseModel):
    url: str
    name: str

class Profile(BaseModel):
    name: str
    description: str
    image: Image

@app.post("/profiles/")
def create_profile(profile:Profile):
    return {
        "profile": profile.model_dump(),
        "image": profile.image.model_dump()
        }

# 🟡 이처럼 중첩된 모델을 사용할 때의 장점!
# - 재사용성: Image 모델을 여러 다른 모델에서 재사용할 수 있습니다.
# - 가독성: 복잡한 데이터 구조를 좀 더 읽기 쉽게 만들어줍니다.
# - 유지보수: 나중에 Image 모델을 업데이트하면, 그 모델을 사용하는 모든 부분에서 자동으로 업데이트됩니다.


# 🟦 List 와 Union
# List와 Union은 복잡한 데이터 구조와 다형성을 모델링할 때 유용한 타입 힌트입니다.

# - List: List[<type>] 형식을 사용하여 지정된 <type>의 여러 값을 갖는 배열이나 리스트를 나타냅니다.
#   예를 들어 List[int]는 정수들의 리스트를 의미하며, List[str]은 문자열들의 리스트를 의미합니다.
#   Pydantic 모델에서 리스트를 사용하면 리스트 내 각 아이템에 대해 정의된 타입의 유효성이 검사됩니다.

# - Union: Union[<typel>, <type2>...] 형식으로 여러 타입 중 하나를 허용하는 변수를 정의할 수 있습니다.
#   예를 들어 Union[int, str]은 해당 필드가 정수 또는 문자열일 수 있음을 나타냅니다.
#   Pydantic은 제공된 값이 Union에 지정된 타입 중 하나와 일치하는지 검사합니다.

from typing import List, Union

class Member(BaseModel):
    name: str
    tags: List[str]
    variant: Union[int, str]

@app.post("/members/")
def create_member(member: Member):
    return {"member": member.model_dump()}

# 🟡 제네릭 타입

# 제네릭 타입은 일종의 '타입 템플릿'입니다. 그래서 List[T] 같은 형태로 사용합니다.
# 여기서 T는 '아무 타입이나' 올 수 있습니다. 그래서 제네릭 타입을 사용하면 여러 다른 타입에 대해 동일한 로직을 적용할 수 있습니다.

# T는 타입 변수(type variable)라고 부르며, 주로 제네릭에서 자주 볼 수 있습니다.
# T는 단순한 변수일 뿐, 의미 자체는 없습니다. T 대신에 U, V, W 등 다른 알파벳을 사용해도 되지만,
# T는 type의 첫 글자라서 관례적으로 많이 사용됩니다.
# T는 그 자리에 어떤 타입이 들어갈 수 있는지를 나타내는 '자리 표시자' 정도로 생각하면 됩니다.

# FastAPI와 Pydantic에서 제네릭 타입을 사용하려면 typing 모듈의 TypeVar와 Generic 클래스를 이용합니다.

# - TypeVar:
#   TypeVar는 타입 변수를 생성하며, 제네릭 클래스나 함수가 사용할 수 있는 타입 매개변수를 정의합니다.
#   동적 타이핑 언어인 파이썬에서 TypeVar는 정적 타입 검사 도구가 타입 정보를 이해하고 검사할 수 있게 만드는 역할을 합니다.
#   제네릭 타입을 사용하려면 먼저 타입 변수를 명시적으로 선언해야 하며, 그것이 바로 TypeVar의 역할입니다.
#   TypeVar를 선언할 때는 일반적으로 변수 이름과 같은 문자열을 인자로 전달합니다.
#   예를 들어 T = TypeVar('T')와 같이 작성합니다.

# - Generic[T]:
#    Generic[T]는 T를 타입 매개변수로 가지는 제네릭 클래스를 정의할 때 사용합니다.

# T=TypeVar('T')에서 사용되는 T는 제네릭 프로그래밍의 관례를 따르는 표현입니다.
#  여기서 T는 타입 변수(type variable)를 정의할 때 사용되는 이름입니다.
#  이 구문에서 왼쪽과 오른쪽 T의 역할은 서로 다릅니다.

# - 왼쪽의 T: 이것은 타입 변수의 이름으로, 코드 내에서 타입 힌트로 사용됩니다.
#    예를 들어, Generic[T] 또는 List[T]와 같이 실제 코드에서 제네릭 타입으로 사용될 때 참조하는 이름입니다.
# - 오른쪽의 'T': 이것은 TypeVar 함수에 전달되는 문자열 리터럴로,
#    TypeVar 객체를 생성할 때 내부적으로 사용되는 식별자입니다.
#    파이썬의 타입 시스템과 관련된 도구들(e.g linters, IDEs)이 타입 정보를 처리할 때
#    이 문자열을 사용하여 타입 변수를 식별합니다.

# 즉, 왼쪽의 T는 타입 변수를 코드 내에서 사용하기 위한 식별자이며,
# 오른쪽의 'T'는 그 타입 변수를 내부적으로 구별하기 위한 문자열입니다.
# 이 구분은 주로 타입 체크 도구나 런타임이 아닌 타입 힌트를 분석할 때 중요합니다.

# TypeVar를 정의할 때 오른쪽에 전달하는 문자열 'T'는 문서화와 가독성을 위한 것이며,
# 이 문자열이 타입 체커에 의해 사용되는 실제 타입 변수의 이름이 됩니다.
# 왼쪽에 사용된 T는 이후 코드에서 해당 타입 변수를 참조할 때 사용하는 이름입니다.

# 이러한 구문은 파이썬에서 타입 힌트를 사용할 때 일관성을 유지하고,
# 타입 변수를 명확히 식별하기 위한 관례적인 방식입니다. 다른 변수 이름을 사용할 수도 있지만,
# T는 제네릭 타입의 'Type'을 나타내는 전통적인 이름으로 널리 받아들여지고 있습니다.

# 다른 예로, 만약 두 개의 다른 타입 변수가 필요하다면 U=TypeVar('U')와 같이 다른 문자를 사용하여 선언할 수 있습니다.
# 이는 T와는 독립적인 또 다른 타입 변수를 정의하는 것이며, 이러한 방식으로 복잡한 타입 구조를 만들 수 있습니다.

from typing import TypeVar, Generic

# 타입변수 T 선언
T = TypeVar('T')

class GenericItem(BaseModel, Generic[T]):
    name: str
    content: T  # T 타입   <- content 타입은 동적으로 결정될수 있다.


