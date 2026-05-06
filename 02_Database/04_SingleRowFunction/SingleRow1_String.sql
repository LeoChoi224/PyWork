-- -------------------------------------------
-- SUBSTR 함수
-- 구문: SUBSTR( '문자열' 또는 컬럼명,   시작위치,  추출할 글자수 )
-- 문자열에서 특정 길이의 문자를 추출할 때 사용하는 함수
-- 시작위치, 음수 가능.
-- ★ 시작 인덱스가 1부터 시작한다 (인덱스는 1부터 시작)

SELECT name,
    substr(name, 2), -- name 컬럼값 2번째 문자부터
    jumin,
    substr(jumin, 1, 6) -- jumin 컬럼값 1번째 6글자
FROM t_student;

-- -----------------------------------------------
-- INSTR()
-- 주어진 문자열이나 컬럼에서 특정 글자의 위치를 찾아주는 함수 (인덱스 리턴)


SELECT name, tel, instr(tel, ')')
FROM t_student;

SELECT name, tel, substr(tel, 1, instr(tel, ')') - 1) 지역번호
FROM t_student
WHERE deptno1 = 101;
