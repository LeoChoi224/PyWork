# StateGraph 구성 연결

from state import StateA

# from agents.collector import CollectorAgent
# from agents.communicator import CommunicatorAgent

from agents import CollectorAgent, CommunicatorAgent

from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI

def create_workflow(llm: ChatOpenAI) -> StateGraph:

    # 각 작업을 담담할 에이전트 인스턴스 생성
    communicator = CommunicatorAgent(llm)
    collectorAgent = CollectorAgent(llm)

    workflow = StateGraph(StateA)

    # node 추가
    workflow.add_node("collector", collector.collect_rss)
    workflow.add_node("communicator", communicator.communicate)

    # edge 연결

    return workflow.compile()
