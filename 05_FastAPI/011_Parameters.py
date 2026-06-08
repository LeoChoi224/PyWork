# 🟥 쿼리 매개변수와 경로매개변수

# FastAPI는 API를 통해 데이터를 요청할 때 주로 쿼리 매개변수와 경로 매개변수 두 가지 방식을 사용.
# '쿼리 매개변수'는 URL의 물음표(?) 기호 이후에 키-값 쌍으로 전달되며,
#      선택적인 데이터를 전송하는 데 적합합니다.
# '경로 매개변수'는 URL의 특정 부분을 대체하여
#      필수적인 리소스 식별자로서 작동합니다.


from fastapi import FastAPI
app = FastAPI()

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# FastAPI에서 경로 매개변수를 사용하려면 중괄호 를 사용합니다.
# 중괄호 안에 들어가는 이름이 파이썬 함수의 매개변수 이름과 일치해야 합니다.

# - 기본 형태: {parameter}
# - 타입 지정: {parameter:type}
#    e.g {item_id: int}
# - 경로 매개변수 연산자: {parameter:path}
@app.get("/products/{product_id}")
def read_product(product_id):
    return {"product_id": product_id}


# 🟡》타입 지정

# 타입을 명시적으로 지정하면, FastAPI는 그 타입에 따라 값의 유효성을 검증합니다. 
# 예를 들어, 다음 코드에서 member_id 는 정수 타입(int)이어야 합니다.

@app.get("/members/{member_id:int}")  # 경로 매개변수 type 지정
def read_member_with_type(member_id): 
    return {"member_id": member_id} 
# /members/abc --> 404에러

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}
# /users/abc --> 422 에러


# 🟡>경로 매개변수 연산자

# 경로 매개변수 연산자 :path를 사용하면 슬래시(/)를 포함한 문자열도 캡처할 수 있습니다.
# 다음의 예에서 sub_path는 경로 매개변수로 사용되며, 여러 부분으로 구성할 수 있습니다.

@app.get("/files/{sub_path}")
def read_file(sub_path: str):
    return {"sub_path": sub_path}
