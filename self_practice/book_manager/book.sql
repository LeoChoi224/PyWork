-- 데이터 다루기 위한 필요한 쿼리들 작성


-- 태이블 생성 DDL
CREATE TABLE IF NOT EXISTS book (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(50) NOT NULL,
    price INT NOT NULL CHECK(price >= 0),
    stock INT NOT NULL DEFAULT 0,
    published_year INT NOT NULL CHECK(published_year BETWEEN 1900 AND 2026),
    regDate DATETIME DEFAULT now()
);

-- 쿼리 동작 테스트 해보세요.


SHOW TABLES;

DROP TABLE book;

DESC book;