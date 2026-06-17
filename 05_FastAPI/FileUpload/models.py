from datetime import datetime
from database import Base
from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

# ---------------------------------------------------------------------------
# UploadedFile: 데이터베이스 테이블과 매핑되는 ORM 모델 클래스
# ---------------------------------------------------------------------------
class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    title: Mapped[str] = mapped_column(String(30), nullable=False)  # 파일 설명
    original_name: Mapped[str] = mapped_column(String(100), nullable=False) # 원본 파일명
    uploaded_name: Mapped[str] = mapped_column(String(100), nullable=False) # 저장된 파일명

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )