from dotenv import load_dotenv
load_dotenv()

import os
from langchain_openai.chat_models.base import ChatOpenAI

# sql agent 생성 함수
from langchain_community.agent_toolkits.sql.base import create_sql_agent

# SQLDatabaseToolkit for interacting with SQL databases.
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

# SQLAlchemy wrapper around a database.
from langchain_community.utilities.sql_database import SQLDatabase

file_dir = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.join(file_dir, 'movies.sqlite')

# DB파일로부터 SQLDatabase 생성
db = SQLDatabase.from_uri(f"sqlite:///{db_path}")

# ToolKit 생성 (DB 와 LLM 으로부터 생성)
llm = ChatOpenAI(temperature=0.1)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# agent 생성 (LLM 과 toolkit 으로부터 생성)
agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    agent_type="tool-calling",
    verbose=True,
)

# agent 호출
# agent.invoke("Give me 5 directors that have the highest grossing films.")

# for tool in toolkit.get_tools():
#     print('🐹', tool)

# "평점은 가장 높지만 예산이 낮았던 영화를 알려줘"
agent.invoke("Give me the movies that have the highest votes but the lowest budgets and give me the name of their directors.")













