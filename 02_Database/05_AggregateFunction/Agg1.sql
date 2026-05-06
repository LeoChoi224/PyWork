SELECT count(*) FROM t_professor;
SELECT count(pay), sum(pay), avg(pay), min(pay), max(pay) FROM t_professor;
-- 그룹함수에서 집계할때 null 값은 (기본적으로) 계산에서 제외
SELECT count(bonus), sum(bonus), avg(bonus), min(bonus), max(bonus) FROM t_professor;


SELECT avg(bonus), avg(ifnull(bonus, 0)) FROM t_professor;

-- t_professor 테이블에서 '학과별'로 교수들의 평균 급여를 출력하세요
SELECT * FROM t_professor;

-- 💥에러 
-- SELECT 절에 그룹함수 아닌 것과 그룹함수는 같이 올수는 없다.  이 경우 그룹함수가 아닌 것들은 GROUP BY 로 묶여야 할 것이다.
-- SELECT deptno, avg(pay) FROM t_professor;
SELECT deptno, avg(pay) FROM t_professor
GROUP BY deptno
;

-- #5101)연습
-- t_professor 테이블 : 학과별(deptno) 그리고 직급별(position)로 교수들의 평균 급여를 계산하여 출력하세요
SELECT deptno, position, format(avg(pay), 0) FROM t_professor
GROUP BY deptno, position
ORDER BY deptno ASC, position ASC
;

-- HAVING : 그룹 함수에 조건 추가
-- 학과별 평균급여를 출력하되, 평균급여가 300 보다 많은 학과만 출력
SELECT deptno, avg(pay) FROM t_professor
-- WHERE avg(pay) > 300  -- 그룹함수는 WHERE 절에서 사용 불가!
GROUP BY deptno
HAVING avg(pay) > 300
;

-- <SELECT 문 순서>
-- SELECT
-- FROM
-- WHERE
-- GROUP BY
-- HAVING
-- ORDER BY

SELECT deptno, avg(pay) 평균급여 FROM t_professor
GROUP BY deptno
HAVING 평균급여 > 300 -- MySQL 에선 SELECT 문에서 지정한 별명을 HAVING 에서 사용 가능.
;

SELECT deptno1 학과, max(weight) - min(weight) 최대최소몸무게차
FROM t_student
GROUP BY deptno1
-- HAVING 최대최소몸무게차 >= 30
;

-- #5103
-- SELECT deptno,
--     count(deptno) 총인원,
--     avg(now() - hiredate) 근속평균,
--     avg(pay) 급여평균,
--     avg(IFNULL(bonus, 0)) 보너스평균
-- FROM t_professor
-- GROUP BY deptno
-- ;