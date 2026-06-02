# main.py
from sqlalchemy import select, func
from databases import SessionLocal
from models import Department, Student, Professor, Course, student_course


def courses_of_student(db, student_id: int):
    """특정 학생이 수강하는 과목 목록"""
    # 방법 1
    # stmt = (
    #     select(Course)
    #     .join(student_course, Course.id == student_course.c.course_id)
    #     .where(student_course.c.student_id == student_id)
    # )
    # return db.scalars(stmt).all()

    # 방법 2
    student = db.get(Student, student_id)
    return student.courses if student else []

def professors_of_department(db, department_id: int):
    """특정 학과에 소속된 교수 목록"""
    # 방법 1
    # stmt = select(Professor).where(Professor.department_id == department_id)
    # return db.scalars(stmt).all()

    # 방법 2
    department = db.get(Department, department_id)
    return department.professors if department else []


def department_of_professor(db, professor_id: int):
    """특정 교수의 학과 정보"""
    # 방법 1
    # stmt = (
    #     select(Department)
    #     .join(Professor, Department.id == Professor.department_id)
    #     .where(Professor.id == professor_id)
    # )
    # return db.scalar(stmt)

    # 방법 2
    prof = db.get(Professor, professor_id)
    return prof.department if prof else None

def department_of_student(db, student_id: int):
    """특정 학생의 학과 정보"""
    # 방법 1
    # stmt = (
    #     select(Department)
    #     .join(Student, Department.id == Student.department_id)
    #     .where(Student.id == student_id)
    # )
    # return db.scalar(stmt)

    # 방법 2
    student = db.get(Student, student_id)
    return student.department if student else None

def students_of_course(db, course_id: int):
    """특정 과목을 수강하는 학생 목록"""
    course = db.get(Course, course_id)
    return course.students if course else []

def student_count_per_course(db):
    """과목별 수강 학생 수"""
    stmt = (
        select(Course.name, func.count(student_course.c.student_id))
        .outerjoin(student_course, Course.id == student_course.c.course_id)
        .group_by(Course.id)
    )
    return db.execute(stmt).all()


def departments_of_grade(db, grade: int):
    """특정 학년의 학생들이 소속된 학과 (중복 제거)"""
    stmt = (
        select(Department)
        .join(Student, Student.department_id == Department.id)
        .where(Student.grade == grade)
    )
    return db.scalars(stmt).all()


if __name__ == "__main__":
    with SessionLocal() as db:
        # print("== 학생 1이 수강하는 과목 ==")
        # for c in courses_of_student(db, 1):
        #     print(f"  {c.name} ({c.credit}학점)")

        # print("\n== 학과 1 소속 교수 ==")
        # for p in professors_of_department(db, 1):
        #     print(f"  {p.name}")

        # print("\n== 교수 3의 학과 ==")
        # d = department_of_professor(db, 3)
        # print(f"  {d.name if d else '없음'}")

        # print("\n== 학생 1의 학과 ==")
        # d = department_of_student(db, 1)
        # print(f"  {d.name if d else '없음'}")

        # print("\n== 과목 1을 수강하는 학생 ==")
        # for s in students_of_course(db, 1):
        #     print(f"  {s.name} ({s.grade}학년)")

        # print("\n== 과목별 수강 학생 수 ==")
        # for name, cnt in student_count_per_course(db):
        #     print(f"  {name}: {cnt}명")

        print("\n== 2학년 학생들이 소속된 학과 ==")
        for d in departments_of_grade(db, 2):
            print(f"  {d.name}")