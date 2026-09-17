import asyncio
from mcp import ClientSession

"""
from mcp import ClientSession
MCP 공식 Python SDK의 핵심 클래스로, 서버와의 통신 세션을 담당합니다. 

내부적으로 read/write 스트림을 받아서 아래와 같은 메소드를 제공

    initialize() — 서버와 핸드셰이크
    list_tools(), call_tool() — 도구 조회/호출
    list_resources(), read_resource() — 리소스 조회
    list_prompts(), get_prompt() — 프롬프트 조회


참고로 FastMCP 에서의 Context와는 다른 객체다, Context는 '서버' 쪽에서 쓰는 거고 
ClientSession은 '클라이언트' 쪽에서 서버를 호출할 때 쓰는 거다.
"""

# MCP 의 각 전송계층(transport) 를 사용하기 위한 클라이언트 팩토리 함수.
from mcp.client.streamable_http import streamable_http_client  
from mcp.client.stdio import stdio_client
from mcp.client.sse import sse_client

import httpx
http_client = httpx.AsyncClient(timeout=30.0)   # http 비동기 요청 클라이언트 

url = "http://localhost:8000/mcp"

async def test(url):
    async with streamable_http_client(
        url = url,
        http_client=http_client,
    ) as (read_stream, write_stream, get_session_id):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            # 툴 목록
            tools_result = await session.list_tools()
            print('🥎', type(tools_result))  # ListToolsResult 객체, iterable 하다

            for tool_result in tools_result:
                print('🌐', type(tool_result), tool_result)
                if tool_result[0] == 'tools':
                    tools = tool_result[1]
                    for tool in tools:
                        print('🔨', tool)

            print('🟩' * 20)

            # 툴 호출
            call_tool_result = await session.call_tool(name = 'scrape_page_text', arguments={'url': 'https://www.yes24.com/Product/Goods/196258878'})
            print('🟠',
                  type(call_tool_result), # CallToolResult 객체
                  call_tool_result,  # <- content 속성에 담겨있다.  List[Content]
            )

            print('💛', len(call_tool_result.content), '개 result')
            print('🟣', call_tool_result.content[0].text[:30])   # content[0] 는 TextContent            

asyncio.run(test(url))