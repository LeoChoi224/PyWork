# uvicorn main:app --reload

from fastapi import FastAPI, Request, File, UploadFile
from fastapi.staticfiles import StaticFiles  # 1. 추가
from typing import List
from model.cifar10 import *
import os
import shutil

app = FastAPI()

# static 파일 설정
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

# 템플릿 설정
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates", auto_reload=True)

# 'uploads' 폴더를 '/upload' 경로로 서빙하도록 설정
# 예: uploads/image.jpg 파일은 http://127.0.0.1:8000/files/image.jpg 로 접근 가능
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)
app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ↓ multiple 파일(들)을 imagefiles 라는 name으로 받아온다
@app.post("/upload")
async def upload_image(imagefiles: List[UploadFile] = File(...)):
    file_paths = []
    urls = []

    for imagefile in imagefiles:
        filename = os.path.basename(imagefile.filename)
        file_path = os.path.join(UPLOAD_DIR, filename)

        with open(file_path, "wb") as f:
            shutil.copyfileobj(imagefile.file, f)

        file_paths.append(file_path)
        urls.append(f"/files/{filename}")

    labels = predict_images(file_paths)
    results = [{"url": url, "label": label} for url, label in zip(urls, labels)]

    return {"results": results}

