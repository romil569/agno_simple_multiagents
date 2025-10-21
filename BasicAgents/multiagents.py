from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
import os
from dotenv import load_dotenv


load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")


web_agent = Agent(
    name="Web Agent",
    role="Search the web for latest news",
    model=Gemini(api_key=google_api_key),
    tools=[DuckDuckGoTools()],
    instructions="Search online for relevant information and always include sources."
)


finance_agent = Agent(
    name="Finance Agent",
    role="Provide financial data and insights",
    model=Gemini(api_key=google_api_key),
    tools=[YFinanceTools()],
    instructions="Provide stock prices, fundamentals, and analyst recommendations in tables."
)

def interactive_multiagent():
    print("=== Multi-Agent Q&A Chatbot ===")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Exiting...")
            break

        
        if any(keyword in user_input.lower() for keyword in ["stock", "finance", "price", "market"]):
            finance_result = finance_agent.print_response(user_input)
            print(f"\nFinance Agent:\n{finance_result}\n")
        elif any(keyword in user_input.lower() for keyword in ["news", "latest", "update"]):
            web_result = web_agent.print_response(user_input)
            print(f"\nWeb Agent:\n{web_result}\n")
        else:
            web_result = web_agent.print_response(user_input)
            finance_input = f"Based on the following info:\n{web_result}\nProvide financial insights if applicable."
            finance_result = finance_agent.print_response(finance_input)
            print(f"\nWeb Agent:\n{web_result}\n")
            print(f"Finance Agent:\n{finance_result}\n")

if __name__ == "__main__":
    interactive_multiagent()
