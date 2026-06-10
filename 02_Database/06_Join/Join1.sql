
-- From 절의 테이블에 별칭(alias) 가능

SELECT s.studno, s.name, s.deptno1
FROM t_student s
;

SELECT d.deptno, d.dname
FROM t_department d;

-- 카티션곱 (Cartesian Product)
-- 두개의 테이블을 JOIN 하게 되면, 
-- 각 테이블의 레코드들의 모든 조합이 출력된다.
-- WHERE 나 ON 등으로 JOIN 조건이 주어지지 않으면 
-- 모든 카티션곱이 출력된다. 

-- 20 x 12 = 240 레코드

SELECT s.studno, s.name, s.deptno1, d.deptno, d.dname
FROM t_student s, t_department d
;

-- ---------------------------------------------------------------------------------
-- Equi Join (등가 Join)
-- 일반적으로 많이 쓰이는 Join 이며, 양쪽 테이블 Join 한 카티션곱에서 ‘같은조건’이 존재할 경우만 값을 가져오는 것

-- 예)  #6101 
-- t_student 테이블과 t_department 테이블을 사용하여 학생이름, 1전공 학과번호, 1전공 학과 이름을 출력하세요

-- MySQL 구문
SELECT s.name 학생이름, s.deptno1 학과번호, d.dname 학과이름
FROM t_student s, t_department d
WHERE s.deptno1 = d.deptno  -- JOIN 조건
;

-- ANSI SQL 구문 (표준 SQL)
SELECT s.name 학생이름, s.deptno1 학과번호, d.dname 학과이름
FROM t_student s JOIN t_department d ON s.deptno1 = d.deptno  -- JOIN 조건
;

-- 제2전공 
-- ⭐️null 값은 JOIN 조건에 참여 안함.
SELECT s.name 학생이름, s.deptno2 제2학과번호, d.dname 제2학과이름
FROM t_student s JOIN t_department d ON s.deptno2 = d.deptno  -- JOIN 조건
;

-- 연습  #6102)
-- t_student 테이블, t_professor 테이블 을 join하여
-- ‘학생이름’, ‘지도교수번호’, ‘지도교수이름’ 을 출력하세요

-- MySQL 구문
SELECT s.name 학생이름, s.profno 지도교수, p.name 지도교수이름
FROM t_student s, t_professor p
WHERE s.profno = p.profno
ORDER BY s.profno ASC
;

-- ANSI 구문
SELECT s.name 학생이름, s.profno 지도교수, p.name 지도교수이름
FROM t_student s JOIN t_professor p ON s.profno = p.profno
ORDER BY s.profno ASC
;

-- 3테이블 JOIN

--  #6103
-- t_student, t_department, t_professor 테이블 을 join 하여 
--  학생의 이름, 1학과이름, 지도교수 이름  을 출력하세요

-- 3개 테이블 join  MySQL 구문
-- MySQL 구문
SELECT s.name 학생이름, d.dname 학과이름, p.name 교수이름
FROM t_student s, t_department d, t_professor p
WHERE s.deptno1 = d.deptno AND s.profno = p.profno -- JOIN 조건
;

-- ANSI 구문
SELECT
    s.name 학생이름, d.dname 학과이름, p.name 교수이름
FROM
    t_student s
    JOIN t_department d ON s.deptno1 = d.deptno
    JOIN t_professor p ON s.profno = p.profno
;

-- 연습  #6105
-- t_student - t_professor 테이블 join 하여
-- 제1전공(deptno1) 이 101번인 학생들의
-- 학생이름과 지도교수 이름을 출력하세요

-- MySQL 구문
SELECT
    s.name 학생이름, p.name 교수이름
FROM
    t_student s, t_professor p
WHERE
    s.profno = p.profno AND s.deptno1 = 101
;

-- ANSI 구문
SELECT
    s.name "학생이름", p.name "교수이름" 
FROM
    t_student s
    JOIN t_professor p
        ON s.profno = p.profno 
        -- AND s.deptno1 = 101
WHERE s.deptno1 = 101
;

