# main 로직 작성
# 사용자 UI. 애플리케이션의 입출력
from pydantic import ValidationError
from book import Book
from bookdb import BookDB


conn_info = {
    'host': 'localhost',
    'user': 'user2604',
    'password': '1234',
    'database': 'db2604',
}


# 애플리케이션 동작 객체
class BookApp:
    def __init__(self):
        self.db: BookDB = BookDB()
        self.db.connect(**conn_info)
        self.db.create_table()
        print("DB 테이블이 준비되었습니다.")

    def close(self):
        self.db.close()

    def choose_menu(self) -> int:
        while True:
            print("""
도서관리 v1.0
---------------
[1] 입력
[2] 목록 [21] 번호↓ [22] 번호↑ [23] 제목↓ [24] 제목↑ [25] 가격↓ [26] 가격↑ [27] 출판일↓ [28] 출판일↑
[3] 수정
[4] 삭제
[0] 종료
---------------
선택: """, end='')

            try:
                choice = int(input())

                if choice in [0, 1, 2, 3, 4] or 21 <= choice <= 28:
                    return choice
                else:
                    print('선택하신 번호의 항목은 존재하지 않습니다. 재입력해주십시오.')

            except ValueError:
                print('잘못 입력했습니다. 숫자로 다시 입력해주세요.')

    def create_book(self):
        print('책 정보를 입력합니다')

        while True:
            item = self.input_item()

            if not item:
                return

            if self.db.find_by_no(item.no):
                print('이미 존재하는 책 번호입니다. 다른 번호를 입력해주세요.\n')
                continue

            saved_item = self.db.save(item)

            if saved_item:
                print('데이터가 입력되었습니다')
            else:
                print('데이터 입력에 실패했습니다.')
            return

    def input_item(self) -> Book:
        while True:
            print("책 번호 입력 (알파벳1자리 + 숫자4자리 형식): ", end='')
            no = input().strip()

            print("책 제목 입력: ", end='')
            title = input().strip()

            print("가격 입력(0이상 정수): ", end='')
            price = input().strip()

            print("출판일 입력(yyyy-MM-dd): ", end='')
            publishedAt = input().strip()

            try:
                item = Book(
                    no=no,
                    title=title,
                    price=price,
                    publishedAt=publishedAt
                )

                return item

            except ValidationError as e:
                for err in e.errors():
                    print(err['msg'])

                print('다시 입력해주세요.\n')

    def input_update_item(self, no: str) -> Book:
        while True:
            print("책 제목 입력: ", end='')
            title = input().strip()

            print("가격 입력(0이상 정수): ", end='')
            price = input().strip()

            print("출판일 입력(yyyy-MM-dd): ", end='')
            publishedAt = input().strip()

            try:
                return Book(
                    no=no,
                    title=title,
                    price=price,
                    publishedAt=publishedAt
                )
            except ValidationError as e:
                for err in e.errors():
                    print(err['msg'])
                print('다시 입력해주세요.\n')

    def show_list(self):
        print('책 목록 출력')

        row_list = self.db.list()

        print(f'{len(row_list)} 개의 데이터')
        print('No    | Title                |      Price | Publication')
        print('--------------------------------------------------------')

        if not row_list:
            print('(출력할 데이터가 없습니다)')
            return

        for row in row_list:
            print(self.to_str(row))

    def optional_show_list(self, menu_choice, sort):
        print('책 목록 출력')

        order_by = ""

        match (menu_choice - 21) // 2:
            case 0:
                order_by = "no"
            case 1:
                order_by = "title"
            case 2:
                order_by = "price"
            case 3:
                order_by = "publishedAt"

        row_list = self.db.optional_list(order_by, sort)

        print(f'{len(row_list)} 개의 데이터')
        print('No    | Title                |      Price | Publication')
        print('--------------------------------------------------------')

        if not row_list:
            print('(출력할 데이터가 없습니다)')
            return

        for row in row_list:
            print(self.to_str(row))

    # Book을 목록 출력 시 필요한 문자열 포맷
    def to_str(self, item: Book) -> str:
        return (
            f'{item.no:<5} | '
            f'{item.title:<20} | '
            f'{item.price:>10,} | '
            f'{item.publishedAt.strftime("%Y-%m-%d")}'
        )

    def update_book(self):
        print("책 정보 수정")
        print("수정할 책번호를 입력하세요: ", end='')

        old_no = input().strip().upper()

        item = self.db.find_by_no(old_no)

        if not item:
            print('존재하지 않는 책입니다')
            return

        print('선택한 항목은 다음과 같습니다.')
        print(self.to_str(item))

        print('수정할 정보를 입력해주세요. (책번호는 변경되지 않습니다)')
        new_item = self.input_update_item(old_no)

        if new_item:
            modified_item = self.db.modify(old_no, new_item)

            if modified_item:
                print("수정되었습니다")
            else:
                print('수정실패')

    def remove_book(self):
        print("책 삭제")
        print("삭제할 책번호를 입력하세요: ", end='')

        no = input().strip().upper()

        item = self.db.find_by_no(no)

        if not item:
            print('존재하지 않는 책번호입니다')
            return

        print('삭제 대상:', self.to_str(item))
        result = self.db.remove(no)

        if result:
            print("삭제하였습니다")
        else:
            print('삭제 실패')


def main():
    app = BookApp()

    try:
        while True:
            menu_choice = app.choose_menu()

            if menu_choice > 20 and menu_choice % 2 != 0:
                app.optional_show_list(menu_choice, "ASC")
                continue

            elif menu_choice > 20 and menu_choice % 2 == 0:
                app.optional_show_list(menu_choice, "DESC")
                continue

            match menu_choice:
                case 0:
                    print('프로그램을 종료합니다')
                    break

                case 1:
                    app.create_book()

                case 2:
                    app.show_list()

                case 3:
                    app.update_book()

                case 4:
                    app.remove_book()

    except Exception as e:
        print('💢', e)

    finally:
        app.close()


if __name__ == "__main__":
    main()