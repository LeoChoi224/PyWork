from book import Book
from bookdb import BookDB
from dotenv import load_dotenv
import os

load_dotenv()
db = BookDB()

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
도서 관리 프로그램 v1.0
---------------
[1] 도서 등록
[2] 도서 목록 조회
[3] 도서 정보 수정
[4] 도서 삭제
[0] 종료
---------------""")
    db.create_book_table()


# 도서 등록하기
def append_product():
    print("도서 등록을 시작합니다.")

    try:    
        title = input("도서의 제목을 입력해주세요. ")
        author = input("도서의 저자를 입력해주세요. ")
        price = input("도서의 가격을 입력해주세요. ")
        stock = int(input("몇 개 등록하시겠습니까? ") or 0) # 입력 없을 시 기본값 0, 0을 대입 안 시켜주면 ''가 대입되어 벨류에러
        published_year = input("도서의 발행년도를 입력해주세요. ")
        Book(
            title=title,
            author=author,
            price=price,
            stock=stock,
            published_year=published_year
            )
    except Exception as e:
        print(e)
    
    db.insert(title, author, price, stock, published_year)
    

# 도서 목록 열람하기
def show_book_list():
    print("모든 도서 목록을 출력합니다.")
    db.select_all()


# 도서 정보 수정하기
def update_book_info():
    print("선택한 도서의 정보을 변경합니다.")

    id = input("변경할 도서 id를 입력해주세요.")
    print("선택한 항목은 다음과 같습니다.")

    result = db.select_one(id)

    if result == -1: return # 없는 id 라면 result = None -> 리턴으로 함수 탈출

    try:    
        title = input("도서의 제목을 입력해주세요. ")
        author = input("도서의 저자를 입력해주세요. ")
        price = input("도서의 가격을 입력해주세요. ")
        stock = int(input("몇 개 등록하시겠습니까? ") or 0) # 입력 없을 시 기본값 0, 0을 대입 안 시켜주면 ''가 대입되어 벨류에러
        published_year = input("도서의 발행년도를 입력해주세요. ")
        Book(
            title=title,
            author=author,
            price=price,
            stock=stock,
            published_year=published_year
            )
    except Exception as e:
        print(e)
    
    update_result = db.update(title, author, price, stock, published_year, id)
    print("성공 여부", update_result)


# 도서 삭제하기
def delete_book():
    print("선택한 항목의 도서을 삭제 합니다.")
    id = input("삭제할 도서 id를 입력해주세요.")

    delete_result = db.delete(id)
    print("성공 여부", delete_result)
    
    
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
                append_product() # 도서 등록 함수 호출
            case 2:
                show_book_list() # 도서 목록 조회 함수 호출
            case 3:
                update_book_info() # 도서 정보 수정 함수 호출
            case 4:
                delete_book() # 도서 삭제 함수 호출
            case _:
                print(f"선택하신 번호의 항목은 존재하지 않습니다.\n재입력해주십시오.")
                continue

if __name__ == "__main__":
    main()