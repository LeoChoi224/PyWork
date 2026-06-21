from datetime import datetime
from pydantic import BaseModel, EmailStr, field_validator

# 1. 공통적으로 사용되는 유저 필드를 정의한 기본 스키마 (데이터 검증 및 데이터 전달용)
class UserBase(BaseModel):
    username: str
    name: str
    email: EmailStr | None = None  # EmailStr을 사용하여 이메일 골뱅이(@) 및 도메인 형식을 자동 검증
                                   # pip install pydantic[email]

    @field_validator('email', mode="before")
    @classmethod
    def allow_empty_string_for_email(cls, v):
        if v == "":
            return None
        
        return v


# 2. 회원가입 API(/api/register) 요청 바디 데이터 검증에 사용되는 스키마
class UserCreate(UserBase):
    password: str  # 회원가입 시에는 비밀번호 입력이 필수적임

# 3. 클라이언트에게 유저 정보를 안전하게 응답값으로 돌려줄 때 사용하는 스키마 (보안을 위해 password 제외)
class UserResponse(UserBase):
    id: int
    created_at: datetime

    # SQLAlchemy의 ORM 모델 인스턴스(객체 체인) 구조를 Pydantic 객체 형식으로 자동 파싱하도록 허용하는 설정입니다.    
    class Config:
        from_attributes = True

# 4. 로그인 성공 후 발급될 JWT 토큰 구조 규격 인터페이스
class Token(BaseModel):
    access_token: str
    token_type: str

# 5. JWT 토큰을 디코딩했을 때 페이로드 내부에 정상적인 유저 식별 정보가 들었는지 검증하는 용도
class TokenData(BaseModel):
    username: str | None = None