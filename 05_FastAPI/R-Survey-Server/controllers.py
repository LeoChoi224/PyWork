from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from models import Survey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from schemas import SurveyCreate, SurveyResponse, SurveyUpdate

router = APIRouter(prefix="/survey")

@router.get("/list", response_model=list[SurveyResponse])
async def list_surveys(db: AsyncSession = Depends(get_db)):
    """목록"""
    stmt = select(Survey).order_by(Survey.created_at.desc(), Survey.id.desc())
    result = await db.execute(stmt)
    return result.scalars().all()


@router.post("/write", status_code=status.HTTP_201_CREATED)
async def create_survey(payload: SurveyCreate, db: AsyncSession = Depends(get_db)):
    """작성"""
    survey = Survey(
        name=payload.name,
        age=payload.age,
        gender=payload.gender,
        area=payload.area,
        favorite=payload.favorite
    )
    db.add(survey)
    await db.commit()
    await db.refresh(survey)  # DB에서 자동 생성된 id 및 created_at을 로드
    return survey


@router.get("/detail/{id}", response_model=SurveyResponse)
async def get_survey(id: int, db: AsyncSession = Depends(get_db)):
    """상세"""
    survey = await db.get(Survey, id)
    if survey is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 설문을 찾을 수 없습니다.",
        )
    return survey


@router.put("/update", response_model=SurveyResponse)
async def update_survey(payload: SurveyUpdate, db: AsyncSession = Depends(get_db)):
    """수정"""
    survey = await db.get(Survey, payload.id)
    if survey is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 설문을 찾을 수 없습니다.",
        )
    survey.gender = payload.gender
    survey.area = payload.area
    survey.favorite = payload.favorite
    await db.commit()
    await db.refresh(survey)
    return survey


@router.delete("/delete/{id}")
async def delete_survey(id: int, db: AsyncSession = Depends(get_db)):
    """삭제"""
    survey = await db.get(Survey, id)
    # if survey is None:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail="해당 설문을 찾을 수 없습니다.",
    #     )
    if survey is None:
        return 0
    await db.delete(survey)
    await db.commit()
    return 1