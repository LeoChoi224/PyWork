-- 요구사항의 동작에 필요한 쿼리문들을 먼저 작성해보고 테스트 해보세요


CREATE TABLE IF NOT EXISTS exam_book (
    id INT PRIMARY KEY AUTO_INCREMENT,
    no VARCHAR(5) UNIQUE,
    title VARCHAR(100) NOT NULL,
    price INT DEFAULT 0 CHECK(price >= 0),
    publishedAt DATE NOT NULL,
    createdAt DATETIME DEFAULT now()
);


SHOW TABLES;

DESC exam_book;

DROP TABLE exam_book;

-- INSERT [1]
-- sql = "INSERT INTO exam_book(no, title, price, publishedAt) VALUES (%s, %s, %s, %s)"
INSERT INTO exam_book(no, title, price, publishedAt) VALUES ("g# 데이터베이스 제어 (데이터소스) 객체 작성
import logging
import pymysql
import pymysql.cursors
from book import Book

class BookDB:
    def __init__(self):
        self.conn = None

    # DB 연결
    def connect(self, host, user, password, database, port=3306):
        if self.conn != None:
            return
        
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor,  # SELECT 결과를 dict 형태로 받아로려면 꼭 설정
        )    

    # DB연결 닫기
    def close(self):
        if self.conn is None:
            return
        
        self.conn.close()
        self.conn = None         


    # DDL 테이블 생성
    def create_table(self):
        cursor = self.conn.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS exam_book (
                id INT PRIMARY KEY AUTO_INCREMENT,
                no VARCHAR(5) UNIQUE,
                title VARCHAR(100) NOT NULL,
                price INT DEFAULT 0 CHECK(price >= 0),
                publishedAt DATE NOT NULL,
                createdAt DATETIME DEFAULT now()
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8            
            """ 
        cursor.execute(sql)
        row_count = cursor.rowcount
        if row_count:
            print("DB 테이블을 생성하셨습니다")

    # # DML 실행
    # def execute(self, sql, *args):
    #     result = None
    #     try:
    #         cursor = self.conn.cursor()
    #         cursor.execute(sql, args)
    #         self.conn.commit()

    #         result = cursor.fetchone()
    #     except Exception as e:
    #         logging.error(e.__class__.__name__, e)
    #     finally:
    #         cursor.close()
    #         return result
        
        
    # SELECT 구문 실행 - 1개의 ROW 리턴 (dict 형태로 리턴)
    def execute(self, sql, *args) -> dict:
        result = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, args)
            result = cursor.fetchone()

        except Exception as e:
            logging.error(e.__class__.__name__, e)
        finally:
            cursor.close()
            return result
        
    # SELECT 실행후 전체 row 들 불러옴
    def select_all(self, sql, *args):
        result = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, args)
            result = cursor.fetchall() # -> list[dict]

        except Exception as e:
            logging.error(e.__class__.__name__, e)
        finally:
            cursor.close()
            return result

    # -------------------------------------------------------------------------------------

    # 입력 <- Book(no, title, price, publishedAt)
    #    리턴값 : 생성된 row => Book
    def save(self, item: Book) -> Book:
        sql = "INSERT INTO exam_book(no, title, price, publishedAt) VALUES (%s, %s, %s, %s)"
        row = self.execute(sql, (item.no, item.title, item.price, item.publishedAt))
        print('🧡', row)  # 확인용
        # return self.find_by_no(row[no])


    # 특정 no 의 데이터 조회
    def find_by_no(self, no: str) -> Book:
        sql = "SELECT * FROM exam_book WHERE no = %s"
        row = self.execute(sql, (no,))  # dict 형태. 없으면 None 리턴

        if not row: return row

        return Book(**row)

    # 전체 목록
    def list(self) -> list[Book]:
        sql = "SELECT no, title, price, publishedAt FROM exam_book ORDER BY id"
        # list[dict] => list[Book]
        result = []
        for row in self.select_all(sql):
            item = Book(**row)
            result.append(item)
        return result
    
        # 전체 목록
    def optional_list(self, order_by, sort):

        sql = "SELECT no, title, price, publishedAt FROM exam_book ORDER BY %s %s"
        result = []
        for row in self.select_all(sql, (order_by, sort)):
            item = Book(**row)
            result.append(item)
        return result
    
    # 특정 no 의 Book 수정 <- no, title, price, publishedAt, no # TODO no 고민
    def modify(self, item: Book) -> Book:
        sql = "UPDATE exam_book SET no=%s, title=%s, price=%s, publishedAt=%s WHERE no=%s"
        _, row_count = self.execute(sql, item.no, item.title, item.price, item.publishedAt, item.no)
        return self.find_by_no(item.id)

    # 특정 no 의 Book 삭제
    def remove(self, no: int) -> int:
        sql = "DELETE FROM exam_book WHERE no = %s"
        _, row_count = self.execute(sql, no)
        return row_count
    





# ↓동작테스트용 코드
if __name__ == "__main__":
    ...2153", "hongmook", 999999, "2026-04-10");

-- SELECT ALL [2]
-- sql = "SELECT no, title, price, publishedAt FROM exam_book ORDER BY id"
SELECT id, no, title, price, publishedAt FROM exam_book ORDER BY id;

-- SELECT ONE
-- sql = "SELECT * FROM exam_book WHERE no = %s"
SELECT * FROM exam_book WHERE no = 'A1153';

-- UPDATE [3]
-- sql = "UPDATE exam_book SET no=%ㄴ, title=%s, price=%s, publishedAt=%s WHERE no=%s"
UPDATE exam_book SET no="B9827", title="야호", price=123456, publishedAt="1996-02-24" WHERE no="A1223";

-- DELETE [4]
-- sql = "DELETE FROM exam_book WHERE no = %s"
DELETE FROM exam_book WHERE no = "A1233"


-- SELECT ALL no ASC [21]
-- sql = "SELECT no, title, price, publishedAt FROM exam_book ORDER BY no ASC"
SELECT no, title, price, publishedAt FROM exam_book ORDER BY no ASC;

-- SELECT ALL no DESC [22]
sql = "SELECT no, title, price, publishedAt FROM exam_book ORDER BY no DESC"

-- SELECT ALL title ASC [23]
sql = "SELECT no, title, price, publishedAt FROM exam_book ORDER BY title ASC"

-- SELECT ALL title DESC [24]
sql = "SELECT no, title, price, publishedAt FROM exam_book ORDER BY title DESC"

-- SELECT ALL price ASC [25]
sql = "SELECT no, title, price, publishedAt FROM exam_book ORDER BY price ASC"

-- SELECT ALL price DESC [26]
sql = "SELECT no, title, price, publishedAt FROM exam_book ORDER BY price DESC"

-- SELECT ALL publishedAt ASC [27]
sql = "SELECT no, title, price, publishedAt FROM exam_book ORDER BY publishedAt ASC"

-- SELECT ALL publishedAt DESC [28]
sql = "SELECT no, title, price, publishedAt FROM exam_book ORDER BY publishedAt DESC"












