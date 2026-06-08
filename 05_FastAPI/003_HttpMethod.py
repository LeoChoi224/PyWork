from fastapi import FastAPI

app = FastAPI()  # FastAPI 인스턴스 생성

@app.get("/")
def root():
    return {"Chapter": "Http Method"}

# HTTP 메서드는 클라이언트가 서버에게 어떤 동작을 해달라고 요청하는 방식을 정의합니다.
# FastAPI는 이러한 메서드를 사용하여 요청의 의도를 명확히 하고, 적절한 엔드포인트에 연결하는 라우팅을 수행합니다.

# - GET:
#   이 메서드는 서버로부터 정보를 '조회' 요청할 때 사용합니다. 데이터를 가져오는 read-only 작업에 적합하며,
#   서버의 상태나 데이터를 변경하지 않습니다.
#   예를 들어 사용자의 프로필 데이터나 게시글 목록을 가져올 때 GET 요청을 사용합니다.

# - POST:
#   서버에 데이터를 전송하여 새로운 리소스를 '생성'하려고 할 때 POST 메서드를 사용합니다.
#   예를 들어 새 사용자를 등록하거나 게시글을 작성할 때 사용합니다.
#   POST 요청은 데이터를 서버의 특정 경로에 제출하며, 해당 데이터는 주로 요청 바디에 포함됩니다.

# - PUT:  혹은 PATCH:
#   PUT 메서드는 지정된 리소스의 '전체' '수정(업데이트)'를 수행합니다.
#     예를 들어, 사용자의 전체 프로필을 업데이트하는 경우에 PUT 요청을 사용할 수 있습니다.
#     PUT은 리소스가 존재하지 않는 경우 새로 생성할 수도 있지만, 주로 기존 리소스의 완전한 교체를 의미합니다.
#   PATCH 메서드는 지정된 리소스의 '일부' 업데이트 수행.

# - DELETE: DELETE 메서드는 지정된 리소스를 '삭제'할 때 사용합니다.
#   이 요청은 서버에 리소스의 제거를 지시하며, 성공적으로 처리된 경우 리소스에 더 이상 접근할 수 없습니다.
#   예를 들어, 사용자가 자신의 계정을 삭제하거나 작성한 게시글을 제거하고 싶을 때 DELETE 요청을 사용할 수 있습니다.

# FastAPI를 사용하면 이러한 메서드를 각각의 라우팅 데코레이터
# (@app.get(), @app.post(), @app.put(), @app.delete() 등)와 함께 사용하여
# 다양한 HTTP 요청을 처리하는 API를 손쉽게 구성할 수 있습니다.


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/")
def read_items (skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.post("/items/")
def create_item(item: dict):
    return {"item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "updated_item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} has been deleted"}
