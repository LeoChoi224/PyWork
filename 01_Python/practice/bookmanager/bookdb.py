# 데이터베이스 제어 (데이터소스) 객체 작성
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
            cursorclass=pymysql.cursors.DictCursor,
        )

    # DB 연결 닫기
    def close(self):
        if self.conn is None:
            return

        self.conn.close()
        self.conn = None

    # DDL 테이블 생성
    def create_table(self):
        cursor = self.conn.cursor()

        try:
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
            self.conn.commit()

            # CREATE TABLE IF NOT EXISTS는 rowcount로 생성/존재 여부 구분이 애매합니다.
            # 과제 흐름상 프로그램 시작 시 테이블 없으면 생성만 보장합니다.

        except Exception as e:
            print("DB 테이블 생성 중 오류가 발생했습니다:", e)

        finally:
            cursor.close()

    # INSERT / UPDATE / DELETE 실행
    def execute_dml(self, sql, *args):
        last_row_id = -1
        row_count = 0

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, args)
            self.conn.commit()

            last_row_id = cursor.lastrowid
            row_count = cursor.rowcount

        except Exception as e:
            self.conn.rollback()
            logging.error(e)

        finally:
            cursor.close()
            return last_row_id, row_count

    # SELECT 구문 실행 - 1개의 ROW 리턴
    def execute(self, sql, *args) -> dict:
        result = None

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, args)
            result = cursor.fetchone()

        except Exception as e:
            logging.error(e)

        finally:
            cursor.close()
            return result

    # SELECT 실행 후 전체 row 반환
    def select_all(self, sql, *args):
        result = []

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, args)
            result = cursor.fetchall()

        except Exception as e:
            logging.error(e)

        finally:
            cursor.close()
            return result

    # 입력 <- Book(no, title, price, publishedAt)
    # 리턴값: 생성된 row => Book
    def save(self, item: Book) -> Book:
        sql = """
            INSERT INTO exam_book(no, title, price, publishedAt)
            VALUES (%s, %s, %s, %s)
        """

        _, row_count = self.execute_dml(
            sql,
            item.no,
            item.title,
            item.price,
            item.publishedAt.strftime("%Y-%m-%d")
        )

        if row_count > 0:
            return self.find_by_no(item.no)

        return None

    # 특정 no의 데이터 조회
    def find_by_no(self, no: str) -> Book:
        sql = """
            SELECT
                id,
                no,
                title,
                price,
                DATE_FORMAT(publishedAt, '%%Y-%%m-%%d') AS publishedAt,
                createdAt
            FROM exam_book
            WHERE no = %s
        """

        row = self.execute(sql, no)

        if not row:
            return None

        return Book(**row)

    # 전체 목록 - 기본 저장순
    def list(self) -> list[Book]:
        sql = """
            SELECT
                id,
                no,
                title,
                price,
                DATE_FORMAT(publishedAt, '%%Y-%%m-%%d') AS publishedAt,
                createdAt
            FROM exam_book
            ORDER BY id
        """

        result = []

        for row in self.select_all(sql):
            item = Book(**row)
            result.append(item)

        return result

    # 정렬 목록
    def optional_list(self, order_by: str, sort: str):
        # ORDER BY 컬럼명/정렬방향은 %s 바인딩으로 넣으면 안 되므로 허용 목록으로 검증합니다.
        allowed_columns = ["no", "title", "price", "publishedAt"]
        allowed_sorts = ["ASC", "DESC"]

        if order_by not in allowed_columns:
            order_by = "no"

        if sort not in allowed_sorts:
            sort = "ASC"

        sql = f"""
            SELECT
                id,
                no,
                title,
                price,
                DATE_FORMAT(publishedAt, '%%Y-%%m-%%d') AS publishedAt,
                createdAt
            FROM exam_book
            ORDER BY {order_by} {sort}
        """

        result = []

        for row in self.select_all(sql):
            item = Book(**row)
            result.append(item)

        return result

    # 특정 no의 Book 수정
    def modify(self, old_no: str, item: Book) -> Book:
        sql = """
            UPDATE exam_book
            SET no = %s,
                title = %s,
                price = %s,
                publishedAt = %s
            WHERE no = %s
        """

        _, row_count = self.execute_dml(
            sql,
            item.no,
            item.title,
            item.price,
            item.publishedAt.strftime("%Y-%m-%d"),
            old_no
        )

        if row_count > 0:
            return self.find_by_no(item.no)

        return None

    # 특정 no의 Book 삭제
    def remove(self, no: str) -> int:
        sql = """
            DELETE FROM exam_book
            WHERE no = %s
        """

        _, row_count = self.execute_dml(sql, no)
        return row_count


# ↓동작테스트용 코드
if __name__ == "__main__":
    ...