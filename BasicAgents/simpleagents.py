from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv


load_dotenv()


os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


agent = Agent(
    model=Gemini(id="gemini-2.0-flash-001"),  # Changed to a working model
    description="You are an assistant, please reply based on the question",
    tools=[DuckDuckGoTools()],
    markdown=True
)

questions = [
    "Who won the India vs New Zealand Finals in CT 2025?",
    "What are the latest discoveries in quantum computing?",
    "Give me a simple recipe for chocolate chip cookies.",
    "Who is the current Prime Minister of Canada?",
    "Explain the concept of black holes in simple terms."
]


for q in questions:
    print(f"Question: {q}")
    agent.print_response(q)
    print("\n" + "="*50 + "\n")
