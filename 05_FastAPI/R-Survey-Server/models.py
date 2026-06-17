from sqlalchemy import Integer, String, DateTime, func, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database import Base

class Survey(Base):
    """설문조사 모델"""
    __tablename__ = "r_survey"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False, comment="이름")
    age: Mapped[int] = mapped_column(Integer, nullable=False, comment="나이")
    gender: Mapped[str] = mapped_column(String(10), nullable=False, server_default="MALE", comment="성별")
    area: Mapped[str] = mapped_column(String(100), nullable=False, comment="거주지역")
    favorite: Mapped[str] = mapped_column(String(100), nullable=False, comment="이상형(들)")

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment="작성일")

    # 제약조건: 나이가 0 이상이어야 함
    __table_args__ = (
        CheckConstraint('age >= 0', name='check_age_non_negative'),
    )

    def __repr__(self):
        return f"<Survey id={self.id} name={self.name}>"