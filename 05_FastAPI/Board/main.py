from fastapi import FastAPI
import models, database, controllers

app = FastAPI(title="게시판CRUD")


# DDL
models.Base.metadata.create_all(database.engine)

app.include_router(controllers.router)

@app.get("/")
def root():
    return {"message": "게시판CRUD. /board/list 로 이동해보세요"}