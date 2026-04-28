SELECT 'abcde', 100, 200, 300;

-- SELECT - 데이터 조회/질의
-- SELECT [컬럼명 또는 표현식] FROM [테이블명, 뷰명]

-- '모든 컬럼' 조회 : * 사용

SELECT * FROM t_emp;

SELECT empno, ename FROM t_emp;

SELECT ename, empno FROM t_emp;

SELECT ename, empno, ename, ename FROM t_emp;

-- 컬럼 별칭 (alias) 사용
SELECT
    studno "학생 학번", -- 별칭에 띄어씨기 있으면 쌍따옴표로 묶기
    name,
    jumin `use`, -- 일반적으로 키워드등은 사용불가. --> ` `으로 감싸서 이름 설정.
    deptno1 AS 제1전공
FROM
    t_student;

-- MySQL 에서 문자열 연결 concat()
SELECT 'aaa' + 'bbb';

SELECT CONCAT(name, `position`)
FROM t_professor;
SELECT CONCAT(name, '-', `position`, '-', `deptno`) 교수님목록
FROM t_professor;

