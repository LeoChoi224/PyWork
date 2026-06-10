# 🟥 스트리밍 응답

# 스트리밍 응답(streaming response)은 일반적인 HTTP 응답과는 다르게
# 데이터를 일정 단위로 나누어 순차적으로 전송하는 방법입니다.

# 이는 대용량 파일을 다루거나 실시간으로 데이터를 전달해야 하는 상황에서 유용합니다.

# 스트리밍 응답의 필요성은 다음과 같습니다.
#   - 메모리 절약: 대용량 파일을 한 번에 로딩하지 않기 때문에 메모리를 절약.
#   - 레이턴시 감소: 클라이언트가 일부 데이터를 먼저 받아볼 수 있으므로
#                사용자 경험이 향상.
#   - 대용량 처리 가능: 데이터가 계속해서 생성되는 경우, 이를 실시간으로 처리할 수 있다.

# FastAPI에서는 StreamingResponse를 사용해 스트리밍 응답을 구현합니다.

# 서버에서 큰 CSV 파일을 생성하고 이를 사용자에게 제공해야 한다고 가정해봅시다.
# 이때 스트리밍 응답을 사용하면 파일을 조각조각 나눠서 전송할 수 있으므로
# 메모리와 네트워크 자원을 효율적으로 사용할 수 있습니다.

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import csv
import io

app = FastAPI()

def csv_streamer():
    data = [
        ["name", "age"],
        ["alice", 32],
        ["bob", 29]]
    output = io.StringIO()  # 실제 디스크에 파일을 쓰지 않고, 메모리 상에서 문자열을 파일처럼 다룰수 있게 하는 '가상 파일 객체'
    writer = csv.writer(output)  # CSV 데이터를 규격에 맞게 안전하게 만들어주는 번역기 역할

    for row in data:
        writer.writerow(row)  # 파이썬 객체 -> CSV 파일 행 작성.
        yield output.getvalue()

        output.flush()  # 버퍼에 남아 있는 내용을 완전히 비움.
        output.truncate(0)  # StringIO 메모리 객체의 내용을 완전히 삭제하여 크기를 0으로 만듬.
        output.seek(0)   # 파일 포인터(커서)를 맨 앞으로 이동.

@app.get("/csv")
def get_csv():
    return StreamingResponse(
        csv_streamer(),  # Stream 객체. generator
        headers= {
            "Content-Type": "text/csv", 
            "Content-Disposition": "attachment; filename=sample.csv",   # 요청한 측이 어떠한 이름으로 파일을 받을지 지정
        }
    )


# csv_streamer() 함수는 yield를 사용하여 데이터를 하나씩 내보내고 있긴 하지만, 
# 예제가 매우 작고 간단하기 때문에 실제로 데이터가 조각조각 나뉘어서 온다는 것을 느끼기 어렵습니다. 
# 스트리밍은 주로 `대용량 데이터`를 처리할 때 빛을 발합니다. 
# 예를 들어 수십 MB, 수백 MB의 큰 파일을 서버에서 생성하여 
# 클라이언트에게 전달해야 하는 경우, 파일을 모두 생성한 후에 전달하는 것이 아니라 
# 생성되는 즉시 조각조각 나눠서 전달합니다.  (이를 chunk 라고 한다.)

# 만약 큰 파일을 전체적으로 메모리에 올려놓고 전송한다면 그만큼의 메모리가 필요하게 되고, 이는 서버에 부담을 줄 수 있습니다. 
# 또한, 파일 전체를 생성하는 데 시간이 오래 걸릴 수 있으므로 사용자는 응답을 기다리는 시간이 길어집니다. 
# 스트리밍 응답을 사용하면 일부 데이터만 생성하고 바로 전송을 시작하므로 이러한 문제를 해결할 수 있습니다. 
# 따라서 "조각조각 나눠서 온다"는 것은 이러한 대용량 데이터 전송 시나리오에서 더 명확하게 이해할 수 있습니다. 
# 예제에서는 데이터가 작아서 한 번에 전송된 것처럼 보이지만, 실제 대용량 데이터 처리에는 큰 이점이 있습니다. 
# 스트리밍 응답은 이처럼 대용량 데이터 처리나 실시간 데이터 전송에 유용합니다. 
# FastAPI의 StreamingResponse를 활용하면 이러한 기능을 간단하게 구현할 수 있습니다.

# 🟡 StreamingResponse는 FastAPI에서 스트리밍 응답을 생성하기 위해 사용되는 클래스입니다. 
# 이 클래스는 큰 데이터를 청크 단위로 나누어 클라이언트에게 순차적으로 전송할 때 유용합니다. 
# 특히 파일 다운로드, 실시간 데이터 전송, 대용량 데이터 처리 등의 경우에 사용됩니다.

# 🟡 주요 옵션과 문법은 다음과 같습니다.

# - 첫 번째 인자: 데이터를 생성하는 제너레이터 함수나 이터러블 객체를 첫 번째 인자로 받습니다. 
#             이 데이터는 HTTP 응답으로 스트리밍됩니다.

# - media_type: media_type은 MIME(Multipurpose Internet Mail Extensions) 타입을 설정하여 
#   응답의 Content-Type 헤더 값을 지정합니다. 예를 들어, CSV 파일의 경우 media_type="text/CSV"로 설정할 수 있습니다.

# 다음은 주로 사용되는 media_type의 목록입니다. 기본적인 MIME 타입들을 나타내며, 
# 사용 목적과 데이터 형식에 따라 적절한 media_type을 선택하여 사용해야 합니다.

# - text/plain: 일반 텍스트 데이터
# - text/html: HTML 문서
# - text/css: CSS 문서
# - text/javascript: 자바스크립트 코드
# - text/csv: CSV 형식의 데이터
# - application/json: JSON 형식의 데이터
# - application/xml:XML 문서
# - application/x-www-form-urlencoded: HTML 폼을 통해 제출된 데이터
# - application/pdf: PDF 문서
# - application/msword: Microsoft Word 문서
# - application/octet-stream: 이진 데이터를 위한 기본값으로, 정해진 타입이 없는 파일을 전송 할 때 사용
# - application/zip: ZIP 압축 파일
# - image/png: PNG 이미지
# - image/jpeg: JPEG 이미지
# - image/gif: GIF 이미지
# - audio/mpeg: MP3 또는 기타 MPEG 오디오
# - audio/ogg: Ogg Vorbis 오디오
# - video/mpeg: MPEG 비디오

# - headers: 추가적인 HTTP 헤더를 딕셔너리 형태로 전달할 수 있습니다. 
#   예를 들어, 파일 다운로드를 위한 Content-Disposition 헤더를 설정할 수 있습니다.

# - background:background 인자에 BackgroundTasks 인스턴스를 전달하여, 
#   스트리밍 작업과 병행하여 실행할 백그라운드 태스크를 지정할 수 있습니다.

# - status_code: 기본적으로 200으로 설정되어 있지만, 
#   필요한 경우 다른 HTTP 상태 코드를 지정할 수 있습니다.


def data_generator():
    for i in range(100):
        yield f"data chunk {i}\n"

@app.get("/stream")
def stream_data():
    generator = data_generator()
    return StreamingResponse(generator, media_type="text/plain")


