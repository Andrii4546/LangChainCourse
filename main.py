import os

from langchain_classic import hub
from dotenv import load_dotenv

from langchain_classic.agents import create_react_agent
from langchain_classic.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

tools = [TavilySearch(api_key=os.getenv("TAVILY_API_KEY"))]

llm = ChatOpenAI(model="gpt-4", temperature=0)
react_prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm=llm, 
                           tools=tools, 
                           prompt=react_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor

def main():
    result = chain.invoke(input={"input": 
        "search for 3 jobs posintion of ML Engineer in the Poland on linkedin and list their details"})
    
    print(result)
if __name__ == "__main__":
    main()
