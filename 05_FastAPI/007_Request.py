# 🟦 쿼리 매개변수 

from fastapi import FastAPI
app = FastAPI()

# FastAPI에서는 Query 클래스를 사용하여 쿼리 매개변수를 선언하고 검증 규칙을 추가할 수 있습니다. 
# 이 클래스를 함수의 매개변수 기본값으로 사용하면 해당 매개변수가 쿼리 매개변수임을 FastAPI에 알려줍니다.
from fastapi import Query

@app.get("/users/")
def read_users(q: str = Query(default=None, max_length=5)):
                            # default= 가 주어지면 'q' 는 optional
                            # max_length= 최대길이 제약조건
    return {"q": q}
# Query(default, 옵션들...)
# -min_length: 문자열 매개변수에 대한 최소 길이를 지정합니다.
# -max_length: 문자열 매개변수에 대한 최대 길이를 지정합니다.
# -alias: 매개변수의 별칭을 지정합니다. 이를 통해 URL에서 사용하는 이름과 함수 내에서 사용하는 이름을 다르게 할 수 있습니다.
# -deprecated: 매개변수가 더 이상 사용되지 않음을 명시합니다. 이는 API 문서에 표시되어 사용자가 해당 매개변수를 사용하지 않도록 경고합니다.
# -description: 매개변수에 대한 설명을 추가합니다. 이 설명은 API 문서에 표시되어 매개변수의 사용 목적이나 기대되는 값 등을 설명할 수 있습니다.
# -ge: (greater than or equal to) 매개변숫값이 지정된 값 이상이어야 함을 명시합니다.
# -le: (less than or equal to) 매개변숫값이 지정된 값 이하이어야 함을 명시합니다.
# -regex: 매개변숫값이 일치해야 하는 정규 표현식 패턴을 지정합니다.
# -title: 매개변수의 설명 제목을 지정합니다. 이는 주로 API 문서에서 매개변수를 설명할 때 사용됩니다.
# -example: 매개변수의 예시 값을 제공합니다. 이는 문서에서 매개변수의 예상 입력값을 보여주는 데 도움을 줍니다.

# Query 클래스의 이러한 옵션들을 사용함으로써 FastAPI에서는 매개변수에 대한 상세한 검증 규칙과 문서화 정보를 제공할 수 있으며, 
# 이는 API의 사용성과 안정성을 높이는 데 기여합니다.


# 🟦 alias= 옵션
@app.get("/items/")
def read_items(internal_query: str = Query(None, alias="search")):
    return {"query_handled": internal_query}


# 🟦 deprecated= 옵션
@app.get("/images/")
def read_images(q: str = Query(None, deprecated=True)):
    return {"q": q}


# 🟦 description= 옵션
@app.get("/info/")
def read_info(info: str = Query(None, description="정보를 입력해주세요")):
    return {"info": info}


# 🟡 >HTTP 프로토콜과 요청

# 프로토콜은 컴퓨터나 원격 장치 간 통신을 위한 규칙의 집합입니다.
# 이러한 규칙은 데이터 포맷, 타이밍, 시퀀싱, 에러 처리 방법 등을 포함하여 네트워크상에서 정보가 어떻게 전송되어야 하는지를 정의합니다.
# 일반적인 통신 프로토콜에는 TCP/IP, HTTP, FTP 등이 있으며, 각각은 다양한 통신 요구 사항을 충족하기 위해 설계되었습니다.

# HTTP(HyperText Transfer Protocol)는 웹에서 데이터를 교환하기 위한 프로토콜입니다.
# www(World Wide Web)의 기초가 되는 이 프로토콜은 클라이언트와 서버 간에 HTML문서나 이미지 같은 리소스를 요청하고 전송하는 데 사용됩니다.
# HTTP는 상태가 없는 (stateless) 프로토콜이지만, 쿠키 등의 기술을 사용하여 상태 정보를 유지할 수 있습니다.

# HTTP 요청(HTTP request)은 클라이언트가 서버에 특정 작업을 요청하는 메시지입니다.
# 이는 일반적으로 웹 브라우저(클라이언트)에서 웹 서버로 정보를 얻거나, 서버상의 데이터를 수정하기 위해 사용됩니다.

# 🟡 HTTP 요청은 다음과 같이 구성됩니다.
# •Method: 서버에 요청하는 작업의 유형을 정의합니다(e.g, GET, POST, PUT).
# •URL: 요청이 지시되는 리소스의 위치를 나타냅니다.
# •Headers: 요청에 대한 메타데이터를 포함하며 인증, 캐싱, 클라이언트 유형 등의 정보를 담습니다.
# •Body: 일부 HTTP 메서드(POST, PUT)에서 사용되며, 전송할 데이터를 담습니다.

@app.get("/comments/")
def read_comments(comment_id: int = Query(...)):
    return {"comment_id": comment_id}

# GET 방식에는 Request body 가 없다. (필요없다)
# Reuqest body 는 주로 POST, PUT, PATCH 방식에 국한된다.

from fastapi import Body  # 요청 body

@app.post("/boards/")
def create_board(board: dict = Body(
        default=None,  # 옵셔녕,  기본값 설정
        example={"key": "value"},  # 문서에 표시고리 예시 값
        media_type="application/json",  # request 의 content-type
        alias="post_alias",  # 별칭 설정
        title="Sample post",  # 문서 제목
        description="This is a sample item",  # 상세 설명
        deprecated=False
    )):
    return {"board": board}
