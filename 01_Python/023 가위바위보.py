import random
print('가위 바위 보 게임')
data = {1: "가위", 2: "바위", 3: "보"}

# 메뉴 보여주기
def show_menu():
    i = 1

    print("\n" + "=" * 20)
    for i in data:
        print(f"[{i}] : {data[i]}")
    print("[0] : 종료")
    print("=" * 20)


# 사용자 입력을 받아 리턴
# 입력허용: 1, 2, 3, 0
# 허용하지 않는 값 입력시 재입력 유도
def input_choice():
    num = int(input("선택 : "))

    while num < 0 or num > 3:
        num = int(input("\n0 ~ 3 까지의 정수를 다시 입력해주세요 : "))
    
    return num


# 컴퓨터 선택: 1 < 2 이김 2 < 3 짐
#  램덤으로 리턴
#  리턴값:  1 - 가위,  2- 바위,  3 - 보
def computer_select():
    return random.randint(1, 3)


# 컴퓨터와 사용자의 선택 보여주기
def display_choice(user_choice, computer_choice):
    print("\n사용자 vs 컴퓨터")
    print(f"{data[user_choice]} vs {data[computer_choice]}\n")


# 가위바위보 결과 보여주기
def compute_result(user_choice, computer_choice):
    print("승부 결과")
    print_win = "유저가 이겼습니다."
    print_lose = "유저가 졌습니다."
    print_draw = "무승부"

    if computer_choice == user_choice:
        print(print_draw)
    else:
        match user_choice:
            case 1:
                print(print_win) if computer_choice == 3 else print(print_lose)
            case 2:
                print(print_win) if computer_choice == 1 else print(print_lose)
            case 3:
                print(print_win) if computer_choice == 2 else print(print_lose)

            

"""
아래 코드는 건드리지 마세요
"""
while True:
    show_menu()   # 메뉴보여주기

    user_choice = input_choice() # 사용자 입력
    if user_choice == 0:
        break  # 0 이변 종료
   
    # 컴퓨터 선택:   1 - 가위,  2- 바위,  3 - 보
    computer_choice = computer_select()
    display_choice(user_choice, computer_choice) # 양측의 선택 보여주기
    compute_result(user_choice, computer_choice) # 승부결과 보여주기    
