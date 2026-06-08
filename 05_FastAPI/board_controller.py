from fastapi import APIRouter, Request

router = APIRouter(prefix="/board")

@router.get("/write")
def write(request: Request):
    return f"{request.method}, {request.url} 요청"

@router.get("/view")
def view(request: Request):
    return f"{request.method}, {request.url} 요청"

@router.get("/update")
def update(request: Request):
    return f"{request.method}, {request.url} 요청"