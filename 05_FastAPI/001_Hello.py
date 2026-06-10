from fastapi import FastAPI

app = FastAPI()  # FastAPI 인스턴스 생성

"""
실행
uvicorn 001_Hello:app --reload

• 001_Hello: FastAPI 애플리케이션 코드가 작성된 파이썬 파일의 이름을 의미
     (011_HelloWorld.py 파일 내에 있다고 가정).

• app: FastAPI 인스턴스를 생성하는 객체의 변수 이름
     (즉, app = FastAPI()라고 정의된 경우).

• --reload: 이 옵션은 개발 중에 코드를 수정할 때마다 서버가 자동으로 재시작하도록 설정.
       코드 변경 사항이 바로 적용되도록 해서 개발 과정을 더 빠르고 효율적으로 만들어줍니다.

"""

@app.get("/")  # HTTP GET 요청 경로 "/" 받으면 아래 함수가 처리하여 응답
def read_root():
    # 리턴하는 값이 응답이 된다.
    return {"message": "Hello FastAPI!"}

# 경로매개변수
@app.get("/items/{item_id}")  
def read_item(item_id):  # 경로매개변수는 함수의 매개변수로 받음. 기본적으로 str 으로 받는다
    return {"item_id": item_id}


# @app.get("/items/{item_id}") <- Path Operation decorator 
# 함수 <- Path operation function

# 라고 공식문서에는 있으나.

# 일반적으로 이런 함수를 handler 혹은 endpoint (엔드포인트) 라고함.
#            라우팅 함수 (routing function) 이라고도 함.

@app.get("/users/{user_id}/items/{item_name}")
def read_user_item(user_id, item_name):
    return {"user_id": user_id, "item_name": item_name}

# 동일한 라우팅 경로를 처리하는 함수들이 있다면
# FastAPI 는 에러를 발생시키지 않는다! -> 💢주의 버그 만들수 있다.
# FastAPI 는 등록된 순서대로 위에서부터 매칭하여 가장 먼저 일치하는 라우트 사용
@app.get("/items/{item_id}")  
def get_item(item_id):
    return {"get_id": item_id}


# 쿼리 매개변수
@app.get("/items/")
def read_item_with_limit(skip, limit):   # 쿼리문자열 매개변수도 함수의 매개변수로 받는다
    return {"skip", "limit"}

# /items/?skip=5&limit=8
# /items/?skip=5     에러 422 Unprocessable Entity

@app.get("/posts/")
def get_posts(limit = 0, rows = 10):
    return {"limit": limit, "rows": rows}

# /posts/?limit=5&rows=15
# /posts/?limit=5     ✅ 200 ok 기본 매개변수 값으로 동작