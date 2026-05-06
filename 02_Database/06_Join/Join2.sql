-- 비등가 조인 (Non-Equi Join)

-- #6201) 
-- t_customer 테이블, t_gift 테이블을 join 하여  
-- 고객의 마일리지 포인트별로 받을수 있는 상품을 조회하여 
-- 고객의 '이름(c_name)'과 포인트(c_point) 상품명(g_name)을 출력하세요
-- BETWEEN ~ AND ~ 사용

SELECT * FROM t_customer; -- 일단 함 보자
SELECT * FROM t_gift;

SELECT c.c_name "고객명", c.c_point "POINT", g.g_name "상품명"
FROM t_customer c, t_gift g
WHERE c.c_point BETWEEN g.g_start AND g.g_end
;
-- ANSI 구문
SELECT c.c_name "고객명", c.c_point "POINT", g.g_name "상품명"
FROM t_customer c JOIN t_gift g ON c.c_point BETWEEN g.g_start AND g.g_end
;

-- #6202
SELECT g.g_name "상품명", count(*) "필요수량"
FROM t_customer c, t_gift g
WHERE c.c_point BETWEEN g.g_start AND g.g_end
GROUP BY g.g_name
;

-- --------------------------------------------------------
-- -------------------------------------------------------
-- Outer Join
-- 지금까지의 JOIN 은 모두 INNER JOIN 이다.
SELECT s.name, p.name
FROM t_student s INNER JOIN t_professor p
ON s.profno  = p.PROFNO;

SELECT s.name, p.name
FROM t_student s LEFT OUTER JOIN t_professor p
ON s.profno  = p.PROFNO;

SELECT s.name, p.name
FROM t_student s RIGHT OUTER JOIN t_professor p
ON s.profno  = p.PROFNO;

-- MySQL 에는 Full outer 없슴.  대신 UNION 으로 구현 가능.
SELECT s.name, p.name
FROM t_student s LEFT OUTER JOIN t_professor p
ON s.profno  = p.PROFNO
UNION
SELECT s.name, p.name
FROM t_student s RIGHT OUTER JOIN t_professor p
ON s.profno  = p.PROFNO;


-- -----------------------------------------------------------------
-- ----------------------------------------------
-- self join

-- #6209) 
-- t_dept2 테이블에서 
-- 부서명 과 그 부서의 상위부서명을 출력하세요
SELECT * FROM t_dept2;

SELECT d1.dname "부서명", d2.dname "상위부서명"
FROM t_dept2 d1, t_dept2 d2
WHERE d1.pdept = d2.dcode
;