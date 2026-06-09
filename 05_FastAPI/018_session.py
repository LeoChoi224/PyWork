# 🟦 Startlette 란.
# "FastAPI는 Starlette이라는 강력한 엔진 위에 얹혀진 아주 세련된 디자인의 자동차"

# Starlette 는 FastAPI가 작동하기 위한 뿌리이자 핵심 구성 요소
# 기술적으로 말하면, FastAPI는 Starlette의 클래스를 직접 *상속(Inheritance)*받아 만들어졌습니다.

# Starlette: 파이썬에서 '비동기 웹 서비스'를 만들기 위한 경량 ASGI 프레임워크/툴킷입니다. 
#   웹 서버의 기본적인 기능(라우팅, 쿠키, 세션, 상태 코드 등)을 담당합니다.
#   매우 빠른 속도 (최상위!)

# FastAPI: Starlette 기능과 성능 위에 Pydantic과 유용한 기능들을 더해, 
#   개발자가 API를 더 쉽고 빠르게 만들 수 있도록 만든 고수준 프레임워크입니다.
#   Starlette의 모든 기능을 그대로 제공
#   Pydantic을 통한 자동 검증 및 변환
#   Swagger UI / Redoc 자동 생성
#   강력한 Dependency Injection 시스템

# ----------------------------------------------------------------------------

from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

@app.post("/set/")
def set_session(request: Request):
    # Request 객체의 session 속성을 통해 세션 데이터 저장
    request.session['username'] = "john"
    return {"message": "Session value set"}

@app.get("/get/")
def get_session(request: Request):
    username = request.session.get("username", "Guest")
    return {"username": username}



@app.post("/login/")
def login(request: Request, username: str, password: str):
    if username == "john" and password == "1234":
        # 세션 추가
        request.session["username"] = username
        return {"message": "Successfully logged in"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
# 인증된 사용자만 접근 가능한 엔드포인트
@app.get("/dashboard/")
def dashboard(request: Request):
    username = request.session.get("username") 
    if not username:
        raise HTTPException(status_code=401, detail="Not authorized")
    
    return {"message": f"Welcome to the dashboard!!, {username}"}