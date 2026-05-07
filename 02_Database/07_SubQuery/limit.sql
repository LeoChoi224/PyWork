DROP TABLE IF EXISTS t_emp3;

-- CREATE TABLE t_emp3
-- AS
-- SELECT empno, name FROM t_emp2;

CREATE TABLE t_emp3(
	id INT PRIMARY KEY AUTO_INCREMENT,
	empno INT NOT NULL,
	name VARCHAR(10) NOT NULL
);

SELECT * FROM  t_emp3;

SELECT count(*) FROM t_emp3;

INSERT INTO t_emp3(empno, name)
SELECT empno, name FROM t_emp2;

INSERT INTO t_emp3(empno, name)
SELECT empno, name FROM t_emp3;

SELECT * FROM  t_emp3;

-- LIMIT n : SELECT 결과 첫 n개
SELECT * FROM  t_emp3 LIMIT 5;

-- LIMIT from, n : from 부터 n개   (from 은 index 0 부터 시작)
-- ↓만약 한 페이지당 5개씩 보여준다면..

SELECT * FROM t_emp3 LIMIT 0, 5;  -- 첫 페이지
SELECT * FROM t_emp3 ORDER BY id DESC LIMIT 0, 5;  -- 첫 페이지
SELECT * FROM t_emp3 ORDER BY id DESC LIMIT 5, 5;  -- 두번째 페이지



