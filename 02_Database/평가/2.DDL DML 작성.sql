-- ──────────────────────────────────────────────────────────
-- ↓ DDL 작성하기
-- 🟦☞

CREATE TABLE IF NOT EXISTS TEST_DEPARTMENT (
    dept_uid INT PRIMARY KEY,
    dept_name VARCHAR(30) NOT NULL,
    dept_build VARCHAR(10) CHECK (
        dept_build IN ('K301', 'A203', 'B306')
    )
);

CREATE TABLE IF NOT EXISTS TEST_STUDENT (
    stu_uid INT PRIMARY KEY,
    stu_name VARCHAR(20) NOT NULL,
    stu_age INT CHECK (stu_age >= 0),
    stu_grade INT CHECK (stu_grade BETWEEN 1 AND 4),
    dept_uid INT,

    FOREIGN KEY (dept_uid)
    REFERENCES TEST_DEPARTMENT(dept_uid)
);


-- ↓ DML 작성하기
-- 🟦☞

INSERT INTO TEST_DEPARTMENT VALUES(1, "a과", "K301");
INSERT INTO TEST_DEPARTMENT VALUES(2, "b과", "A203");
INSERT INTO TEST_DEPARTMENT VALUES(3, "c과", "B306");
INSERT INTO TEST_STUDENT VALUES(1, 'a학생', 20, 1, 1);
INSERT INTO TEST_STUDENT VALUES(2, 'b학생', 20, 2, 1);
INSERT INTO TEST_STUDENT VALUES(3, 'c학생', 20, 3, 1);
INSERT INTO TEST_STUDENT VALUES(4, 'd학생', 21, 1, 2);
INSERT INTO TEST_STUDENT VALUES(5, 'e학생', 22, 1, 3);




DROP IF EXISTS TABLE TEST_STUDENT;
DROP IF EXISTS TABLE TEST_DEPARTMENT;

SELECT * FROM TEST_STUDENT;
SELECT * FROM TEST_DEPARTMENT;