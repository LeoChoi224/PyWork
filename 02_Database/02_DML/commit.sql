-- DCL : Data Control Language
-- commit : 작업결과를 물리적 디스크에 저장.  manipulation 작업이 정상적으로 완료
-- rollback : 원래의 데이터 상태로 복구

-- 테이블과 데이터 준비
DESC phonebook;
SELECT * FROM phonebook ;

DROP TABLE IF EXISTS phonebook; 

CREATE TABLE phonebook(
    id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(80) NOT NULL,
    phonenum varchar(20) DEFAULT '010-0000-0000',
    email varchar(100),
    regdate datetime DEFAULT now()
);


INSERT INTO phonebook (name, phonenum, email)
VALUES
    ('아이언맨', '111-1111-1111', 'ironman@mail.com')
    , ('캡틴아메리카', '222-2222-2222', 'captain@mail.com')
    , ('토르', '3333-3333-3333', 'thor@mail.com')
;
SELECT * FROM phonebook;

DELETE FROM phonebook;  -- 다 지워진다!

-- 기본적으로 MySQL 은 auto-commit 이다
-- DML 은 실행 즉시 물리적인 데이터에 반영된다.

-- MySQL 은 기본적으로 auto commit 이다.
-- commit 을 사용하려면 auto commit 부터 비활성화 해야 한다.

SELECT @@autocommit; -- 현재 auto COMMIT 활성화 여부 1: 활성화  0:비활성화

SET @@autocommit = 0;

commit; -- 변경내역을 DB 에 저장

DELETE FROM phonebook WHERE id = 5;

SELECT * FROM phonebook;

UPDATE phonebook SET email = 'avengers@center';

rollback;   -- 마지막으로 commit 했던 상태로 되돌아감.

SELECT * FROM phonebook;