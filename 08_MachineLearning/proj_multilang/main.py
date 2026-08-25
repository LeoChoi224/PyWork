from fastapi import FastAPI, Request

import joblib, os

# 모델 로드
model_path = r'./model/freq.pkl'
clf = joblib.load(model_path)

# 템플릿 설정
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

def detect_lang(text):
    # 알파벳 출현 빈도 구하기
    text = text.lower()

    # 알파벳인 경우 해당 알파벳의 빈도수 ++
    cnt = []
    for i in range(26):
        ch = chr(i + ord('a'))
        cnt.append(text.count(ch))

    total = sum(cnt)

    if total == 0: return "입력이 없습니다"
    
    # 빈도 계산
    freq = list(map(lambda n : n / total, cnt))
    
    # 언어 예측하기
    res = clf.predict([freq])
    
    # 언어 코드를 한국어로 변환하기
    lang_dic = {
        "en": "영어",
        "fr": "프랑스어",
        "id": "인도네시아어",
        "tl": "타갈로그어"
    }
    return lang_dic[res[0]]


app = FastAPI()

from fastapi.staticfiles import StaticFiles
app.mount("/static",  StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"message": "Hello Multilang"}

@app.get("/lang")
def form(request: Request):
    return templates.TemplateResponse(
        request, 
        "langform.html",
        {"username": "최홍묵"})


from pydantic import BaseModel

class InputText(BaseModel):
    text: str

@app.post("/detect_lang")
def class_lang(body: InputText):
    print('✅ body:', body)
    result = detect_lang(body.text)
    return {"result": result}









