import os

"""
환경변수(environment variable)
  운영체제 차원에서 관리되는 키-값 형태의 전역 설정 값

응용프로그램이나 프로세스가 실행될 때 운영체제에서 불러와서 사용할 수 있는 외부 설정값으로 활용
보통 KEY=VALUE 형태로 저장되며, 실행되는 프로그램이 이를 참조할 수 있습니다

▶설정값 분리
  코드 안에 직접 값(예: 데이터베이스 비밀번호, API 키 등)을 넣으면 보안에 취약하고 관리하기 어렵습니다.
  환경변수를 사용하면 코드와 설정을 분리할 수 있어 더 안전하고 유연합니다.

▶환경에 따른 차이 관리

  로컬 개발 환경, 테스트 서버, 실제 운영 서버마다 설정이 다를 수 있습니다.
  예를 들어 DB 주소나 API 엔드포인트를 환경변수로 관리하면 코드 수정 없이 환경만 바꿔 실행할 수 있습니다.

▶보안성 향상

  비밀번호, 토큰, API 키 같은 민감한 정보를 코드에 노출하지 않고 환경변수로 안전하게 관리할 수 있습니다.

▶프로세스 실행 제어

  어떤 옵션이나 모드를 켜고 끄는 플래그를 환경변수로 관리하면, 실행할 때 쉽게 제어할 수 있습니다.

  예) NODE_ENV=production node app.js
"""

"""
파이썬에서 환경변수 읽어오기

os.getenv(환경변수명)  ->  str | None  (없으면 None)
os.environ[환경변수명]  -> str (없으면 에러)

"""

"""
dotenv
  특정 '환경변수 파일'을 런타임에서 불러올수 있는 패키지
  pip install python-dotenv

※ git 등을 사용시 민감한 환경변수 파일은  .gitignore 시켜주세요
"""

print('🟦 환경변수')

print(os.getenv('PATH')[:100])
print(os.environ['PATH'][:100])

# 없는 환경변수에 대해...
print(os.getenv('XXX')) # None
# print(os.environ['XXX']) # KeyError  발생

from dotenv import load_dotenv
result = load_dotenv()  # 환경변수 파일을 정상적으로 읽어오면 True 리턴.
        # 기본적으로 현재작업경로 밑의 ".env" 파일을 찾아서 읽어옴.

# load_dotenv(특정환경변수파일경로)        

print('result =', result)


print(os.getenv('db_host'))
print(os.getenv('db_user'))
print(os.getenv('db_password'))
print(os.getenv('db_database'))

