# 실행: inventorymain.py
from inventorydb import InventoryDB
from dotenv import load_dotenv

print(load_dotenv())

import os

db = InventoryDB()

conn_info = {
    'host': os.getenv('db_host'),
    'user': os.getenv('db_user'),
    'password': os.getenv('db_password'),
    'database': os.getenv('db_database'),
}

db.connect(**conn_info)


# 입력 메뉴 표기
def show_menu():
    print("""
상품정보 관리 프로그램 v1.0
---------------
[1] 입력
[2] 열람
[3] 수정
[4] 삭제
[0] 종료
---------------""")


# 상품 입력하기
def append_product():
    print("아이템 항목 입력을 시작합니다.")

    name = input("아이템 이름을 입력해주세요. ")
    price = int(input("아이템 가격을 정해주세요. ") or -1)
    stock = int(input("몇 개 등록하시겠습니까? ") or 0) # 입력 없을 시 기본값 0, 0을 대입 안 시켜주면 ''가 대입되어 벨류에러

    db.insert(name, price, stock)
    

# 상품 열람하기
def show_product_list():
    print("모든 아이템 항목을 출력합니다.")
    db.select_all()


# 상품 수정하기
def update_product():
    print("선택한 항목의 상품의 내용을 변경합니다.")

    id = input("변경할 상품 id를 입력해주세요.")
    print("선택한 항목은 다음과 같습니다.")

    result = db.select_one(id)

    if result is None: return # 없는 id 라면 result = None -> 리턴으로 함수 탈출

    name = input("상품명을 입력해주세요.")
    price = int(input("가격을 입력해주세요.") or -1)
    stock = int(input("개수를 입력해주세요.") or 0) # 입력 없을 시 기본값 0, 0을 대입 안 시켜주면 ''가 대입되어 벨류에러
    
    update_result = db.update(name, price, stock, id)
    print("성공 여부", update_result)


# 상품 삭제하기
def delete_product():
    print("선택한 항목의 상품을 삭제 합니다.")
    id = input("삭제할 상품 id를 입력해주세요.")

    delete_result = db.delete(id)
    print("성공 여부", delete_result)
        
# TODO 쿼리 inventorydb.py 로 옮기기 o, Inventory(BaseModel) 검증 로직 추가 및 예외 처리 o
# 불필요 return 정리 o, 검증 부분 타입 고려, 포맷 정리, 주석 정리

def main():
    while True:
        show_menu()
        input_num = int(input("선택: ") or -1)
        if input_num == 0: 
            db.close()
            print("프로그램을 종료합니다.")
            break
        
        match input_num:
            case 1:
                append_product() # 상품 입력 함수 호출
            case 2:
                show_product_list() # 상품 열람 함수 호출
            case 3:
                update_product() # 상품 수정 함수 호출
            case 4:
                delete_product() # 상품 삭제 함수 호출
            case _:
                print(f"선택하신 번호의 항목은 존재하지 않습니다.\n재입력해주십시오.")
                continue

if __name__ == "__main__":
    main()