aaa = '뽀로로'

def bbb(name):
    print(name)

class Ccc:
    def __init__(self):
        print('Ccc 생성')

# 이 파일이 main 으로 실행될때만 실행되게 하고,
# 외부에서 import 할때는 실행되지 않게 하려면?
if __name__ == "__main__":
    print('👿크아아앙~')
    print(__name__)  # __name__ 은 파일이 직접 실행될때만 "__main__ 값을 가짐"
