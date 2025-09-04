import asyncio
import os

from agents import Agent, Runner
from agents import set_default_openai_key

set_default_openai_key(os.getenv("ENDAVA_OPENAI_API_KEY"))


async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant. be VERY concise.",
    )

    result = await Runner.run(agent, "What is the largest country in South America?")
    print(result.final_output)
    # Brazil

    result = await Runner.run(
        agent,
        "What is the capital of that country?",
        previous_response_id=result.last_response_id,
    )
    print(result.final_output)
    # Brasilia


if __name__ == "__main__":
    asyncio.run(main())
