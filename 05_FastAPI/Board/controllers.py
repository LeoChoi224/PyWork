from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc, select, func, update, delete
import models, database, schemas

router = APIRouter(prefix="/api")

# 목록  
# GET /api/board
@router.get("/board", response_model=list[schemas.PostResponse])
def get_posts(db: Session = Depends(database.get_db)):
    result = db.scalars(select(models.Post).order_by(desc(models.Post.regdate)))
    return result.all()

# 글 작성
# POST /api/board
@router.post("/board")
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db)):
    db_post = models.Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


# 특정 id 글 읽기
# GET /api/board/{id}
@router.get("/board/{id}", response_model=schemas.PostResponse)
def get_post(id: int, db: Session = Depends(database.get_db)):
    post = db.get(models.Post, id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # 조회수 증가
    post.viewcnt += 1
    db.commit()
    return post


# 특정 id 글 수정: id, subject, content 
# PUT /api/board/{id}
@router.put("/board/{id}")
def update_post(id: int, post_update: schemas.PostUpdate, db: Session = Depends(database.get_db)):
    db_post = db.get(models.Post, id)

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db_post.subject = post_update.subject
    db_post.content = post_update.content
    db.commit()

    return {"message": "Updated successfully"}

# 특정 id 글 삭제
# DELETE /api/board/{id}
@router.delete("/board/{id}")
def delete_post(id: int, db: Session = Depends(database.get_db)):
    db_post = db.get(models.Post, id)

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db.delete(db_post)
    db.commit()

    return {"message": "Deleted successfully"}
    