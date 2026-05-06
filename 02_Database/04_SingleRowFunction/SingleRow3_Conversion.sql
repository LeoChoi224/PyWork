-- 데이터의 종류
-- 1) 숫자
-- 2) 문자
-- 3) 날짜/시간

-- MySQL 은 필요시 string -> number, 혹은 number -> string 으로 묵시적 형변환 수행

SELECT 1 + '1';


SELECT now(), year(now()), month(now()), day(now());

-- ################################################
-- 날짜 --> 원하는 포맷의 문자로 리턴
-- DATE_FORMAT() 함수
-- https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html

SELECT now(), date_format(now(), '%Y%m%d');
SELECT now(), date_format(now(), '%Y-%m-%d %H:%i:%s');

-- ################################################
-- format() 함수
-- 숫자 를 포맷팅하여 문자로 리턴
-- FORMAT(number, decimal_places)

-- 참조: https://www.w3schools.com/sql/func_mysql_format.asp

-- 숫자 세자리마다 콤마 찍기

SELECT 1234567, format(1234567, 0);

SELECT 250250.5634, format(250250.5634, 2);

SELECT * FROM t_professor;

SELECT name,
    hiredate 입사일,
    format(pay * 12 + IFNULL(bonus, 0), 0) 연봉,
    format((pay * 12 + IFNULL(bonus, 0)) * 1.1, 0) 인상후
FROM t_professor
WHERE YEAR(hiredate) < 2000;