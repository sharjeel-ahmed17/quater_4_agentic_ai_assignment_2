from agents import Agent , Runner , OpenAIChatCompletionsModel  , AsyncOpenAI
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
    openai_client=provider,
)

config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True

)

agent = Agent(
    name="Ai aisistant",
    instructions="You are a helpful AI assistant.",
    model=model,
)


result = Runner.run_sync(
    agent,
    "What is the capital of France?",
    run_config=config,

)
print(result.final_output)