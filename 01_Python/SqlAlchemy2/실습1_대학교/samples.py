from databases import engine, SessionLocal
from models import Base, Department, Student, Professor, Course

# 예제를 위한 샘플 데이터 생성
def create_sample_data():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(engine)

    with SessionLocal() as db:
        # 학과
        cs = Department(name="컴퓨터공학과")
        ee = Department(name="전자공학과")
        math = Department(name="수학과")
        db.add_all([cs, ee, math])
        db.flush()

        # 교수
        prof_kim = Professor(name="김교수", department=cs)
        prof_lee = Professor(name="이교수", department=cs)
        prof_park = Professor(name="박교수", department=ee)
        prof_choi = Professor(name="최교수", department=math)
        db.add_all([prof_kim, prof_lee, prof_park, prof_choi])
        db.flush()

        # 과목
        c_python = Course(name="파이썬프로그래밍", credit=3, professor=prof_kim)
        c_db = Course(name="데이터베이스", credit=3, professor=prof_kim)
        c_algo = Course(name="알고리즘", credit=4, professor=prof_lee)
        c_circuit = Course(name="회로이론", credit=3, professor=prof_park)
        c_calc = Course(name="미적분학", credit=2, professor=prof_choi)
        c_os = Course(name="운영체제", credit=4, professor=prof_kim)  # 아무도 수강하지 않는 과목
        db.add_all([c_python, c_db, c_algo, c_circuit, c_calc, c_os])
        db.add_all([c_python, c_db, c_algo, c_circuit, c_calc])
        db.flush()

        # 학생
        s1 = Student(name="홍길동", grade=1, department=cs)
        s2 = Student(name="김철수", grade=2, department=cs)
        s3 = Student(name="이영희", grade=3, department=cs)
        s4 = Student(name="박민수", grade=2, department=ee)
        s5 = Student(name="정수진", grade=4, department=ee)
        s6 = Student(name="강지훈", grade=1, department=math)

        # 수강신청 (M:M)
        s1.courses = [c_python, c_db, c_calc]
        s2.courses = [c_python, c_algo]
        s3.courses = [c_db, c_algo, c_calc]
        s4.courses = [c_circuit, c_calc]
        s5.courses = [c_circuit, c_python]
        s6.courses = [c_calc]

        # c_python.students = [s2, s3, s4]
        db.add_all([s1, s2, s3, s4, s5, s6])                

        db.commit()
        print('샘플 데이터 생성 완료')


if __name__ == "__main__":
    create_sample_data()