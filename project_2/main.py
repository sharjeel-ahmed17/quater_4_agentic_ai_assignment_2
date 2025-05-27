from agents import Agent , Runner , OpenAIChatCompletionsModel , AsyncOpenAI , function_tool
from agents.run import RunConfig
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=provider
)

config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

@function_tool
def get_capital_of_country(country: str) -> str:
    capitals = {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid"
    }
    return capitals.get(country, "Unknown")

@function_tool
def get_population_of_country(country: str) -> int:
    populations = {
        "France": 65273511,
        "Germany": 83783942,
        "Italy": 60244639,
        "Spain": 46754778
    }
    return populations.get(country, 0)  
agent  = Agent(
    name="ai assistant",
    instructions="You are a helpful AI assistant.",
    model=model,
    tools=[get_capital_of_country, get_population_of_country]
)

result = Runner.run_sync(
    agent , 
    "What is the population of Spain?",
    # "What is the capital of Spain?",
    run_config=config
)

print(f"Result: {result.final_output}")