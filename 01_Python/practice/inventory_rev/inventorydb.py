# 데이터베이스 제어 객체 작성
#  TODO

import logging
import pymysql
import pymysql.cursors
from inventory import Inventory

class InventoryDB:
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

    # DDL, DML 실행
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

    # SELECT 구문 실행 - 1개의 ROW 리턴 (dict 형태로 리턴)
    def select_one(self, sql, *args) -> dict:
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

    # 생성 <- Inventory(name, price, stock)
    #    리턴값 : 생성된 row => Inventory
    def save(self, item: Inventory) -> Inventory:
        sql = "INSERT INTO exam_inventory_rev(name, price, stock) VALUES (%s, %s, %s)"
        last_row_id, row_count = self.execute(sql, item.name, item.price, item.stock) # last_row_id -> 생성된 함수 id 값이 바로 필요한 경우.예: 게시물 포스팅
        # print('🧡', last_row_id, row_count)  # 확인용
        return self.find_by_id(last_row_id)


    # 특정 id 의 데이터 조회
    def find_by_id(self, id: int) -> Inventory:
        sql = "SELECT * FROM exam_inventory_rev WHERE id = %s"
        row = self.select_one(sql, id)  # dict 형태. 없으면 None 리턴

        if not row: return row

        return Inventory(**row)

    # 전체 목록
    def list(self) -> list[Inventory]:
        sql = "SELECT id, name, price, stock, regDate as reg_date FROM exam_inventory_rev ORDER BY id"
        # list[dict] => list[Inventory]
        result = []
        for row in self.select_all(sql):
            item = Inventory(**row)
            result.append(item)
        return result
    
    # 특정 id 의 Inventory 수정 <- name, price, stock, id
    def modify(self, item: Inventory) -> Inventory:
        sql = "UPDATE exam_inventory_rev SET name=%s, price=%s, stock=%s WHERE id=%s"
        _, row_count = self.execute(sql, item.name, item.price, item.stock, item.id)
        return self.find_by_id(item.id)

    # 특정 id 의 inventory 삭제
    def remove(self, id: int) -> int:
        sql = "DELETE FROM exam_inventory_rev WHERE id = %s"
        _, row_count = self.execute(sql, id)
        return row_count
    

# 동작 테스트        
if __name__ == "__main__":        
    conn_info = {
        'host': 'localhost', 
        'user': 'user2604', 
        'password': '1234',
        'database': 'db2604',
    }    
    db = InventoryDB()
    db.connect(**conn_info)

    item = db.save(Inventory(name='장갑', price=25000, stock=120))
    print(item)
    print(db.find_by_id(-1))

    item = db.modify(Inventory(id=2, name='티셔츠', price=32500, stock=28))
    print(item)

    print('목록]')
    for item in db.list():
        print(item)

    print(db.remove(3))

    db.close()