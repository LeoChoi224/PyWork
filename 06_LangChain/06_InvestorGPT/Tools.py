from dotenv import load_dotenv
load_dotenv()

import os
import requests
import yfinance as yf  # ✅ 추가: 무료 야후 파이낸스 라이브러리
from langchain_openai.chat_models.base import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.tools.base import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper

print(f'\tOPENAI_API_KEY={os.getenv("OPENAI_API_KEY")[:20]}')
alpha_vantage_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
print(f'\t✅ALPHA_VANTAGE_API_KEY={alpha_vantage_api_key[:5]}...')

llm = ChatOpenAI(temperature=0.1)

# ANSI 코드 출력용
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

# ──────────────────────────────────────────────────────────────
# 회사 심볼 
# ─────────────────────────────────────────────────────────────

from langchain.tools import tool

class StockMarketSymbolSearchToolArgsSchema(BaseModel):  # pydantic 모델로 정의
    query: str = Field(
        description="The query you will search for. Example query: Stock Market Symbol for Apple Company"
    )

@tool(
        name_or_callable= "StockMarketSymbolSearchTool",  # tool 이름 
        description="""   
        Use this tool to find the stock market symbol for a company.
        It takes a query as an argument.    
        """,
        args_schema=StockMarketSymbolSearchToolArgsSchema,
)
def search_stock_symbol(query):
    """
    희준이가 심심할때 보는 tool  
    """

    print('🟧 search_stock_symbol 호출] query=', f"{RED}{query}{RESET}")
    ddg = DuckDuckGoSearchAPIWrapper()
    result = ddg.run(query)
    print(f"\n🟧 search_stock_symbol 호출 결과\n{GREEN}{result}{RESET}")
    return result


# class StockMarketSymbolSearchTool(BaseTool):
#     name: Type[str] = "StockMarketSymbolSearchTool"   # tool 이름은 뛰어쓰기 안됨!
#     description: Type[str] = """
#         Use this tool to find the stock market symbol for a company.
#         It takes a query as an argument.
#         """
    
#     args_schema: Type[StockMarketSymbolSearchToolArgsSchema] = StockMarketSymbolSearchToolArgsSchema
    
#     # tool 호출시 실행되는 함수
#     def _run(self, query):
#         print('🟧StockMarketSymbolSearchTool 호출] query=', f"{RED}{query}{RESET}")
#         ddg = DuckDuckGoSearchAPIWrapper()
#         result = ddg.run(query)
#         print(f"\n🟧StockMarketSymbolSearchTool 호출 결과\n{GREEN}{result}{RESET}")
#         return result
    
# ──────────────────────────────────────────────────────────────
# 회사 개요 tool
# ──────────────────────────────────────────────────────────────
class CompanySymbolArgsSchema(BaseModel):
    symbol: str = Field(description="Stock symbol of the company.Example: AAPL,TSLA")

class CompanyOverviewTool(BaseTool):
    name: Type[str] = "CompanyOverview"
    description: Type[str] = """
    Use this to get an overview of the financials of the company.
    You should enter a stock symbol.
    """    

    args_schema: Type[CompanySymbolArgsSchema] = CompanySymbolArgsSchema

    def _run(self, symbol):
        print('🟪CompanyOverviewTool 호출 symbol=', f"{RED}{symbol}{RESET}")
        r = requests.get(f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={alpha_vantage_api_key}")
        result = r.json()
        print(f"\n🟪CompanyOverviewTool 호출 결과\n{GREEN}{result}{RESET}")
        return result

# ──────────────────────────────────────────────────────────────
# ✅ 손익계산서 툴 — yfinance 로 교체 (API Key 불필요, rate-limit 없음)
# ──────────────────────────────────────────────────────────────
class CompanyIncomeStatementTool(BaseTool):
    name: Type[str] = "CompanyIncomeStatement"
    description: Type[str] = """
    Use this to get the annual income statement of a company (via Yahoo Finance).
    You should enter a stock symbol.
    Returns a list of yearly income statement records (Revenue, Gross Profit,
    Operating Income, Net Income, EPS 등).
    """    

    args_schema: Type[CompanySymbolArgsSchema] = CompanySymbolArgsSchema

    def _run(self, symbol):
        print('🟩CompanyIncomeStatementTool(yfinance) 호출 symbol=', f"{RED}{symbol}{RESET}")
        try:
            ticker = yf.Ticker(symbol)
            # 연간 손익계산서 (DataFrame: rows=항목, columns=연도)
            df = ticker.income_stmt

            if df is None or df.empty:
                return f"💢ERROR: No income statement data found for symbol '{symbol}'."

            # LLM 이 읽기 좋게: [{year: '2024-12-31', Total Revenue: ..., Net Income: ...}, ...]
            df_t = df.T  # 연도가 행이 되도록 전치
            df_t.index = df_t.index.astype(str)  # Timestamp -> str (JSON-serializable)
            records = []
            for year, row in df_t.iterrows():
                record = {"fiscalDateEnding": year}
                for key, value in row.items():
                    # NaN 값은 None 으로 정리
                    if value is None or (isinstance(value, float) and value != value):
                        record[str(key)] = None
                    else:
                        record[str(key)] = value
                records.append(record)

            print(f"\n🟩CompanyIncomeStatementTool 호출 결과 ({len(records)} years)\n"
                  f"{GREEN}{records}{RESET}")
            return records

        except Exception as e:
            return f"💢ERROR while fetching income statement for {symbol}: {e}"

# ──────────────────────────────────────────────────────────────
# ✅ 주가 정보 툴 — yfinance 로 교체 (주봉 weekly performance)
# ──────────────────────────────────────────────────────────────
class CompanyStockPerformanceTool(BaseTool):
    name: Type[str] = "CompanyStockPerformance"
    description: Type[str] = """
    Use this to get the recent weekly stock performance of a company (via Yahoo Finance).
    You should enter a stock symbol.
    Returns the last ~6 months of weekly OHLCV bars and summary stats.
    """
    args_schema: Type[CompanySymbolArgsSchema] = CompanySymbolArgsSchema    

    def _run(self, symbol):
        print('🟨CompanyStockPerformanceTool(yfinance) 호출] symbol=', f"{RED}{symbol}{RESET}")
        try:
            ticker = yf.Ticker(symbol)
            # 주봉(weekly) 데이터, 최근 6개월
            hist = ticker.history(period="6mo", interval="1wk", auto_adjust=False)

            if hist is None or hist.empty:
                return f"💢ERROR: No price history found for symbol '{symbol}'."

            # 최근 12주만 가져오기 (토큰 절약)
            hist = hist.tail(12)

            weekly_bars = []
            for ts, row in hist.iterrows():
                weekly_bars.append({
                    "date": ts.strftime("%Y-%m-%d"),
                    "open": round(float(row["Open"]), 4),
                    "high": round(float(row["High"]), 4),
                    "low": round(float(row["Low"]), 4),
                    "close": round(float(row["Close"]), 4),
                    "volume": int(row["Volume"]),
                })

            # 간단한 성과 요약 추가
            first_close = weekly_bars[0]["close"]
            last_close = weekly_bars[-1]["close"]
            change_pct = ((last_close - first_close) / first_close) * 100.0

            result = {
                "symbol": symbol,
                "interval": "1 week",
                "weeks_returned": len(weekly_bars),
                "summary": {
                    "first_close": first_close,
                    "last_close": last_close,
                    "period_change_pct": round(change_pct, 2),
                    "period_high": round(float(hist["High"].max()), 4),
                    "period_low": round(float(hist["Low"].min()), 4),
                },
                "weekly_bars": weekly_bars,
            }

            print(f"\n🟨CompanyStockPerformanceTool 호출 결과\n{GREEN}{result}{RESET}")
            return result

        except Exception as e:
            return f"💢ERROR while fetching stock performance for {symbol}: {e}"



agent = create_agent(
    model=llm,
    tools=[
        # StockMarketSymbolSearchTool(),

        search_stock_symbol,  #@tool 로 정의한 함수는 Tool 객체로 변환됨. 

        # CompanyOverviewTool(),   # 회사 개요 정보
        CompanyIncomeStatementTool(),   # 회사의 손익계산서 정보
        CompanyStockPerformanceTool(),   # 회사의 최근 주가 정보
    ],
)

prompt = """
    Give me financial information on Cloudflare's stock, 
    considering its financials, income statements and stock performance
    and help me analyze if it's a potential good investment.  
    """


if __name__ == "__main__":
    # print(f"내 이름은 {RED}김정준{RESET} {BLUE}김정준{RESET} {YELLOW}김정준{RESET}임다")
    result = agent.invoke({
        "messages": [
            {"role": "user", "content": prompt},
        ],
    })

    print('📌', result['messages'][-1].content)