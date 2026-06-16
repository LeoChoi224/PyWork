from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, func, update, delete, desc
from database import get_db
from models import Post
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import PostResponse, PostCreate, PostUpdate

router = APIRouter(prefix="/board")

@router.get("/list", response_model=list[PostResponse])
async def list_posts(db: AsyncSession = Depends(get_db)):
    """목록: 게시글 목록 최신순"""
    stmt = select(Post).order_by(Post.created_at.desc(), Post.id.desc())
    result = await db.execute(stmt)
    return result.scalars().all()

@router.post("/write", status_code=status.HTTP_201_CREATED)
async def create_post(payload: PostCreate, db: AsyncSession = Depends(get_db)):
    """작성: 새 게시글 데이터 생성"""
    post = Post(user=payload.user, subject=payload.subject, content=payload.content)
    await db.add(post)
    await db.commit()
    return {"message": "게시글이 작성되었습니다.", "id": post.id}


@router.get("/detail/{id}", response_model=PostResponse)
async def get_update_post(id: int, db: AsyncSession = Depends(get_db)):
    """상세 조회: 특정 id 게시글 출력"""
    post = await db.get(Post, id)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 개시글을 찾을 수 없습니다.",
        )
    # 조회수 증가
    post.viewcnt += 1
    await db.commit()
    return post

@router.get("/read/{id}", response_model=PostResponse)
async def create_post(id: int, db: AsyncSession = Depends(get_db)):
    """상세 조회: 수정할 id 게시글 조회"""
    post = await db.get(Post, id)
    return post

@router.put("/update/{id}")
async def update_post(payload: PostUpdate, db: AsyncSession = Depends(get_db)):
    """수정: 특정 id 게시글 수정"""
    post = await db.get(Post, payload.id)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 개시글을 찾을 수 없습니다.",
        )
    post.user = payload.user
    post.subject = payload.subject
    post.content = payload.content
    await db.commit()
    return {"message": "게시글이 수정되었습니다."}


@router.delete("/delete/{id}")
async def delete_post(id: int, db: AsyncSession = Depends(get_db)):
    """삭제: id 게시글 삭제"""
    post = await db.get(Post, id)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 개시글을 찾을 수 없습니다.",
        )
    await db.delete(post)
    await db.commit()
    return {"message": "게시글이 삭제되었습니다."}