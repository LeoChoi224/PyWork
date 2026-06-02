# Base 클래스 정의, 모델 클래스 생성

from typing import List
from sqlalchemy import (
    String, Integer, ForeignKey, CheckConstraint, Table, Column
)
from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column, relationship
)


class Base(DeclarativeBase):
    pass

# 학생-과목  M:M 연결 테이블
student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("students.id", ondelete="CASCADE"), primary_key=True),
    Column("course_id", ForeignKey("courses.id", ondelete="CASCADE"), primary_key=True),
)

# 학과
class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)

    students: Mapped[List["Student"]] = relationship(back_populates="department")
    professors: Mapped[List["Professor"]] = relationship(back_populates="department")

# 학생
class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    grade: Mapped[int] = mapped_column(Integer) 
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"), nullable=False) 

    __table_args__ = (
        CheckConstraint("grade >= 1 AND grade <= 4", name="ck_student_grade"), 
    )

    department: Mapped["Department"] = relationship(back_populates="students") 
    courses: Mapped[List["Course"]] = relationship(
        secondary=student_course, back_populates="students"
    ) 

# 교수
class Professor(Base):
    __tablename__ = "professors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"), nullable=False) 

    department: Mapped["Department"] = relationship(back_populates="professors")  
    courses: Mapped[List["Course"]] = relationship(back_populates="professor")

# 과목
class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    credit: Mapped[int] = mapped_column(Integer)
    professor_id: Mapped[int] = mapped_column(ForeignKey("professors.id"), nullable=False)

    __table_args__ = (
        CheckConstraint("credit >= 1 AND credit <= 5", name="ck_course_credit"),
    )


    professor: Mapped["Professor"] = relationship(back_populates="courses")

    students: Mapped[List["Student"]] = relationship(
        secondary=student_course, back_populates="courses"
    )



