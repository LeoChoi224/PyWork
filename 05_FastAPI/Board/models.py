from sqlalchemy import Integer, String, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database import Base

class Post(Base):
    __tablename__ = "r_post"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user: Mapped[str] = mapped_column(String(20), nullable=False, comment="게시글 작성자")   
    subject: Mapped[str] = mapped_column(String(200), nullable=False, comment="게시글 제목")
    content: Mapped[str] = mapped_column(Text, nullable=True, comment="게시글 내용")
    viewcnt: Mapped[int] = mapped_column(Integer, default=0, comment="게시글 조회수")
    regdate: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment="게시글 작성일시")