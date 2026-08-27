import os, shutil

from fastapi import FastAPI, Request, File, UploadFile
from fastapi.staticfiles import StaticFiles

from model.fashionmnist import *

app = FastAPI()

# 템플릿 설정
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates( directory="templates")

# 2. 'uploads' 폴더를 '/static' 경로로 서빙하도록 설정
# 예: uploads/image.jpg 파일은 http://127.0.0.1:8000/static/image.jpg 로 접근 가능
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


app.mount("/static", StaticFiles(directory=UPLOAD_DIR), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.post("/upload")
async def upload_image(fashionfile: UploadFile = File(...)):
    # 업로드된 파일 저장
    file_path = os.path.join(UPLOAD_DIR, fashionfile.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(fashionfile.file, buffer)

    # 추론 (예측)
    pred = predict(file_path)

    # 업로드 성공 후, 접근 가능한 이미지 URL을 예측 결과와 함꼐 응답
    image_url = f"http://127.0.0.1:8000/static/{fashionfile.filename}"
    return {
        "filename": fashionfile.filename,
        "url": image_url,
        "message": "이미지 업로드 성공!",
        "pred": pred,
    }


