# JWT 생성, 검증

from fastapi import FastAPI, HTTPException, Header
import jwt     # pyjwt 패키지
import datetime

app=FastAPI()

SECRET_KEY = "my_secret_key"
# ↑ 토큰을 암호화/복호화 할때 사용하는 비밀키. 
# 이 키는 외부에 노출되면 안되고 복잡하게 설정하는 것이 좋다.
# SECRET_KEY의 길이는 사용하는 알고리즘과 보안 요구 사항에 따라 다릅니다. 
# 일반적으로는 길수록 더 안전하다고 할 수 있습니다. 
# HS256을 사용하는 경우, 최소한 256비트(32바이트 또는 32자리 ASCII 문자) 이상을 권장. 
# 하지만 실제로는 더 긴 키를 사용하는 것이 더 안전할 수 있습니다.
# 예를 들어, 64자리나 128자리의 랜덤한 문자열을 사용할 수 있습니다. 
# 길이가 길수록 무작위 공격에 대한 저항성이 높아집니다. 
# 또한 키는 복잡한 문자, 숫자, 특수문자의 조합으로 이루어져야 합니다.

# 키 관리에 대한 별도의 정책이나 모듈을 사용하는 것도 좋은 방법입니다. 
# 예를 들어, AWS의 KMS(Key Management Service)나 
# 하시코프(HashiCorp)의 볼트(Vault)와 같은 서비스를 사용할 수 있습니다.


# JWT 생성
def create_jwt_token(data: dict):

    # JWT 만료시간. 설정
    #  UTC 현재 시각에 1시간을 더해서 설정 (가장 많이 사용하는 설정)
    # expiration 설정은 서비스의 특성과 보안 요구 사항에 따라 다릅니다.
    # 다양한 시간 설정을 통해 토큰의 만료 시간을 제어할 수 있다,
    expiration = datetime.now(datetime.timezone.utc) + datetime.timedelta(hours = 1)

    # JWT 의 "exp" 클레임에 만료시간 설정
    data["exp"] = expiration

    # 입력된 data, SECRET_KEY, 그리고 algorithm을 사용해 JWT 토큰을 생성
    # algorithm=: HS256 말고도 여러 알고리즘이 있습니다. 
    #   예로 HS384, HS512, RS256 등이 있지만, HS256을 가장 일반적으로 많이 사용합니다.
    # payload= : 페이로드에 들어갈 데이터 부분입니다. 예를 들어, 사용자 권한이나 ID 등을 넣을 수 있습니다.
    return jwt.encode(payload=data, key=SECRET_KEY, algorithm="HS256")

# JWT 검증
def verify_jwt_token(token: str):
    try:
        # 입력된 jwt token 을 SECRET_KEY 와 함께 알고리즘 사용하여 복호화
        return jwt.decode(jwt=token, key=SECRET_KEY, algorithms=["HS256"])  # dict 리턴
        # ↑ 이 함수는 여러 옵션과 함께 사용할 수 있습니다.
        # jwt.decode(token, key, algorithms, verify, options, **kwargs)  -> dict[str, Any]
        # •jwt=: 검증할 JWT 토큰 문자열입니다.
        # •key=: 검증에 사용할 키입니다. 이 예제에서는 SECRET_KEY를 사용했습니다.
        # •algorithms=: 검증에 사용할 암호 알고리즘의 리스트입니다. 
        #      예를 들어 ["HS256", "RS256"] 같이 여러 개를 지정할 수 있습니다.    
    except:
        raise HTTPException(status_code=401, detail="Invalid token")


# 토큰 생성
# username 을 받아서 토큰을 생성
@app.get("/token")
def generate_token(username: str):
    return {"token": create_jwt_token({"username": username})}

# 토큰 검증
# 인증된 상태에서만 접근 가능한 엔드포인트  (인증토큰이 있는 요청) 
# Header로부터 token을 받아 검증합니다.
# - token: HTTP 헤더에서 토큰을 받습니다. 
# - 이 값이 없거나 유효하지 않으면 401 상태 코드를 반환합니다.

# token: str = Header(None)  <- FastAPI의 강력한 기능
#     요청 HTTP 헤더중에서 이름이 'token' 인 값을 자동으로 찾아서 token 매개변수에 넣어줌.
#     Header(None)  : 기본값 None  .  만약 헤더에 'token' 이 없다면 기본값 None

@app.get("/protected")
def read_protected_route(token: str = Header(None)):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    decoded = verify_jwt_token(token)

    return {"message": "This is a protected route", "decoded": decoded}

