from langchain_openai.chat_models.base import ChatOpenAI
from langchain.agents import create_agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(temperature=0.1)
agent = create_agent(model=llm)

inputs = {"messages": [{"role": "user", "content": "Python 언어에 대해 설명해봐"}]}

if __name__ == "__main__":
    print('🟦', type(agent)) # CompiledStateGraph 객체

    # 🟦 일반 호출
    """
    ● invoke(input, config=None)	그래프를 동기로 끝까지 실행하고 '최종 결과'만 반환
    ● ainvoke(input, config=None)	invoke 의 비동기 버젼 (FastAPI async 라우터에서는 이걸 써야 함)
    """
    # result = agent.invoke(inputs)
    # print(result['messages'][-1].content)

    # 🟦 스트리밍 (중간 과정도 streaming 받기)
    """
    ● stream(input, config=None, stream_mode=...)	동기 스트리밍. 
        stream_mode로 
            "values"(매 스텝 전체 상태),   State 값
            "updates"(스텝별 변경분만), 
            "messages"(LLM 토큰), 
            "debug" 등을 선택
        -> Iterable 리턴

    ● astream(input, config=None, stream_mode=...)  stream 의 비동기 버젼

    ● astream_events(input, config=None, version="v2")	
        그래프 내부의 모든 콜백 이벤트(on_chat_model_stream, on_tool_start 등)를 잘게 쪼개서 흘려줌. 
        Runnable 인터페이스에서 옴
    """

    # for chunk in agent.stream(inputs):  
    #     print('🟡', chunk)

    # 🟦 messages 모드 (토큰 단위 스트리밍)
    #   stream(stream_mode='messages')
    # LLM이 생성하는 토큰을 실시간으로 받고 싶다면 stream_mode="messages"를 사용

    # for token, metadata in agent.stream(inputs, stream_mode='messages'):
        # token: AIMessageChunk 객체
        # metadata: dict

        # print('🟡', type(token), '🔵', type(metadata))
        # print('\t', token)

        # if token.content:
        #     print(token.content, end="", flush=True)


    # 🟦 astream_events -> AsyncIterator 리턴
    # agent.astream_events: Agent의 실행 과정(LLM 토큰 생성, 도구 호출 시작/종료 등)을
    # 세밀한 이벤트 단위로 스트리밍해주는 LangGraph/LangChain의 API.
    # version="v2"는 이벤트 스키마 버전을 의미한다(v1과 필드 구조가 다름).

    async def run_astream():
        async for event in agent.astream_events(inputs, version='v2'):
            # event 는 dict 다  version='v2'
            # {
            #     "event": "on_chat_model_stream",   # 이벤트 종류
            #     "name": "ChatOpenAI",              # 어떤 Runnable이 발생시켰는지
            #     "run_id": "...",                   # 이 실행의 고유 ID
            #     "parent_ids": [...],               # 상위 실행 체인 (v2부터 채워짐)
            #     "tags": [...],
            #     "metadata": {...},
            #     "data": {...},                     # 실제 내용물, 이벤트 종류마다 다름
            # }

            kind = event.get('event')
            # print('🟡 event:', kind)
            if kind == 'on_chat_model_stream':
                content = event["data"]['chunk'].content
                # print('🟡 data:', content)
                if content:
                    print(content, end='', flush=True)

    asyncio.run(run_astream())