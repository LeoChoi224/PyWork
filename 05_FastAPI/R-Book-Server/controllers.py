from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import desc
import models, database, schemas
from sqlalchemy import select, func, update, delete
from database import get_db
from models import Book
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import BookCreate, BookResponse, BookUpdate

router = APIRouter(prefix="/book")

# 목록
@router.get("", response_model=list[BookResponse])
async def list_books(db : AsyncSession = Depends(get_db)):
    """목록: 도서목록 최신순"""
    stmt = select(Book).order_by(Book.created_at.desc(), Book.id.desc())
    result = await db.execute(stmt)
    return result.scalars().all()

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_book(payload: BookCreate, db: AsyncSession = Depends(get_db)):
    """작성: 새 도서 데이터 생성"""
    book = Book(title=payload.title, author=payload.author)
    db.add(book)
    await db.commit()
    return {"message": "도서가 작성되었습니다.", "id": book.id}

@router.get("/{id}", response_model=BookResponse)
async def get_book(id: int, db: AsyncSession = Depends(get_db)):
    """상세조회: 특정 id 도서 출력"""
    book = await db.get(Book, id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 도서를 찾을 수 없습니다.",
        )
    return book

@router.put("")
async def update_book(payload: BookUpdate, db: AsyncSession = Depends(get_db)):
    """수정: 주어진 id 도서의 title, author 수정"""
    book = await db.get(Book, payload.id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 도서를 찾을 수 없습니다.",
        )
    book.title = payload.title
    book.author = payload.author
    await db.commit()
    return {"message": "도서가 수정되었습니다."}

@router.delete("/{id}")
async def delete_book(id: int, db: AsyncSession = Depends(get_db)):
    """삭제: 주어진 id 도서 삭제"""
    book = await db.get(Book, id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 도서를 찾을 수 없습니다.",
        )
    await db.delete(book)
    await db.commit()
    return {"message": "도서가 삭제되었습니다."}