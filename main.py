# ✅ Install required package
!pip install -Uq openai-agents

# ✅ Import required libraries
import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# ✅ Disable tracing (optional, prevents logging metadata to OpenAI dashboard)
set_tracing_disabled(disabled=True)

# ✅ Configuration
OPENROUTER_API_KEY = "your-api-key-here"  # 🔐 Replace with your actual OpenRouter API key
BASE_URL = "https://openrouter.ai/api/v1"  # OpenRouter's compatible API endpoint
MODEL = "mistralai/mistral-small-3.2-24b-instruct:free"  # Free-tier model available on OpenRouter

# ✅ Create Async client to interact with OpenRouter's LLMs
client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=BASE_URL
)

# ✅ Main async function to define and run your agent
async def main():
    # Step 1: Define the agent with personality and instructions
    agent = Agent(
        name="Jhone",
        instructions="You only respond in English and your name is Jhon from Helpsupport.",
        model=OpenAIChatCompletionsModel(
            model=MODEL,
            openai_client=client
        ),
    )

    # Step 2: Run the agent with a user prompt
    result = await Runner.run(
        agent,
        "What is your name?",
    )

    # Step 3: Print the final output
    print(result.final_output)

# ✅ Run the async function inside Jupyter or Colab using `await` (not `asyncio.run`)
await main()
