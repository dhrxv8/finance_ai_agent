from phi.agent import Agent
#from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import openai, os
from dotenv import load_dotenv
openai.api_key=os.getenv("OPENAI_API_KEY")

#Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="search the web for information",
    model =Groq(id="llama-3.2-90b-vision-preview"),
    tools = [DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
    )

#Financial Agent
finance_agent = Agent(
    name = "Finance AI Agent",
    model = Groq(id= "llama-3.2-90b-vision-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True, company_info=True)],
    
    show_tool_calls=True,
    markdown=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],

)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model = Groq(id= "llama-3.2-90b-vision-preview"),
    instructions=["Always include sources", "Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA", stream=True)
