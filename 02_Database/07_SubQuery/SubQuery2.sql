-- 스칼라 서브쿼리

SELECT (SELECT 10), (SELECT '홍묵')
;

SELECT e.name "사원이름", (SELECT d.dname FROM t_dept2 d WHERE e.deptno = d.dcode) "부서이름"
FROM t_emp2 e
;

"""실습"""
--  #7207) 예제
-- t_student, t_department 테이블 사용
-- 학생이름, 아이디, 학년, 제1전공 이름, 제2전공 이름이 나오게 하세요 (
-- 출력되게 하세요

SELECT * FROM t_student;

SELECT * FROM t_department;

SELECT
    s.name, s.id, s.grade,
    (SELECT d.dname
    FROM t_department d
    WHERE s.deptno1 = d.deptno
    ) "dname",
    IFNULL((
        SELECT d.dname
        FROM t_department d 
        WHERE s.deptno2 = d.deptno) , ''
    ) "dname2"
FROM
    t_student s
;