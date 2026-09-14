from workflow import create_workflow
from state import NewsState
from config import Config
from dotenv import load_dotenv
load_dotenv()

import os
import logging
import asyncio
from datetime import datetime
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

from workflow import create_workflow
from config import Config
from state import NewsState

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# main.py : 실행 진입점.  LLM/그래프 생성.  초기상태 세팅, 
#           그래프 호출.

async def main():
    """Google News AI 멀티에이전트 시스템의 메인 실행 함수"""
    print(
        """
Google News AI 멀티에이전트 시스템
RSS 수집 → AI 요약 → 카테고리 분류 → 리포트 생성
"""
    )

    try:

        if not Config.validate():
            raise ValueError("API 키가 설정되지 않았습니다.")

        print("뉴스 처리 시작")
        print("=" * 60)

        llm = ChatOpenAI(
            model=Config.MODEL_NAME,
            max_tokens=Config.MAX_TOKENS,
            api_key=Config.OPENAI_API_KEY,
        )
        graph = create_workflow(llm)

        initial_state = NewsState(
            messages=[HumanMessage(content='Google News RSS 처리를 시작합니다')]
        )

        final_state = await graph.ainvoke(initial_state)

        if not final_state.get("final_report"):
            print("\n생성된 보고서가 없습니다.")
            return

        os.makedirs(Config.OUTPUT_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(Config.OUTPUT_DIR, f"news_report_{timestamp}.md")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_state["final_report"])

        print("\n" + "=" * 60)
        print("처리 완료")
        print("=" * 60)
        print(f"\n보고서가 저장되었습니다: {filename}")
        print(f"처리된 뉴스: {len(final_state.get('summarized_news', []))}건")
        print("\n보고서 미리보기:")
        print("-" * 60)
        print(final_state["final_report"][:500] + "...")        


    # ⑥ 예외 처리 - 사용자 중단과 일반 오류를 구분하여 처리
    #   예외 처리에서는 두 가지 예외 상황을 처리합니다. KeyboardInterrupt는 사용자가 Ctrl+C 로 
    #   프로그램을 중단했을 때 발생합니다. 그 외의 모든 예외는 로거를 통해 상세한 스택 트레이스를 
    #   기록하고 사용자에게 오류 메시지를 표시합니다.
    except KeyboardInterrupt:
        print("\n\n사용자에 의해 중단되었습니다.")
    except Exception as e:
        logger.exception("실행 중 오류 발생")
        print(f"\n오류 발생: {e}")
    

if __name__ == "__main__":
    asyncio.run(main())