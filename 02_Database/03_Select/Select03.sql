-- t_student 테이블에서 키(height)가 180 보다 크거나 같은 사람 이름, 키 출력
SELECT name, height FROM t_student WHERE height >= 180;

-- t_student 테이블에서 몸무게(weight)가 
-- 60~80 인 사람의 이름과 체중 출력
SELECT name, weight FROM t_student WHERE weight BETWEEN 60 AND 80;

-- t_student 테이블에서는 제1전공이 101번 학과(deptno1) 학생과 201번 학과 학생들을 모두 출력하세요 (in 연산자 활용)
SELECT * FROM t_student WHERE deptno1 IN (101, 201);

-- t_student 테이블에서 성이 ‘김’ 씨인 사람 조회
-- LIKE 연산자 사용:  
SELECT * FROM t_student WHERE name LIKE '김%';

-- t_student 테이블에서 4학년 학생중에 키 가 170cm 이상인 사람의 
-- '이름'과 '학년'과 '키'를 조회하세요
SELECT
    name, grade, height
FROM
    t_student
WHERE
    grade = 4 AND height >= 170;

-- t_student 테이블에서 1학년이거나 또는 몸무게가 80kg 이상인 학생들의 
-- '이름'과 '키'와 '학년'과 '몸무게'를 출력하세요
SELECT
    name, grade, height, weight
FROM
    t_student
WHERE
    grade = 1 OR weight >= 80;

-- t_student 테이블을 사용해서 2학년 중에서 키가 180cm 보다 크면서 
-- 몸무게가 70kg 보다 큰 학생들의 
-- 이름과 학년과 키와 몸무게를 출력하세요
SELECT
    name, grade, height, weight
FROM
    t_student
WHERE
    grade = 2 AND height > 180 AND weight > 70;

-- t_student 테이블: 2학년 학생중에서 키가 180cm보다 크거나 
-- 또는 몸무게가 70kg 보다 큰 학생들의 
-- 이름과 학년과 키와 몸무게를 출력하세요
SELECT
    name, grade, height, weight
FROM
    t_student
WHERE
    grade = 2 AND height > 180 OR weight > 70;

-- t_emp 테이블에서 고용일(hiredate)이 1992년 이전인 사람들의 
-- 이름(ename) 과 고용일을 출력하세요
SELECT ename, hiredate FROM t_emp WHERE hiredate < '1992-01-01 00:00:00';

-- t_student 테이블: 1학년 학생의 이름과 생일과 키와 몸무게를 출력하세요, 
-- 단 생일이 빠른 사람 순서대로 정렬하세요.
SELECT
    name, birthday, height, weight
FROM
    t_student
WHERE
    grade = 1
ORDER BY
    birthday;

-- student 테이블: 1학년 학생의 이름과 키를 출력하세요, 
-- 별명은 ‘이름’, ‘키’ 로 출력.  
-- 단 이름은 오름차순으로 정렬하세요
SELECT
    name 이름,
    height 키
FROM
    t_student
WHERE
    grade = 1
ORDER BY
    name
;

SELECT name 이름, height 키, grade
FROM t_student
ORDER BY grade DESC, name ASC;  -- 정렬조건 복수개 가능

-- t_emp2 직원 테이블에서
-- 생일(birthday) 가 1980년대생인 사람들의 이름과 생일만 출력하세요
-- 즉 1980/01/01 ~ 1989/12/31
SELECT name, birthday FROM t_emp2 WHERE birthday LIKE '198%';


-- -----------------------------------------------------
-- WHERE 조건절에 1 = 1 으로 시작하면
-- 이후의 AND 조건들을 유연하게 작성할수 있다. (추가, 삭제 등이 용이)

SELECT * FROM t_student
WHERE
    1 = 1
    AND grade = 3
    AND deptno1 = 101
