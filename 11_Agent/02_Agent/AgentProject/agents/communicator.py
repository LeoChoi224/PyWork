
from state import StateA

class CommunicatorAgent:
    """AI팀의 진행상황을 사용자에게 보고하고, 사용자의 의견을 파악하기 위한 대화를 나누는 에이전트"""

    def __init__(self, llm):
        self.llm = llm

    def communicate(self, state: StateA) -> StateA:
        print("\n\n🧡====== COMMUNICATOR ======")

        return {
            
        }