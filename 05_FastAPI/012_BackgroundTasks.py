# 🟥 백그라운드 태스크

# FastAPI의 BackgroundTasks는 주로 긴 작업을 별도로 처리하는 데 사용합니다.
# 이는 HTTP 응답을 먼저 보내고 나서도 서버에서 계속 작업을 실행할 수 있게 해줍니다.
# 이러한 방식은 사용자 경험을 향상시키며, 서버 리소스를 효율적으로 활용할 수 있습니다.
# 예를 들어, 사용자가 회원가입을 하면 "회원가입을 환영합니다"라는 이메일을 보내야 할 수 있습니다.
# 이메일을 보내는 작업은 시간이 걸릴 수 있기 때문에 이 작업을 별도의 배경 작업으로 처리하고,
# 사용자에게는 즉시 응답을 보낼 수 있습니다.

# 백그라운드 태스크가 필요한 이유는 다음과 같습니다.

# - 비동기 처리: 메인 로직을 멈추지 않고 다른 작업을 병렬로 실행할 수 있습니다.
# - 리소스 최적화: 주요 로직과 무관한 작업을 분리하여 리소스를 효율적으로 사용할 수 있습니다.

from fastapi import FastAPI, BackgroundTasks
from datetime import datetime
import time

app = FastAPI()

def write_log(message: str):
    time.sleep(3)
    with open("log.txt", "a") as f:    # "append"
        f.write(f"{message}\n")

# BackgroundTasks 를 함수의 매개변수로 추가
@app.get("/")
# def read_root(background_tasks: BackgroundTasks):
def read_root():
    now = datetime.now()
    # background_tasks.add_task(write_log, f"root endpoint was accessed {now}")
    write_log(f"root endpoint was accessed {now}")
    return {"message": f"Hello World {now}"}        


@app.get("/background/")
def background(background_tasks: BackgroundTasks):
    now = datetime.now()
    background_tasks.add_task(write_log, f"root endpoint was accessed {now}")
    return {"message": f"Hello World {now}"}        

# BackgroundTasks는 FastAPI의 내장 클래스로, 이를 통해 별도의 스레드에서 실행될 작업들을 관리하고 예약할 수 있습니다. 
# 이 클래스는 FastAPI 애플리케이션에서 다양한 백그라운드 태스크를 쉽게 다룰 수 있도록 설계되었습니다. 
# 특히, I/O 작업이나 시간이 오래 걸리는 작업에 유용합니다.

# add_task()는 BackgroundTasks 클래스의 메서드입니다. 
# 이 메서드를 사용하면 실행할 함수와 그 함수에 전달할 매개변수를 지정할 수 있습니다. 
# 매개변수는 위치 기반 또는 키워드 기반으로 전달합니다.

# background_tasks.add_task(func, *args, **kwargs)
# - func: 실행할 함수
# - *args: 함수에 전달할 위치 기반 매개변수
# - **kwargs: 함수에 전달할 키워드 기반 매개변수
