from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    try:
        if item_id < 0:
            raise ValueError("음수는 허용되지 않습니다")
    except ValueError as e:
        # 클라이언트에게 400에러와 메세지 응답.
        raise HTTPException(status_code=400, detail=str(e))

# FastAPI는 HTTPException 클래스를 활용하여 API에서 발생하는 예외를 클라이언트에게 명확하게 알릴 수 있도록 도와줍니다.
# 이를 통해 발생할 수 있는 다양한 에러 상황에 대해 HTTP 상태 코드와 에러 메시지를 정의하고 반환할 수 있습니다.
# HTTPException은 FastAPI에서 예외 처리를 위한 기본적이고 강력한 도구입니다.

@app.get("/members/{member_id}")
def read_item(member_id: int):

    if member_id == 42:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There was an Error"} # header 에는 한글, 특수문자 안됨. -> url encoding 하면 가능
        )
    return {"member_id": member_id}

# 🟡 HTTPException의 status_code에 주로 설정하는 HTTP 상태 코드 값은 다음과 같이 정리할 수 있습니다.

# •200: 요청이 성공적으로 처리되었습니다.
# •201: 요청이 성공적으로 처리되었고, 새로운 리소스가 생성되었습니다.
# •400: 서버가 요청을 이해할 수 없음을 나타냅니다.
# •401: 인증이 필요함을 나타냅니다.
# •403: 서버가 요청을 이해했으나 승인을 거부합니다.
# •404: 서버가 요청한 리소스를 찾을 수 없음을 나타냅니다.
# •405: 허용하지 않는 요청 메소드
# •500: 서버 내부에 에러가 발생했음을 나타냅니다.

# 참고: https://developer.mozilla.org/ko/docs/Web/HTTP/Reference/Status
