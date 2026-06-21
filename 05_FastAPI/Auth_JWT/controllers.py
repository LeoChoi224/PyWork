from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import select

from models import User
from schemas import UserCreate, UserResponse, Token
import auth
from database import get_db

# 1. main.py 대신 엔드포인트를 매핑할 컨트롤러 전용 라우터 객체를 생성합니다.
router = APIRouter(prefix="/api")


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    """[회원가입 엔드포인트]"""

    # 중복 유저 체크
    stmt = select(User).where(User.username == user_in.username)
    db_user = db.execute(stmt).scalars().first()    
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # 패스워드 암호화
    hashed_password = auth.get_password_hash(user_in.password)

    # DB 저장
    new_user = User(
        username=user_in.username,
        password=hashed_password,
        name=user_in.name,
        email=user_in.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

    

@router.post("/login", response_model=Token)
def login(form_data : OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """ [로그인 엔드포인트] 로그인인증 및 토큰 발행"""

    # form_data 안에 username 과 password 가 담겨 있다.

    # 유저 존재 여부 파악
    stmt = select(User).where(User.username == form_data.username)
    user = db.execute(stmt).scalars().first()
    
    # 암호 일치 여부 대조 검증
    if not user or not auth.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    # 통과 시 고유 access_token 생성 후 클라이언트에 반환
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


# FastAPI 내부 보안 시스템인 OAuth2 표준 방식을 적용하여 로그인 토큰을 헤더에서 파싱하도록 추적 지점을 생성합니다.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """1. [의존성 함수] 현재 요청자가 들고 있는 토큰을 자동 추적하여 
    실제 가입된 유저인지 파악 및 DB 객체를 실시간 동기화합니다.
    인증된 현재 유저 가져오기 의존성"""
    
    # 토큰 유효성 검증 및 username 추출
    username = auth.verify_token(token)

    # DB에서 유효한 user 인지 확인
    stmt = select(User).where(User.username == username)
    user = db.execute(stmt).scalars().first()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user    
    

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    """[회원전용 데이터 요청 엔드포인트] 
    의존성 주입(Depends) 단에서 헤더 검증 및 토큰 복호화가 완료되어 
    인가된 회원 정보만 유효하게 전달받아 응답합니다."""

    return current_user