import asyncio
import os

from agents import Agent, Runner, ModelSettings, OpenAIChatCompletionsModel
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.getenv("ENDAVA_OPENAI_API_KEY"))


async def main():
    agent = Agent(
        name="Agent007",
        instructions="You are a helpful agent",
        model=OpenAIChatCompletionsModel(model="gpt-4.1", openai_client=client),
        model_settings=ModelSettings(max_tokens=100)
    )

    result = await Runner.run(agent, "Best places to eat in Tokyo?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
