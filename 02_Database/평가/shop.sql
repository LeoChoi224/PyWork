
CREATE TABLE Comment
(
  id         INT      NOT NULL AUTO_INCREMENT COMMENT '일련번호',
  content    TEXT     NOT NULL COMMENT '내용',
  created_at DATETIME NULL     DEFAULT now() COMMENT '작성일',
  member_no  INT      NOT NULL COMMENT '고유번호',
  post_id    INT      NOT NULL COMMENT '일련번호',
  PRIMARY KEY (id)
) COMMENT '댓글';

CREATE TABLE Friend
(
  id                  INT                        NOT NULL AUTO_INCREMENT,
  requester_member_no INT                        NOT NULL COMMENT '고유번호',
  receiver_member_no  INT                        NOT NULL COMMENT '고유번호',
  status              ENUM('PENDING','ACCEPTED') NULL     COMMENT '상태',
  PRIMARY KEY (id)
) COMMENT '친구';

CREATE TABLE Like
(
  member_no INT NOT NULL COMMENT '고유번호',
  post_id   INT NOT NULL COMMENT '일련번호',
  id        Int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id)
) COMMENT '좋아요';

CREATE TABLE Member
(
  no       INT          NOT NULL AUTO_INCREMENT COMMENT '고유번호',
  id       VARCHAR(50)  NOT NULL COMMENT '아이디',
  password VARCHAR(255) NOT NULL COMMENT '패스워드',
  PRIMARY KEY (no)
) COMMENT '회원';

ALTER TABLE Member
  ADD CONSTRAINT UQ_id UNIQUE (id);

CREATE TABLE Photo
(
  file_name VARCHAR NOT NULL COMMENT '파일명',
  post_id   INT     NOT NULL COMMENT '일련번호',
  id        INT     NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id)
) COMMENT '사진';

CREATE TABLE Post
(
  id         INT          NOT NULL AUTO_INCREMENT COMMENT '일련번호',
  title      VARCHAR(100) NOT NULL COMMENT '제목',
  content    TEXT         NOT NULL COMMENT '내용',
  visibility ENUM         NOT NULL DEFAULT 'PUBLIC' COMMENT '공개수준',
  view_count INT          NULL     DEFAULT 0 COMMENT '조회수',
  created_at DATETIME     NULL     DEFAULT now() COMMENT '등록일',
  member_no  INT          NOT NULL COMMENT '고유번호',
  PRIMARY KEY (id)
) COMMENT '게시물';

ALTER TABLE Post
  ADD CONSTRAINT FK_Member_TO_Post
    FOREIGN KEY (member_no)
    REFERENCES Member (no);

ALTER TABLE Comment
  ADD CONSTRAINT FK_Member_TO_Comment
    FOREIGN KEY (member_no)
    REFERENCES Member (no);

ALTER TABLE Comment
  ADD CONSTRAINT FK_Post_TO_Comment
    FOREIGN KEY (post_id)
    REFERENCES Post (id);

ALTER TABLE Photo
  ADD CONSTRAINT FK_Post_TO_Photo
    FOREIGN KEY (post_id)
    REFERENCES Post (id);

ALTER TABLE Like
  ADD CONSTRAINT FK_Member_TO_Like
    FOREIGN KEY (member_no)
    REFERENCES Member (no);

ALTER TABLE Like
  ADD CONSTRAINT FK_Post_TO_Like
    FOREIGN KEY (post_id)
    REFERENCES Post (id);

ALTER TABLE Friend
  ADD CONSTRAINT FK_Member_TO_Friend
    FOREIGN KEY (requester_member_no)
    REFERENCES Member (no);

ALTER TABLE Friend
  ADD CONSTRAINT FK_Member_TO_Friend1
    FOREIGN KEY (receiver_member_no)
    REFERENCES Member (no);
