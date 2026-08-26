from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from model.iris_model import predict_iris

# 템플릿 설정
templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static",  StaticFiles(directory="static"), name="static")

class InputData(BaseModel):
    sepal_length: float
    petal_width: float
    sepal_width: float
    petal_length: float


@app.get("/")
def form(request: Request):
    return templates.TemplateResponse(
        request, 
        "irisform.html"
    )


@app.post("/predict_iris")
def class_iris(body: InputData):
    print('✅ body:', body)

    result = predict_iris(
        body.sepal_length,
        body.sepal_width,
        body.petal_length,
        body.petal_width,
    )

    return {"result": result}

