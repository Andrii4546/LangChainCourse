import os

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

import dotenv

dotenv.load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search(query: str) -> str:
    """Search the web for the query

    Args:
        query (str): The query to search for

    Returns:
        str: the results of the search
    """
    
    print(f"Searching for: {query}")
    return tavily_client.search(query)

llm = ChatOpenAI(model="gpt-5")
tools = [search]
agent = create_agent(model=llm, tools=tools)
def main():
    result = agent.invoke({"messages": HumanMessage(content="search 3 jobs positions for a ML/AI engineer in the Poland on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()
