from workflow import create_workflow
from state import StateA
from config import Config
from utils import *

from langchain_openai import ChatOpenAI

# main.py : 실행 진입점.  LLM/그래프 생성.  초기상태 세팅, 
#           그래프 호출.

def main():

    llm = ChatOpenAI(model=Config.MODEL_NAME)
    graph = create_workflow(llm)

    initial_state = StateA()

    graph.invoke(initial_state)

if __name__ == "__main__":
    main()    