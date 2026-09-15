# ToolNode 나 model 에 사용할 tool 들을 정의


from langchain_core.tools import tool   # @tool

@tool
def web_search(query: str):
    """
    주어진 query에 대해 웹검색을 하고, 결과를 반환한다.

    Args:
        query (str): 검색어

    Returns:
        dict: 검색 결과
    """

    return "✅검색결과"