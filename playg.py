from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app
import openai, os
from dotenv import load_dotenv

#Load Env variables from .env file
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

#Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Perform accurate and comprehensive web searches to retrieve current and reliable information.",
    model=Groq(id="llama-3.2-90b-vision-preview"),
    tools=[DuckDuckGo()],
    instructions=[
        "Always verify information accuracy by cross-referencing multiple sources.",
        "Summarize findings concisely and clearly using bullet points or numbered lists when appropriate.",
        "Always cite the sources used directly in your responses with hyperlinks.",
        "Prioritize recent and credible sources for the most accurate results."
    ],
    show_tool_calls=True,
    markdown=True,
)


#Financial Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.2-90b-vision-preview"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
            company_info=True
        )
    ],
    description=(
        "You are a professional financial analyst providing detailed insights "
        "on stock prices, analyst ratings, financial fundamentals, recent company news, "
        "and comprehensive company profiles."
    ),
    instructions=[
        "Present all data clearly formatted in markdown tables or structured lists for readability.",
        "Include actionable insights based on analyst recommendations and fundamental analysis.",
        "Provide brief summaries of recent company news highlighting significant events impacting stock performance.",
        "Clearly label each section of your analysis (e.g., 'Stock Price', 'Analyst Recommendations', 'Fundamental Analysis', 'Recent News', 'Company Profile').",
        "Always timestamp financial data to indicate its relevance."
    ],
    show_tool_calls=True,
    markdown=True,
)


app=Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playg:app", reload=True)
