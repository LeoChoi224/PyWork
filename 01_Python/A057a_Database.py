# 데이터 베이스 제어를 위한 모듈
import pymysql
import logging  # 애플리케이션의 실행상태를 기록/추적 하기위해 사용.  print() 하는 것보다 체계적으로 기록.

class Database:
    def __init__(self):
        self.conn = None

    # 연결함수
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
        print('DB connect 성공')

    # 연결 종료 함수
    def close(self):
        if self.conn is None:
            return
        
        self.conn.close()
        self.conn = None
        print('DB connection closed!')

    # DDL, DML 구문 실행
    def execute(self, sql):

        last_row_id = -1
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            last_row_id = cursor.lastrowid
        except Exception as e:
            logging.error(e)  # '에러 로그' 작성
        finally:
            cursor.close()
            return last_row_id
        
    # SELECT 구문 실행 - 1개의 row 리턴 (dict 로 리턴)
    def select_one(self, sql):
        result = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            
        except Exception as e:
            logging.error(e)  # '에러 로그' 작성
        finally:
            cursor.close()
            return result
    
    # SELECT 결과 전체 row 불러오기
    def select_all(self, sql):
        result = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall() # => List[Dict]
            
        except Exception as e:
            logging.error(e)  # '에러 로그' 작성
        finally:
            cursor.close()
            return result        
        
    # 필요한 동작들 있으면 여기에 함수로 추가...