from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Chapter": "Type Hint"}

# FastAPI에서 경로 매개변수나 쿼리 매개변수에 타입 힌트를 추가하면, 
# 해당 타입에 맞지 않는 요청은 자동으로 거부됩니다. 
# 또한, 매개변수에 기본값을 설정하여 선택적으로 만들 수 있습니다

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# /items/500    ✅ 200 ok
# /items/john   💢 422 Unprocessable Entity

@app.get("/getage/")
def read_age(age: float = 23.4):
    return {"age": age}

# /getage/?age=31.6    ✅ 200 ok
# /getage/?age=kim     💢 422 Unprocessable Entity
# /getage/?age=31

# ------------------------------------------------

# FastAPI는 typing 모듈에서 제공하는 List, Dict 같은 고급 타입 힌트를 사용하여 
# 요청 데이터를 쉽게 다룰 수 있습니다.

from typing import List
from fastapi import Query

@app.get("/details/")
def read_details(q: List[int] = Query([])):
    return {"q": q}

# ↑ Query는 쿼리 매개변수의 기본값을 설정하는 데 사용되며, 
#  유효성 검사 및 메타데이터 선언에도 사용됩니다. 
#  여기서 Query([])는 해당 쿼리 매개변수가 필수가 아님을 나타내고, 
#  기본값으로 빈 리스트를 제공합니다.

# /details/?q=1&q=2&q=3  ✅ 200 ok
# /details/              ✅ 200 ok
# /details/?q=김정        💢 422 Unprocessable Entity

# Dict와는 달리 List 타입 힌트의 경우에는 List[int] = Query([])와 같이 
# 반드시 Query() 관련 구문을 함께 넣어주어야 타입 힌트 유효성 검사가 정상 동작합니다.

from typing import Dict
@app.post("/create-item/")   # post 방식 요청 처리  (브라우저에서 확인 불가. Poastman 등을 통해 동작 확인)
def create_item(item: Dict[str, int]):
    return item

# Postman 동작시
#   request body 에  json 으로 전달  => {"name": 1}


# 다음은 타입 힌트로 사용할 수 있는 일반적인 파이썬 데이터 타입의 목록입니다.

# •기본 데이터 타입
#   -int: 정수
#   - float: 부동소수점 숫자
#   - str: 문자열
#   - bool: 불리언(True 또는 False)

# •컬렉션 타입
#   -List: 변경 가능한 순서가 있는 컬렉션
#       e.g List[int]는 정수의 리스트를 나타낸다.

#   -Tuple: 변경 불가능한 순서가 있는 컬렉션
#       e.g Tuple[str, int]는 문자열과 정수의 튜플을 나타낸다.

#   -Dict: 키와 값의 쌍을 갖는 컬렉션
#       e.g Dict[str, float]는 문자열 키와 부동소수점 숫자 값의 딕셔너리를 나타낸다.

#   -Set: 중복 없는 항목의 컬렉션
#       e.g Set [bool]은 불리언 값의 세트를 나타낸다.

# •특수 타입
#   - None: 아무런 값을 갖지 않음을 나타냄
#   - Any: 모든 타입을 허용, 타입 검사를 무시하고자 할 때 사용


# •typing 모듈의 고급 타입

#   -Optional: 값이 있거나 None일 수 있는 타입
#       eg Optional[str]은 문자열이거나 None일 수 있음

#   -Union: 여러 타입 중 하나일 수 있는 값
#       e.g Union[int, str]은 정수 또는 문자열이 될 수 있음

#   -Callable: 호출 가능한 객체(함수 등)를 나타냄
#       e.g Callable[[int, int], int]는 두 정수 매개변수를 받고 정수를 반환하는 함수

#   -Iterable: 반복 가능한 객체를 나타냄
#       e.g Iterable[str]은 문자열을 항목으로 갖는 반복 가능 객체

#   -Sequence: 시퀀스 타입을 나타냄
#       e.g Sequence[float]는 부동소수점 숫자의 시퀀스

# •사용자 정의 타입
#   -클래스나 다른 타입 힌트를 사용하여 사용자 정의 타입을 생성할 수 있음
#   e.g 클래스 Person을 정의하고 def get_person()-> Person:과 같이 사용할 수 있음

# 이러한 타입은 단독으로 사용하거나 typing 모듈의 다양한 기능과 결합하여
# 더 복잡한 타입 힌트를 만드는 데 사용할 수 있습니다.

# 예를 들어, List[Dict[str, Union[int, str]]]은
# 문자열을 key 로 하고, 정수 또는 문자열을 value으로 하는 딕셔너리의 리스트를 나타냅니다.

# FastAPI는 이러한 타입 힌트를 사용하여
# - 요청에서 받은 데이터의 형식을 검증하고,
# - 응답 데이터를 적절한 형식으로 변환하며
# - API에 대한 문서를 자동으로 생성합니다. -> /docs , /openapi.json
