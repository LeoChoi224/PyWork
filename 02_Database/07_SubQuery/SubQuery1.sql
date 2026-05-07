-- --------------------------------------
-- Sub Query

-- #7101
-- t_emp 테이블에서 
-- scott 보다 급여를 많이 받는 사람의 이름과 급여 출력

-- scott 의 급여
SELECT sal FROM t_emp WHERE ename = 'SCOTT';

SELECT ename, sal FROM t_emp
WHERE sal > (SELECT sal FROM t_emp WHERE ename = 'SCOTT')
;


SELECT * FROM t_professor;
SELECT * FROM t_department;
-- #7104) 연습
--t_professor, t_department 테이블 :
--입사일이 송도권 교수보다 나중에 입사한 사람의
--이름과 입사일, 학과명을 출력하세요
SELECT
    p.name, p.hiredate, d.dname
FROM
    t_professor p
    JOIN t_department d
        ON p.deptno = d.deptno
WHERE
    p.hiredate > (SELECT hiredate FROM t_professor WHERE name = "송도권")
;

-- 2. 다중행 서브쿼리
-- Sub Query 결과가 2건 이상 출력되는 것을 말합니다.
-- 다중행 Sub Query 와 함께 사용하는 연산자
--		 IN 같은 값을 찾음
--		>ANY 최소값을 반환함 (서브쿼리 결과중 가장작은것보다 큰)
--		<ANY 최대값을 반환함 (서브쿼리 결과중 가장큰것보다 작은)
--		<ALL 최소값을 반환함 (서브쿼리 결과중 가장작은것보다 작은)
--		>ALL 최대값을 반환함 (서브쿼리 결과중 가장큰것보다 큰)
--		EXIST Sub Query 값이 있을 경우 반환

-- #7107) 예제
-- t_emp2, t_dept2 테이블 : 
-- 근무지역 (t_dept2.area) 이 서울 지사인 모든 사원들의 
-- 사번(empno)과 이름(name), 부서번호(deptno)를 출력하세요

SELECT * FROM t_emp2;
SELECT * FROM t_dept2;

-- 근무지역이 '서울지사' 인 부서들
SELECT dcode FROM t_dept2 WHERE area = '서울지사';

SELECT empno, name, deptno
FROM t_emp2
-- WHERE deptno = (SELECT dcode FROM t_dept2 WHERE area = '서울지사')
WHERE deptno IN (SELECT dcode FROM t_dept2 WHERE area = '서울지사')
;


-- #7108) 연습
-- t_emp2 테이블 :
-- 전체직원중 과장 직급의 최소연봉자보다
-- 연봉이 높은 사람의
-- 이름(name)과 직급(post), 연봉(pay)을 출력하세요.  
-- 단, 연봉 출력 형식은 천 단위 구분 기호와 원 표시를 하세요

SELECT pay FROM t_emp2 WHERE post = '과장';

SELECT
	name "이름", 
	post "직급",
	concat(format(pay, 0), '원') "연봉"
FROM t_emp2
WHERE pay >ANY (SELECT pay FROM t_emp2 WHERE post = '과장')
;

-- 이렇게 해도 된다
SELECT min(pay) FROM t_emp2 WHERE post = '과장';

SELECT
	name "이름", 
	post "직급",
	concat(format(pay, 0), '원') "연봉"
FROM t_emp2
WHERE pay > (SELECT min(pay) FROM t_emp2 WHERE post = '과장')
;


"""실습"""
-- #7110) 연습
-- t_emp2, t_dept2 테이블 : 
-- 각 부서별 평균 연봉을 구하고 그 중에서 평균 연봉이 가장 적은 부서의 평균연봉보다 
-- 적게 받는 직원들의 부서명, 직원명, 연봉을 출력 하세요

SELECT deptno, avg(pay) FROM t_emp2 GROUP BY deptno;

SELECT
    d.dname, e.name, e.pay
FROM
    t_emp2 e
    JOIN t_dept2 d
        ON e.deptno = d.dcode
WHERE
    e.pay <ALL (SELECT avg(pay) FROM t_emp2 GROUP BY deptno)
ORDER BY e.pay
;
