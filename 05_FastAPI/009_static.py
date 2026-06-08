# 🟥 정적 파일
# 웹 애플리케이션을 만들 때 정적 파일은 굉장히 중요합니다.
# 정적 파일 (static files)이란 HTML, CSS, 자바스크립트, 이미지 파일 같은 것들을 의미합니다.
# 이런 파일들은 '그대로' 브라우저에 전달되고, 서버에서는 변경이 없습니다.
# FastAPI에서도 이런 정적 파일을 쉽게 다룰 수 있는 기능을 제공합니다.

# 정적 파일들을 담을 하위 폴더 (특정 폴더) 생성
# (이하 static 폴더)


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")  # HTML 템플릿 파일 경로 설정

app = FastAPI()
app.mount(path = "/static", app = StaticFiles(directory="static"), name="static")
# app.mount()메서드를 사용해서 
# /static이라는 URL 경로와 - static 디렉터리를 연결
# 그리고 이를 static이라는 '이름'으로 지정.


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse({"request": request}, "index_static1.html")