
CREATE TABLE Account
(
  id          INT         NOT NULL AUTO_INCREMENT COMMENT '예금번호',
  balance     BIGINT      NULL     DEFAULT 0 COMMENT '잔고',
  history     LONGTEXT    NULL     COMMENT '입출금내역',
  branch_name VARCHAR(20) NOT NULL COMMENT '지점명',
  PRIMARY KEY (id)
) COMMENT '예금계좌';

CREATE TABLE Branch
(
  name     VARCHAR(20)  NOT NULL COMMENT '지점명',
  city     VARCHAR(100) NOT NULL COMMENT '도시',
  asset    BIGINT       NULL     DEFAULT 0 COMMENT '자산',
  engname  VARCHAR(20)  NOT NULL COMMENT '영문지점',
  opendate DATE         NOT NULL COMMENT '지점개설일',
  phone    VARCHAR(30)  NOT NULL COMMENT '전화번호',
  PRIMARY KEY (name)
) COMMENT '지점';

ALTER TABLE Branch
  ADD CONSTRAINT UQ_phone UNIQUE (phone);

CREATE TABLE Deposit
(
  account_id INT      NOT NULL COMMENT '예금번호',
  member_id  INT      NOT NULL COMMENT '고객번호',
  amount     BIGINT   NULL     DEFAULT 0 COMMENT '금액',
  created_at DATETIME NULL     DEFAULT now() COMMENT '예금일시',
  PRIMARY KEY (account_id, member_id)
) COMMENT '예금';

CREATE TABLE Member
(
  id        INT         NOT NULL AUTO_INCREMENT COMMENT '고객번호',
  name      VARCHAR(30) NOT NULL COMMENT '이름',
  address   TINYTEXT    NULL     COMMENT '주소',
  birthdate DATE        NULL     COMMENT '생년월일',
  PRIMARY KEY (id)
) COMMENT '고객';

ALTER TABLE Account
  ADD CONSTRAINT FK_Branch_TO_Account
    FOREIGN KEY (branch_name)
    REFERENCES Branch (name)
    ON DELETE CASCADE;

ALTER TABLE Deposit
  ADD CONSTRAINT FK_Account_TO_Deposit
    FOREIGN KEY (account_id)
    REFERENCES Account (id)
    ON DELETE CASCADE;

ALTER TABLE Deposit
  ADD CONSTRAINT FK_Member_TO_Deposit
    FOREIGN KEY (member_id)
    REFERENCES Member (id)
    ON DELETE CASCADE;
