# 현재 날자와 시각을 반환하는 MCP서버

from datetime import datetime

from fastmcp import FastMCP
# MCP서버객체 생성
mcp = FastMCP(name="Datetime-MCP")   # 서버의 이름 지정.

@mcp.tool()  # <- 이 함수를 MCP서버의 tool(도구)로 등록
def get_current_datetime() -> str:
    """현재 날짜와 시간을 반환합니다"""
    # ↑ 이때 함수 바로 아래에 작성한 docstring 문자열(주석)을 바탕으로 AI가 함수의 역할과 동작을 이해하게 됩니다. (중요)
    now= datetime.now() 
    return now.strftime("%Y-%m-%d %H:%M:%S") 

# 매개변수에 대한 타입 힌트(str, int, bool 등)는 FastMCP 도구가 올바르게 동작하는 데 반드시 필요합니다.
# 타입 힌트를 명확하게 지정하면 LLM이 각 매개변수에 어떤 데이터 타입을 입력해야 하는지 정확하게 이해할 수 있습니다.
# 또한 FastMCP는 클라이언트로부터 입력받은 데이터가 주석에 명시된 타입과 일치하는지 자동으로 검증해
# 잘못된 데이터가 도구에 전달되는 것을 방지합니다.
@mcp.tool()
def add(a: int, b: int) -> int:  # 도구의 이름을 별도로 지정하지 않으면 함수의 이름이 도구의 이름으로 등록
    """Add two integer numbers together"""
    return a + b

@mcp.tool()
def greet_user(name: str, is_morning: bool = False) -> str:
    """Greet the user with a personalized message.""" # 도구에 대한 설명
    greeting = "Good morning" if is_morning else "Hello"
    return f"{greeting}, {name}!"


if __name__ == "__main__":
    mcp.run()  #  MCP 서버를 실행.

# 참고로 아래가 fastmcp 기본 설정값이다
# mcp.run(
#     transport="stdio",
#     host="127.0.0.1",  # 기본값: 127.0.0.1
#     port=8000,          # 기본값: 8000
#     path="/mcp"         # 기본값: 바로 이 부분! 명시하지 않아도 자동으로 "/mcp"
# ) 


# MCP 서버를 테스트하는 클라이언트로는 앤트로픽에서 제작한 인스펙터 (inspector)와 
# 포스트맨(postman)이 가장 사용하기 쉽습니다. 
# 인스펙터는 Node.js가 설치되어 있다면' 한 줄의 명령으로 웹 클라이언트를 사용할 수 있습니다.

# npx @modelcontextprotocol/inspector

# -----------------
# fastmcp dev inspector server.py


# --------------------------------------------------------------------------
from typing import Annotated
from pydantic import Field

# 매개변수에 메타데이터 적용하여 
# AI각 각 구성요소를 쉽게 이해하고 효율적으로 활용하도록 도와준다.

# @mcp.tool
def 메타데이터(
    name: Annotated[str, Field(description="Name of the user to greet", min_length=2, max_length=20)],
    image_url: Annotated[str, Field(description="URL of the image to process")],
    limit: int = Field(10, description="Maximum number of results", ge=1, le=100),
    query: str = Field(description="Search query string")
):
    ...

# 도구에 대한 메타데이터 제공.
@mcp.tool(
    name="greet_홍묵",   # LLM에 노출되는 도구 이름
    description="Generates a personalized greeting for the user",  # 도구 설명.
    tags = {"greeting", "user"}    # 도구 분류 태그
)
def 도구_메타데이터():
    """docstring 보다 description 이 우선함"""
    return