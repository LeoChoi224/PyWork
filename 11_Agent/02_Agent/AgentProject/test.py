from dotenv import load_dotenv
load_dotenv()

import os
import logging
import asyncio

from config import Config
from state import NewsState

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

async def test():
    """테스트"""
    from langchain_openai import ChatOpenAI
    state = NewsState()
    llm = ChatOpenAI(temperature=0.1)

    from agents.collector import RSSCollectorAgent
    agent = RSSCollectorAgent()
    await agent.collect_rss(state)
    print('🟠collect_rss() 후', len(state.raw_news), '개 뉴스 수집')
    print("\n".join([f"{news['title']}-{news['source']}-{news['published_kst']}" for news in state.raw_news[:5]]))

    from agents.summarizer import NewsSummarizerAgent
    agent = NewsSummarizerAgent(llm)
    await agent.summarize_news(state)
    print('🌐summarize_news() 후')
    print("\n".join([f"{news['ai_summary'][:30]}"  for news in state.summarized_news[:5] ]))
       

    from agents.organizer import NewsOrganizerAgent
    agent = NewsOrganizerAgent(llm)
    await agent.organize_news(state)
    print('🎃organize_news() 후\n', 
          "\n".join([f"{category}-{len(news_list)}개"for category, news_list in state.categorized_news.items()]) )

    from agents.reporter import ReportGeneratorAgent
    agent = ReportGeneratorAgent()
    await agent.generate_report(state)
    print('📙generate_report() 후')
    print(state.final_report)

if __name__ == "__main__":
    asyncio.run(test())