# main 로직 작성
# 사용자 UI, 애플리케이션 입출력
# 실행: inventorymain.py
from inventory import Inventory
from inventorydb import InventoryDB

conn_info = {
    'host': 'localhost', 
    'user': 'user2604', 
    'password': '1234',
    'database': 'db2604',
}

# 애플리케이션 동작 객체
class InventoryApp:
    def __init__(self):
        self.db: InventoryDB = InventoryDB()
        self.db.connect(**conn_info)
        # self.db.create_table()  # table 없으면 생성해두기

    def close(self):
        self.db.close()

    def choose_menu(self) -> int:      
        while True:
            print("""
상품정보 관리 프로그램 v1.0
---------------
[1] 입력
[2] 열람
[3] 수정
[4] 삭제
[0] 종료
---------------
선택: """, end='')
            
            try:
                choice = int(input())
                if choice not in [0, 1, 2, 3, 4, 5]:
                    print('선택하신 번호의 항목은 존재하지 않습니다. 재입력해주십시오.')
                    continue

                return choice
            except ValueError as e: 
                print('잘못 입력했습니다 다시 입력해주세요')

    def create_inventory(self):
        print('아이템 항목 입력을 시작합니다')
        item = self.input_item()
        if item:
            self.db.save(item)

    def input_item(self) -> Inventory:
        print("아이템 이름을 입력해주세요.")
        name = input().strip()
        print("아이템 가격을 정해주세요.")
        price = input().strip()
        print("몇 개 등록하시겠습니까?")
        stock = input().strip()

        try:
            item = Inventory(name = name, price = price, stock = stock)
            return item
        except ValueError as e:
            for err in e.errors():
                print(err['msg'])

            return None  # 실패하면 None
        
    def show_list(self):    
        print('모든 아이템 항목을 출력합니다.')
        print('id   name     price     count   time')

        for item in self.db.list():
            print(self.to_str(item))

    # Inventory 를 목록 출력시 필요한 문자열 포맷
    def to_str(self, item: Inventory) -> str:
        return ('------------------------------\n' 
                + f'{item.id} | {item.name} | {item.price}원 | {item.stock}개 | {item.reg_date.strftime("%Y-%m-%d %H:%M:%S")}')

    def update_inventory(self):
        print("선택한 항목의 상품의 내용을 변경합니다.")
        print("변경할 상품 id를 입력해주세요")

        try:
            id = int(input())

            item = self.db.find_by_id(id)
            if not item:
                print('존재하지 않는 id 입니다')
                return

            # 출력
            print('선택한 항목은 다음과 같습니다.')
            print(self.to_str(item))

            # 변경사항 입력
            new_item = self.input_item()
            if new_item:
                item.name = new_item.name
                item.price = new_item.price
                item.stock = new_item.stock

                # UPDATE
                item = self.db.modify(item)
                if item:
                    print("성공여부: 1")
                else:
                    print('수정실패')            
        
        except ValueError as e:
            print('상품의 id 를 잘못 입력하셨습니다')

    def remove_inventory(self):
        print("선택한 항목의 상품의 삭제합니다.")
        print("삭제할 상품 id를 입력해주세요")
        try:
            id = int(input())

            item = self.db.find_by_id(id)
            if not item:
                print('존재하지 않는 id 입니다')
                return

            # DELETE
            result = self.db.remove(id)
            if result:
                print("성공여부: 1")
            else:
                print('삭제 실패')

        except ValueError as e:
            print("상품의 id 를 잘못 입력하셨습니다") 


def main():
    app = InventoryApp()  # 앱 생성

    try:
        while True:            
            menu_choice = app.choose_menu()

            match menu_choice:
                case 0: # 종료
                    print('프로그램을 종료합니다')
                    break
                
                case 1: # 입력
                    app.create_inventory()
                
                case 2: # 열람
                    app.show_list()

                case 3: # 수정
                    app.update_inventory()

                case 4: # 삭제
                    app.remove_inventory()

    except Exception as e:
        print('💢', e)
    finally:
        app.close()  # 앱 종료시 자원해제

if __name__ == "__main__":
    main() # 애플리케이션은 main() 만 호출하는 것으로 동작하게 합니다.
           # ←여기에 다른 코드 추가하지 마세요
