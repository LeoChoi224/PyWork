import logging
from datetime import datetime
import pymysql

class BookDB:
    def __init__(self):
        self.conn = None


    # 연결 함수
    def connect(self, host, user, password, database, port=3306):
        if self.conn != None: return
        
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor,            
        )

    # 연결 종료 함수
    def close(self):
        if self.conn is None: return
        
        self.conn.close()
        self.conn = None

    # DDL 테이블 생성
    def create_book_table(self):
        cursor = self.conn.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS book (
                id INT PRIMARY KEY AUTO_INCREMENT,
                title VARCHAR(100) NOT NULL,
                author VARCHAR(50) NOT NULL,
                price INT NOT NULL CHECK(price >= 0),
                stock INT NOT NULL DEFAULT 0,
                published_year INT NOT NULL CHECK(published_year BETWEEN 1900 AND 2026),
                regDate DATETIME DEFAULT now()
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8            
            """ 
        cursor.execute(sql)
        
    # DML 구문 실행
    def execute(self, sql, *args):
        last_row_id = -1
        
        try:
            cursor = self.conn.cursor()

            cursor.execute(sql, args)
            self.conn.commit()
            
            row_count = cursor.rowcount
            last_row_id = cursor.lastrowid
        except Exception as e:
            logging.error(e.__class__.__name__, e)
        finally:
            cursor.close()
            return last_row_id, row_count

    # SELECT - 1개의 row 리턴 (dict 로 리턴)
    def select_all(self, sql, *args):
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
        # print("id\ttitle\tauthor\tprice\tstock\tyear\ttime")
        # print("-" * 30)
        # print(f"{result['id']} | {result['title']} | {result['author']} | {result['price']} | {result['stock']} | {result['published_year']} | {result['regDate']}")


    # SELECT - 전체 row 불러오기
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
            # print("id\ttitle\tauthor\tprice\tstock\tyear\ttime")
            # for row in result:
            #     print("-" * 30)
            #     print(f"{result['id']} | {result['title']} | {result['author']} | {result['price']} | {result['stock']} | {result['published_year']} | {result['regDate']}")

        
    # INSERT
    def insert(self, title, author, price, stock, published_year):
        sql = "INSERT INTO book (title, author, price, stock, published_year, regDate) VALUES (%s, %s, %s, %s, %s, %s)"
        self.execute(sql, (
            title,
            author,
            price,
            stock,
            published_year,
            datetime.now()
            ))


    # UPDATE
    def update(self, title, author, price, stock, published_year, id):
        result = None
        sql = "UPDATE book SET title=%s, author=%s price=%s, stock=%s, published_year=%s, regDate=%s WHERE id = %s"
        self.execute(sql, (
            title,
            author,
            price,
            stock,
            published_year,
            datetime.now(),
            id
            ))

    # DELETE
    def delete(self, id):
        sql = "DELETE FROM book WHERE id = %s"
        result = self.execute(sql, id)

        if result == -1:
                raise ValueError("ERR-3]ID오류 존재하지 않는 id:", id)
            