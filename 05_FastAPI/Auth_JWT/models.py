from datetime import datetime
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class User(Base):
    __tablename__ = "a_users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # 회원 관리를 위한 필수 식별자 유저네임 (중복 비허용)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    # 암호화(해싱)된 비밀번호가 저장될 필드 (평문 저장 절대 금지)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    # 회원의 실명 혹은 닉네임 필드
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str | None] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())