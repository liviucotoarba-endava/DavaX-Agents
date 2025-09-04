import asyncio
import os

from agents import run_demo_loop
from agents import set_default_openai_key, Agent

set_default_openai_key(os.getenv("ENDAVA_OPENAI_API_KEY"))


async def main() -> None:
    agent = Agent(name="Agent007", instructions="You are a helpful assistant.")
    await run_demo_loop(agent)


if __name__ == "__main__":
    asyncio.run(main())
