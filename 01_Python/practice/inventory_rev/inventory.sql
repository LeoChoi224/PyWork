-- 데이터 다루기 위한 필요한 쿼리 테스트
-- 요구사항의 동작에 필요한 쿼리문들을 작성해보고 테스트 해보세요


-- 테이블 생성 DDL
CREATE TABLE IF NOT EXISTS exam_inventory_rev (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    price INT NOT NULL CHECK(price >= 0),
    stock INT DEFAULT 0,
    regDate DATETIME DEFAULT now()
)

-- 목록
SELECT * FROM exam_inventory_rev ORDER BY id;

-- 데이터 생성 INSERT <-  name, price, stock
INSERT INTO exam_inventory_rev(name, price, stock) VALUES ('모카', 10000, 10);

-- 데이터 수정 UPDATE <- id, name, price, stock
UPDATE exam_inventory_rev SET name='로켓', price=22000, stock=20 WHERE id=1;

-- 데이터 삭제 DELETE <- id
DELETE FROM exam_inventory_rev WHERE id=1;

-- 특정 id 의 데이터 조회
SELECT * FROM exam_inventory_rev WHERE id = 1;