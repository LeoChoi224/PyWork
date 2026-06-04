# Base 클래스 정의, 모델 클래스 생성

from datetime import datetime
from typing import List, Optional
from sqlalchemy import (
    String, Integer, ForeignKey, Table, Column, DateTime, Text, func
)
from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column, relationship
)


class Base(DeclarativeBase):
    pass

# 게시글 좋아요 M:M 연결 테이블
post_likes = Table(
    "post_likes",
    Base.metadata,
    Column("member_id", ForeignKey("members.id", ondelete="CASCADE"), primary_key=True),
    Column("post_id", ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True),
    Column("created_at", DateTime, server_default=func.now(), nullable=False)
)

# 회원
class Member(Base):
    __tablename__ = "members"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)

    posts: Mapped[List["Post"]] = relationship(back_populates="author", cascade="all, delete-orphan")
    comments: Mapped[List["Comment"]] = relationship(back_populates="author", cascade="all, delete-orphan")

    liked_posts: Mapped[List["Post"]] = relationship(
        secondary=post_likes, back_populates="liked_by_members"
    )

# 게시글
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    view_cnt: Mapped[int] = mapped_column(Integer, server_default="0", default=0, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("members.id", ondelete="CASCADE"), nullable=False)

    author: Mapped["Member"] = relationship(back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship(back_populates="post", cascade="all, delete-orphan")
    
    liked_by_members: Mapped[List["Member"]] = relationship(
        secondary=post_likes, back_populates="liked_posts"
    )

# 댓글
class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(String(200), nullable=False) 
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False) 
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"), nullable=False) 
    author_id: Mapped[int] = mapped_column(ForeignKey("members.id", ondelete="CASCADE"), nullable=False) 

    post: Mapped["Post"] = relationship(back_populates="comments")
    author: Mapped["Member"] = relationship(back_populates="comments")