import asyncio
import os

from agents import Agent, Runner, ModelSettings
from agents.extensions.models.litellm_model import LitellmModel


async def main():
    agent = Agent(
        name="Agent007",
        instructions="You are a helpful agent",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=os.getenv("GEMINI_API_KEY")),
        model_settings=ModelSettings(max_tokens=100)
    )

    result = await Runner.run(agent, "Explain how AI works in a few words")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
