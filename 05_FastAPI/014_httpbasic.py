# 인증 (Authentication)
# 인가 (Authorization)

# FastAPI 에선 인증 인가를 따로 구분하지 않고 걍 Authorization (인증) 이라고 하기도 한다…

# 🟥 기본 인증 (Basic authorization) 메커니즘

# 'Authorization'이라는 특별한 HTTP 헤더를 사용하여 인증하는 방법.
# 예를 들어, HTTP 요청을 할 때 'Authorization: Basic <인코딩된 문자>과 같은 헤더가 구성됩니다. 
#  여기서 'Basic'은 인증 방식을 나타내고, <인코딩된 문자열>은 실제 중 정보가 담긴 부분입니다. 
# '아이디: 비밀번호' 형태의 문자열을 Base64 방식으로 인코딩한 값이 들어갑니다. 
#  Base64는 데이터를 텍스트 형식으로 저장하고 전송하기 위해 사용되는 인코딩 방식입니다.

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

# 'Basic 인증 객체' 생성. 이를 의존주입 하면 객체가 요청헤더에서 인증정보를 읽어온다. -> HTTPBasicCredentials
security = HTTPBasic()

app = FastAPI()

# 현재 인증정보를 가져오는 함수
def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    print('✨', credentials)   # username, passowrd 속성이 담겨 있다

    if credentials.username != 'alice' or credentials.password != "1234":
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return credentials.username

# 🟦 아래 API 는 인증(로그인)이 필요한 API 라 하자
@app.get("/users/me")
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}