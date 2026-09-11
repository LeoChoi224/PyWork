from state import StateA

class CollectorAgent:
    """RSS 피드를 수집하는 에이전트"""

    def __init__(self, llm):
        """생성자. 변수 초기화"""
        self.llm = llm

    def functionA(self):
        """필요한 함수들"""

    # 노드로 사용할 함수. 나중에 workflow의 node로 사용
    def collect_rss(self, state: StateA) -> StateA:
        """RSS 피드를 수집하고 상태를 업데이트"""