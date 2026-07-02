import json
from fastapi import Request
from collections.abc import AsyncGenerator

from Tools import agent
# 위 agent를 '스트리밍 응답'을 위한 하무들
#   SSE(Server Sent Event)방식으로 응답해보겠습니다.

def _extract_text(content) -> str:
    """LangChain 메시지 청크(chunk)의 content에서 순수 텍스트만 뽑아내는 헬퍼 함수.

    LLM 스트리밍 청크의 content는 모델/상황에 따라 형태가 다를 수 있다:
      1) 단순 문자열인 경우: "안녕하세요"
      2) 리스트(멀티모달/구조화된 응답)인 경우:
         예) [{"type": "text", "text": "안녕"}, {"type": "image", ...}]
         이 중 텍스트 블록만 모아서 이어 붙인다.
    그 외의 타입(None 등)이면 빈 문자열을 반환해 안전하게 처리한다.
    """
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict) and block.get('type') == 'text':
                parts.append(block.get('text', ""))
        return "".join(parts)
    
    return ""

def _sse(event: str, data: dict) -> str:
    """SSE(Server-Sent Events) 규격에 맞는 문자열 한 덩어리를 만든다.

    SSE 프로토콜 형식:
        event: <이벤트 이름>
        data: <JSON 문자열>
        \n\n   (빈 줄 두 개로 메시지 종료를 표시)

    프론트엔드(HomePage.jsx)는 이 정확한 형식("event: ...\\ndata: ...\\n\\n")을
    그대로 파싱하므로, 줄바꿈 개수를 임의로 바꾸면 안 된다.
    ensure_ascii=False로 한글이 유니코드 escape(\\uXXXX) 없이 그대로 전송되도록 한다.
    """
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"

async def stream_company_analysis(company_name: str, request: Request) -> AsyncGenerator[str, None]:

    user_message = f"{company_name} 회사를 분석해줘. 투자할만한 가치가 있는지 평가해줘."

    try:
        async for event in  agent.astream_event(
            {"messages": [{"role": "user", "content": user_message}]},
            version="v2",
            ):

            # 사용자가 '취소'버튼을 누르거나, 브라우저 탭 닫으면 연결이 끊긴다.
            #    따라서, 매 event마다 '연결상태' 확인해서. 끊겼다면 for 루프 탈출 (break)
            if await request.is_disconnected():
                break

            kind = event.get('event')

            if kind == 'on_chat_model_stream':
                # LLM이 토큰 하나를 생성할 때마다 발생하는 이벤트
                text = _extract_text(event['data']['chunk'].content)
                if text:
                    # SSE 응답
                    yield _sse("token", {"content", text})

            elif kind == "on_tool_start":
                # Agent 가 도구(tool) 를 호출하기 시작할 때 발생하는 이벤트
                # event.get("name")에는 호출된 도구의 이름이 들어있다 (예: 검색 도구, 계산 도구 등).
                # 프론트엔드는 이를 받아 "🔧 ○○ 도구를 사용 중입니다..." 같은 상태 텍스트를 보여준다.
                yield _sse("tool_start", {"tool": event.get("name")})

            elif kind == "on_tool_end":
                # 도구 실행이 끝났을 때 발생하는 이벤트.
                yield _sse("tool_end", {"tool": event.get("name")})
        
        else:
            # for...else: for 루프가 break 없이 "정상적으로" 모든 이벤트를 다 순회했을 때만 실행되는 블록.
            # 즉, 중간에 클라이언트 연결이 끊겨 break된 경우는 이 else 블록을 타지 않는다.
            # 정상적으로 Agent 실행이 끝났음을 의미하므로 "done" 이벤트를 보낸다.
            yield _sse("done", {})
            return
        
        # 위의 for...else에서 return되지 않고
        # for 루프 중간에 break로 빠져나온 경우 (ex: 사용자 취소)
        yield _sse("cancelled", {})

    except Exception as e:
        # Agent 실행 중 예외(LLM 호출 실패, 도구 오류 등)가 발생하면
        # 서버가 죽지 않도록 잡아서 "error" 이벤트로 클라이언트로 알려준다.
        yield _see("error", {"message":str(e)})

