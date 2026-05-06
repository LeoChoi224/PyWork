
-- null 값 과 연산 결과는 null 이다!
SELECT name, pay, bonus, pay + bonus
FROM t_professor;

-- IFNULL() : NULL값을 만나면 다른 값으로 치환해서 출력하는 함수
SELECT name, pay, bonus, ifnull(bonus, 0), pay + ifnull(bonus, 0)
FROM t_professor;

SELECT name, pay,
    ifnull(bonus, 0) as BONUS,
    pay * 12 + ifnull(bonus, 0) as 연봉
FROM t_professor
WHERE deptno = 101;
