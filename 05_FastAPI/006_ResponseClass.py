# 응답 클래스

# FastAPI에서 응답 클래스는 서버가 클라이언트에게 반환하는 HTTP 응답의 종류를 정의합니다. 
# 이를 통해 개발자는 반환되는 데이터의 형식을 제어하고, 특정 HTTP 응답의 동작을 세밀하게 조정할 수 있습니다.

# 🟡 다음은 주요 응답 클래스 리스트입니다.

# - JSONResponse: 클라이언트에게 JSON 형식의 데이터를 반환합니다. 
#   이 클래스는 파이썬의 딕셔너리나 Pydantic 모델을 JSON 문자열로 변환하여 응답 바디에 담아 전송합니다.

# - HTMLResponse: 클라이언트에게 HTML 형식의 데이터를 반환합니다. 
#   주로 웹페이지의 내용을 반환할 때 사용합니다.

# - PlainTextResponse: 클라이언트에게 단순 텍스트 형식의 응답을 반환합니다. 
#   이는 로깅, 간단한 메시지 전달 등에 적합합니다.

# - RedirectResponse: 이 응답 클래스는 클라이언트를 지정된 다른 URL로 리디렉션하는 HTTP 응답을 생성합니다. 
#   이는 사용자를 다른 페이지로 유도할 때 유용합니다.

from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse, RedirectResponse

app = FastAPI()

# content-type : application/json
@app.get("/json", response_class=JSONResponse)
def read_json():
    return {"msg": "This is JSON"}

# content-type : text/plain
@app.get("/text", response_class=PlainTextResponse)
def read_text():
    return "<div>This is <u>Plain</u> Text</div>"

# content-type : text/html
@app.get("/html", response_class=HTMLResponse)
def read_text():
    return "<div>This is <u>Plain</u> Text</div>"

# content-type : text/html
@app.get("/input_age/", response_class=HTMLResponse)
def input_age():
    return """
    <form action="/age_check/">
		당신의 나이를 입력하세요<br/>
		<input type="text" name="age" size=4/><br/>
		<input type="submit" value = "전송"/>	
	</form>
    """

@app.get("/age_check/")
def age_check(age: int):
    if age < 19:
        return RedirectResponse(url = "/under_age/")
    else:
        return RedirectResponse(url = "/adult")

@app.get("/under_age/")
def under_age():
    return "당신은 미성년자입니다."

@app.get("/adult/")
def adult():
    return "당신은 성인입니다."