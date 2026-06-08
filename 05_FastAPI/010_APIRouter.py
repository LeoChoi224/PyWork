# 🟥 APIRouter

# FastAPI에서의 APIRouter는 매우 강력한 도구입니다.
# 플라스크에서의 블루프린트와 유사하게 작동하며,
# 이를 이해하면 라우트 관리가 더욱 간편해집니다.

# 웹 애플리케이션을 개발할 때 코드가 길어지고 복잡해질 수 있습니다.
# 이런 경우에 코드를 모듈화하고 잘 구조화하는 것이 중요한데, 이때 APIRouter 사용.

from fastapi import APIRouter

router1 = APIRouter()
# 이제 이 router에 라우트를 추가할 수 있습니다.

@router1.get("/items/")  # "/api" + "/items/" => "/api/items/"
def read_items(): 
    return {"Hello": "World"}

@router1.get("/item/{id}")  # "/api" + "/items/{id}" => "/api/items/{id}"
def read_items(id: int): 
    return {"item": id}


from fastapi import FastAPI
app = FastAPI()

# 위 router 를 FastAPI 앱에 포함시킨다!
# app.include_router(router1)

# - URL 접두사
#   include_router() 함수를 사용할 때 prefix 매개변수를 통해 모든 라우트에 공통으로 적용되는 URL 접두사를 설정할 수 있습니다.
# - 태그
#   tags 매개변수를 통해 자동 생성되는 API 문서에 태그를 추가할 수 있습니다.
app.include_router(router1, prefix="/api", tags=["items"])
app.include_router(router1, prefix="/webtoon", tags=["webtoon"])


# 🟦 APIRouter 와 의존성 함수.
# 의존성(dependency) 함수는 
# FastAPI에서 특정 라우터나 엔드포인트가 **실행되기 전에** 수행되는 함수입니다. 
# 일반적으로 의존성 함수는 인증, 권한 확인, 데이터 검증 등을 수행합니다. 

# - Depends(): 의존성을 설정하는 데 사용하는 함수.
#   e.g Depends(의존성 함수)

# - APIRouter: dependencies 매개변수를 이용하여 라우터 레벨에서 의존성을 설정할 수 있다.
#   e.g. APIRouter(dependencies=[Depends(+)])

"""
예제:  
  사용자가 특정 토큰을 가지고 있는지 확인해보는 의존성 함수를 작성
  사용자가 특정토큰 ('my-secret-token') 을  URL 매개변수로 전달했는지 확인하는 함수로 작성
"""
from fastapi import HTTPException, Depends

def check_token(token: str):
    print(f'✅ check_token(token={token}) 호출')
    if token != "my-secret-token":
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return token

router_depends_api = APIRouter(dependencies=[Depends(check_token)])

@router_depends_api.get("/items/")  # "/depends/api" + "/items/"
def get_items():
    return {"message": "Access granted, you can view the items"}

@app.get("/public/")
def read_public():
    return {"message": "This is a public endpoint."}

app.include_router(router_depends_api, prefix="/depends/api")


# 🟦 APIRouter 설정을 상속
# FastAPI에서 APIRouter는 다른 APIRouter 또는 FastAPI 애플리케이션에 추가될 수 있습니다. 
# 이때 상위 라우터에서 설정한 옵션들을 하위 라우터에서 상속받을 수 있습니다. 
# 주로 dependencies, tags 같은 설정이 해당합니다. 
# 이 기능은 중복 코드를 줄이고, 특정 설정을 여러 라우터에 쉽게 적용할 수 있도록 도와줍니다.

def common_dependency():
    print("🐹 common_dependency() 호출")
    return "This is common dependency"

# 상위라우터
parent_router = APIRouter(prefix="/parent", tags=["parent"], dependencies=[Depends(common_dependency)])
@parent_router.get("/item")  # /parent/item
def read_parent_item():
    return {"message": "💚 This is an item from the parent router"}


def child_dependency():
    print("🌐 child dependency")
    return "✨Session✨"

# 하위라우터
child_router = APIRouter()
@child_router.get("/item")  # /parent/child/item
def read_child_item(session: str = Depends(child_dependency)):
    return {"message": "💛 This is an item from the child router", "session": session}
# 하위 라우터를 상위 라우터에 추가 (상속)
parent_router.include_router(child_router, prefix="/child")

# 상위 라우터를 앱에 추가
app.include_router(parent_router)

# ==============================================
# 라우터들을 모듈별로 분리하여 제작하면 분업 및 유지보수에 유리하다
# ==============================================
import board_controller
app.include_router(board_controller.router)
