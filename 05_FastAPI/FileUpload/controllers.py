# 파일 처리 비즈니스 로직 및 REST API 엔드포인트를 정의. 
# 파일 저장, 용량 검증, 파일 조회 및 스트리밍 다운로드가 이루어집니다.

import os
import uuid
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from fastapi.responses import FileResponse
from models import UploadedFile
from schemas import FileApiResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

# ---------------------------------------------------------------------------
# 라우터 객체 생성
# ---------------------------------------------------------------------------
# prefix="/api/files" 설정을 통해 이 라우터 안의 모든 URL 경로 앞에 공통 주소가 붙습니다.
router = APIRouter(prefix="/api/files", tags=["files"])

# ---------------------------------------------------------------------------
# 설정 변수 (Configuration)
# : 업로드 경로 및 제한 용량 (2MB)
# ---------------------------------------------------------------------------
# - UPLOAD_DIR: 프로젝트 루트 하위의 'upload' 폴더를 절대 경로로 계산하여 지정합니다.
# - MAX_FILE_SIZE: 업로드 가능한 최대 파일 용량을 바이트(Byte) 단위로 정의합니다. (2MB = 2 * 1024 * 1024)
UPLOAD_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "upload"
)
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# ---------------------------------------------------------------------------
# [POST] /api/files/upload : 파일 및 설명 업로드 API
# ---------------------------------------------------------------------------
@router.post("/upload", response_model=FileApiResponse)
async def upload_file(
    title: str, file: UploadFile, 
    db: Session = Depends(get_db)
):
    """파일 및 설명 업로드 API"""

    # 1. 파일 용량 체크
    file.file.seek(0, os.SEEK_END)  # 파일의 끝 byte
    file_size = file.file.tell()  # 파일의 끝이 몇번째 byte => 용량
    file.file.seek(0)  # 파일의 첫 바이트로 file pointer 이동

    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400, detail="파일 용량은 2MB를 초과할 수 없습니다."
            #    400: Bad Request
        )

    # 2. 파일명 중복 방지를 위한 Rename 처리
    ext = os.path.splitext(file.filename)[1]  # splittext() => 파일명과 확장자를 스플릿, 파일의 확장자 ".jpg", ".docx" 
    unique_filename = f"{uuid.uuid4().hex}{ext}"  # 고유한 파일명 생성
    file_path = os.path.join(UPLOAD_DIR, unique_filename)  # 저장될 파일경로

    # 3. 로컬 서버에 파일 저장
    try:
        with open(file_path, 'wb') as f:
            content = await file.read()  # UploadFile 객체는 async 함수에서는 비동기로 동작
            f.write(content)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"파일 저장중 오류가 발생했습니다: {str(e)}"
        )

    # 4. 데이터베이스에 기록 저장 (SQLAlchemy 2.0)
    db_file = UploadedFile(
        title=title,
        original_name=file.filename,
        uploaded_name=unique_filename,
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)

    return db_file
    

# ---------------------------------------------------------------------------
# [GET] /api/files : 업로드된 파일 전체 목록 조회 API
# ---------------------------------------------------------------------------
@router.get("", response_model=list[FileApiResponse])
def get_files(db: Session = Depends(get_db)):
    """업로드된 파일 전체 목록 조회 API"""
    stmt = select(UploadedFile).order_by(UploadedFile.id.desc())
    result = db.scalars(stmt).all()
    return result

# ---------------------------------------------------------------------------
# [GET] /api/files/download/{file_id} : 안전한 파일 다운로드 API (원본 파일명 복원)
# ---------------------------------------------------------------------------
@router.get("/download/{file_id}")
def download_file(file_id: int, db: Session = Depends(get_db)):
    """파일 다운로드 API (원본 파일명 복원)"""

    # 데이터베이스에서 ID에 해당하는 파일 정보 검색
    stmt = select(UploadedFile).where(UploadedFile.id == file_id)
    db_file = db.scalar(stmt)

    if not db_file:
        raise HTTPException(
            status_code=404, detail="파일을 찾을 수 없습니다."
        )

    # 물리적인 파일 존재 여부 재검증
    file_path = os.path.join(UPLOAD_DIR, db_file.uploaded_name)
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404, detail="서버에 실제 파일이 존재하지 않습니다."
        )

    # FastAPI의 FileResponse 객체를 사용해 파일 스트림 전송
    # - filename=db_file.original_name: 다운로드 시 서버에 저장된 무작위 UUID명이 아닌 
    #   사용자가 최초에 올렸던 원본 이름으로 브라우저에 저장되도록 Content-Disposition 헤더를 세팅합니다.
    return FileResponse(
        path=file_path,
        filename=db_file.original_name,  # 원본 이름으로 다운로드되게 처리
        media_type="application/octet-stream",  # 일반적인 바이트 스트림
    )

# ---------------------------------------------------------------------------
# [GET] /api/files/view/{file_id} : 이미지 보기용 파일 스트리밍 API (팝업 전용)
# ---------------------------------------------------------------------------
@router.get("/view/{file_id}")
def view_file(file_id: int, db: Session = Depends(get_db)):
    """이미지 보기용 파일 스트리밍 API"""
    
    # 파일 다운로드와 로직은 유사하지만, 브라우저가 강제 다운로드하지 않고 
    # 브라우저 내부 화면(모달 창 등)에 직접 렌더링할 수 있도록 돕는 엔드포인트입니다.
    stmt = select(UploadedFile).where(UploadedFile.id == file_id)
    db_file = db.scalar(stmt)

    if not db_file:
        raise HTTPException(
            status_code=404, detail="파일을 찾을 수 없습니다."
        )

    file_path = os.path.join(UPLOAD_DIR, db_file.uploaded_name)

    # 물리적인 파일 존재 여부 재검증
    file_path = os.path.join(UPLOAD_DIR, db_file.uploaded_name)
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404, detail="서버에 실제 파일이 존재하지 않습니다."
        )    
    
    # filename 매개변수를 제외하고 전송함으로써 브라우저가 다운로드 창을 띄우지 않고 
    # 파일 자체를 인라인 스트리밍 형태로 읽어가게(렌더링하게) 만듭니다    
    return FileResponse(path=file_path)