from sqlalchemy import Integer, String, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database import Base

class Book(Base):
    """도서 모델"""
    __tablename__ = "r_book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False, comment="도서 제목")   
    author:Mapped[str] = mapped_column(String(40), nullable=False, comment="도서 저자")

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), comment="도서 등록 일시")