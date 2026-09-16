from fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP()

# MCP서버의 구성요소 3가지: tool, resource, prompt

# 리소스는 서버가 외부 데이터나 파일, 데이터베이스 등에서 정보를 가져올 수 있도록
# 지원하는 역할을 합니다. 즉, 도구가 동작하는 데 필요한 데이터 소스를 제공하며,
# 서버에서 관리하는 데이터나 외부 저장소에 접근할 수 있는 함수로 구현됩니다.
# 예를 들어, 특정 파일의 내용을 읽거나 데이터베이스에서 테이블 목록을 가져오는 함수가
# 리소스에 해당합니다.
# 이는 RAG 기반 시스템에서 LLM의 지식 확장에 매우 중요한 역할을 합니다.

@mcp.resource(uri = "resource://greeting")  # 리소스 주소
def get_greeting() -> str:
    """간단한 인사말을 제공합니다"""
    return "안녕하세요~ FastMCP 리소스입니다"

# 가령 클라이언트가 특정 리소스 URI을 요청하면 FastMCP는 다음과 같이 동작합니다.

# 1. 리소스 정의 검색: 요청된 URI에 해당하는 리소스 정의를 찾습니다.

# 2. 함수 실행(동적 리소스의 경우): 리소스가 함수로 정의된 동적 리소스라면 해당 함수를 실행합니다.

# 3. 콘텐츠 반환: 실행 결과로 얻은 콘텐츠(텍스트, JSON, 바이너리 데이터 등)를 클라이언트에 반환합니다.


# 리소스 메타데이터
@mcp.resource(
        uri="data://app-settings",
        name="AppSettings",   # 리소스 이름.
        description="애플리케이션 설정 정보를 JSON으로 제공합니다.",   # AI가 읽는 설명
        mime_type="application/json",   # 응답 데이터 형식: JSON
        tags = {"settings", "config", "public"},   # 리소스 분류 태그
)
def load_app_settings() -> dict:  
    """내부 함수 설명 (위의 'description'이 우선합니다)."""
    return {
        "theme": "light",
        "version":"1.2.1",
        "options": ["tools", "resources", "notifications"],
    }

# 프롬프트는 사용자가 LLM에게 전달하는 명령어나 질문을 미리 정의해두는 템플릿입니다.
# 클라이언트가 특정 작업을 요청할 때 프롬프트를 통해 LLM이 어떤 방식으로 응답해야 하는지,
# 어떤 정보를 참고해야 하는지 등을 안내할 수 있습니다.
# 예를 들어, 문서 오류 메시지를 디버깅하거나 특정 양식에 맞춰 답변을 생성하도록
# 유도하는 프롬프트가 있습니다. 프롬프트는 사용자 경험을 개선하고,
# LLM의 출력을 일관성 있게 만드는 데 기여합니다.


@mcp.prompt(
    name="analyze_data_request", #프롬프트 명칭
    description="Generates a data analysis request with user-specified options.", #설명
    tags={"analysis", "data"} #태그
)
def data_analysis_prompt(
    data_uri: str = Field(description="Resource URI containing the target dataset."),
    analysis_type: str = Field(default="summary", description="Desired analysis type.")
) -> str:
    """이 docstring은 description이 있을때 무시됨"""
    return f"Analyze the dataset at {data_uri} using the '{analysis_type}' method."


from typing import Annotated
@mcp.tool(
    name="User_Profile",
    description="Generate User Profile",
)
def 메타데이터(
    name: Annotated[str, Field(description="Name of the user to greet", min_length=2, max_length=20)],
    image_url: Annotated[str, Field(description="URL of the image to process")],
    limit: int = Field(10, description="Maximum number of results", ge=1, le=100),
    query: str = Field("", description="Search query string")
):
    return {
        "name": name,
        "image_url": image_url,
        "limit": limit,
        "query": query,
    }


