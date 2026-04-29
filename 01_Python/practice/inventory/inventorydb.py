# 데이터베이스 제어 모듈 작성

from inventory import Inventory
from datetime import datetime
import pymysql

class InventoryDB:
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
        # print('DB connect 성공')
    
    # 연결 종료 함수
    def close(self):
        if self.conn is None: return
        
        self.conn.close()
        self.conn = None

    # # DML 구문 실행
    # def execute(self, sql):

    #     last_row_id = -1
    #     try:
    #         cursor = self.conn.cursor()
    #         cursor.execute(sql)
    #         self.conn.commit()
    #         last_row_id = cursor.lastrowid
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         cursor.close()
    #         return last_row_id
        

    # SELECT 구문 실행 - 1개의 row 리턴 (dict 로 리턴)
    def select_one(self, id):
        result = None
        try:
            cursor = self.conn.cursor()

            sql = "SELECT * FROM inventory WHERE id = %s"
            cursor.execute(sql, id)
            result = cursor.fetchone() # 존재하는 id 라면 결과 한줄, 없다면 None

            if result is None:
                raise ValueError("ERR-3]ID오류 존재하지 않는 id:", id)

            print("-" * 30)
            print(f"{result['id']} | {result['name']} | {result['price']} | {result['stock']} | {result['regDate']}")

        except Exception as e:
            print(e)
        finally:
            cursor.close()
            return result
    

    # SELECT 결과 전체 row 불러오기
    def select_all(self):
        try:
            cursor = self.conn.cursor()

            sql = "SELECT * FROM inventory"
            cursor.execute(sql)
            result = cursor.fetchall() # 결과값 전체를 리스트[딕트{}, ...]

            print("id\tname\tprice\tcount\ttime")
            for row in result:
                print("-" * 30)
                print(f"{row['id']} | {row['name']} | {row['price']} | {row['stock']} | {row['regDate']}")

        except Exception as e:
            print(e)
        finally:
            cursor.close()

    
    # INSERT 결과 
    def insert(self, name, price, stock):
        try:
            cursor = self.conn.cursor()
            Inventory(name=name, price=price, stock=stock)

            sql = "INSERT INTO inventory (name, price, stock, regDate) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (name, price, stock, datetime.now()))

            self.conn.commit()

        except Exception as e:
            print(e)
        finally:
            cursor.close()


   # UPDATE 결과 
    def update(self, name, price, stock, id):
        result = None
        try:
            cursor = self.conn.cursor()
            Inventory(name=name, price=price, stock=stock)

            sql = "UPDATE inventory SET name=%s, price=%s, stock=%s, regDate=%s WHERE id = %s"
            cursor.execute(sql, (name, price, stock, datetime.now(), id))

            self.conn.commit()
            result = cursor.rowcount
            return result 
        except Exception as e:
            print(e)
        finally:
            cursor.close()


    # DELETE
    def delete(self, id):
        result = None
        try:
            cursor = self.conn.cursor()

            sql = "DELETE FROM inventory WHERE id = %s"
            cursor.execute(sql, id)
            result = cursor.rowcount # id = %s 이기에 삭제에 성공시 행이 1개, 아니라면 0
            
            if cursor.rowcount == 0:
                raise ValueError("ERR-3]ID오류 존재하지 않는 id:", id)
            
            self.conn.commit()
        
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            return result 