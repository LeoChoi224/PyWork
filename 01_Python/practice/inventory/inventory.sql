-- 데이터 다루기 위한 필요한 쿼리들 작성


-- 태이블 생성 DDL
CREATE TABLE inventory(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(80) NOT NULL,
    price INT NOT NULL CHECK(price >= 0),
    stock INT DEFAULT 0,
    regDate DATETIME DEFAULT now()
);


-- 쿼리 동작 테스트 해보세요.

SHOW DATABASES;

USE db2604;

SHOW TABLES;

DROP TABLE inventory;

SELECT * FROM inventory;

DESC inventory;

INSERT INTO inventory (name, price, stock) VALUES ('abc', 1000, 2);

SELECT * FROM inventory WHERE id = 10;

SHOW DATABASES;