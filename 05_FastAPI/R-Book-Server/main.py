from fastapi import FastAPI
import models, database, controllers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="도서관리 CRUD")

# React 프론트엔드 연동을 위한 CORS 설정
# Vite 포트 5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# DDL
# models.Base.metadata.create_all(database.engine)

app.include_router(controllers.router)

@app.get("/")
def root():
    return {"message": "도서관리 CRUD. /board 로 이동해보세요"}