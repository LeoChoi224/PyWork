-- 제약조건 (Constraint)
-- 테이블 생성시 동시에 설정하기 

-- MySQL 에서 Table 의 제약조건 확인 
-- SELECT * FROM Information_schema.table_constraints WHERE table_schema='db이름';
-- SELECT * FROM Information_schema.table_constraints WHERE table_schema='db이름' AND table_name="table이름";

SELECT * FROM Information_schema.table_constraints 
WHERE table_schema='db2604' AND table_name="t_emp4";

DROP TABLE IF EXISTS t_emp4;
CREATE TABLE t_emp4 (
    no INT PRIMARY KEY,  -- PK
    name VARCHAR(10) NOT NULL, -- NN
    jumin VARCHAR(13) NOT NULL UNIQUE, -- NN, UQ
    area INT CHECK(area < 5), -- CK
    deptno VARCHAR(6) REFERENCES t_dept2(dcode) -- FK
);

-- MySQL 은 NN 에 대한 내용은 제약조건으로 다루지 않고 컬럼의 속성으로 다룬다.


-- 별도의 항목으로도 정의 가능.
DROP TABLE IF EXISTS t_emp4;
CREATE TABLE t_emp4 (
    no INT,  -- PK
    name VARCHAR(10) NOT NULL, -- NN
    jumin VARCHAR(13) NOT NULL, -- NN, UQ
    area INT, -- CK
    deptno VARCHAR(6), -- FK
    CONSTRAINT emp4_no_pk PRIMARY KEY(no), -- 제약조건의 이름 설정
    CONSTRAINT emp4_jumin_uk UNIQUE(jumin),
    CONSTRAINT emp4_area_ck CHECK(area < 5),
    CONSTRAINT emp4_deptno_fk FOREIGN KEY (deptno) REFERENCES t_dept2(dcode)
);

-- 제약조건에 위배되는 DML
INSERT INTO t_emp4 VALUES(
	1, 'MySQL', '1234561234567', 4, 1000
); -- 두번 실행하면 오류 

INSERT INTO t_emp4 VALUES(
	2, '오라클', '1234561234567', 4, 1000
); -- UK 위배


INSERT INTO t_emp4 VALUES(
	2, '오라클', '22222222222222222222222222', 4, 1000
); -- vARCHAR(13) 초과!

INSERT INTO t_emp4 VALUES(
	2, '오라클', '2222222222222', 10, 1000
);  -- CK 위배

SELECT dcode FROM t_dept2;

INSERT INTO t_emp4 VALUES(
	2, '오라클', '2222222222222', 3, 2000
); -- FK 위배

SELECT * FROM t_emp4;

-- DELETE FROM t_dept2 WHERE dcode=1000;
-- 참조하는 자식이 있으면 부모 row 삭제 불가

-- 참조하는 부모테이블의 데이터에
-- ON DELETE [reference_option]
-- 
-- 1. RESTRICT : (디폴트) 개체를 변경/삭제할 때 다른 개체가 변경/삭제할 개체를 참조하고 있을 경우 변경/삭제가 취소됩니다.(제한)
-- 2. CASCADE : 개체를 변경/삭제할 때 다른 개체가 변경/삭제할 개체를 참조하고 있을 경우 함께 변경/삭제됩니다.
-- 3. NO ACTION : MYSQL에서는 RESTRICT와 동일합니다.
-- 4. SET NULL : 개체를 변경/삭제할 때 다른 개체가 변경/삭제할 개체를 참조하고 있을 경우 참조하고 있는 값은 NULL로 세팅됩니다.

DROP TABLE IF EXISTS t_emp4;
CREATE TABLE t_emp4 (
    no INT,  -- PK
    name VARCHAR(10) NOT NULL, -- NN
    jumin VARCHAR(13) NOT NULL, -- NN, UQ
    area INT, -- CK
    deptno VARCHAR(6), -- FK
    CONSTRAINT emp4_no_pk PRIMARY KEY(no), 
    CONSTRAINT emp4_jumin_uk UNIQUE(jumin),
    CONSTRAINT emp4_area_ck CHECK(area < 5),
    CONSTRAINT emp4_deptno_fk FOREIGN KEY (deptno) 
        REFERENCES t_dept2(dcode)
        ON DELETE CASCADE  -- 부모테이블의 참조가 삭제되면 참조하는 자식도 자동으로 연쇄 삭제
);



