# 인증 관련 로직
import os
from datetime import datetime, timedelta, UTC
import jwt
import bcrypt # 단방향 암호화(해싱)
from fastapi import HTTPException, status
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

def get_password_hash(password: str) -> str:
    """
    1. 사용자가 가입 시 입력한 평문 패스워드를 salt를 부여하여 안전하게 단방향 암호화(해싱)합니다.
    최신 bcrypt 호환성 버그 예방을 위해 직접 바이트 변환 후 해싱 메커니즘을 적용
    """
    # 문자열을 바이트로 변환 후 솔트 생성 및 해싱
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    
    # DB 저장을 위해 문자열로 리턴
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """ 2. 로그인 시 사용자가 입력한 평문 비밀번호와 DB에 들어있는 기존 해시 패스워드가 정확히 매칭되는지 대조"""
    password_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def create_access_token(data: dict) -> str:
    """ 3. 로그인 인증 성공 시, 유저 고유 식별 정보(sub)와 유효기간(exp)을 담아 
        대칭키 암호화된 JWT 토큰 문자열을 생성"""
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> str:
    """ 4. 요청 헤더로 넘어온 JWT 토큰을 SECRET_KEY로 역해독하여 
    변조 여부를 확인하고 식별 데이터를 꺼내옵니다."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Could not validate credentials"
            )
        return username
    except jwt.PyJWTError:  # 토큰이 위조되었거나 만료 시간이 초과된 경우 자동 차단 예외 처리
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Could not validate credentials"
        )    
    
if __name__ == "__main__":
    """✨테스트✨"""

    username = "user1"
    password = "1234"

    encoded = [get_password_hash(password) for i in range(3)]
    print('\n'.join(encoded))
    print()

    verification = [verify_password(password, enc_pw)  for enc_pw in encoded]
    print('⭕', verification)
    print()

    jwt_token = create_access_token(data = {"sub": username})
    print('😎', jwt_token)
    print()

    extracted_username = verify_token(jwt_token)
    print('✅', extracted_username)
    print()


