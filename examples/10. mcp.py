import asyncio
import os

from agents import Agent, Runner, trace
from agents import set_default_openai_key
from agents.mcp import MCPServer, MCPServerStdio

set_default_openai_key(os.getenv("ENDAVA_OPENAI_API_KEY"))


async def run(mcp_server: MCPServer):
    agent = Agent(
        name="Agent007",
        instructions="You are a helpful agent that can answer questions about git repository located at '/Users/liviucotoarba/dev/Endava/repos/DavaX-Agents'",
        mcp_servers=[mcp_server],
    )

    message = "Who's the last contributor?"
    print(f"Running: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(f"Answer: {result.final_output}")

    message = "What git branch I'm currently on?"
    print(f"Running: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(f"Answer: {result.final_output}")

    message = "Summarize the last change in the repository."
    print(f"Running: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(f"Answer: {result.final_output}")


async def main():
    async with MCPServerStdio(
            cache_tools_list=True,
            params={"command": "uvx", "args": ["mcp-server-git"]},
    ) as server:
        with trace(workflow_name="MCP Git Example"):
            await run(server)


if __name__ == "__main__":
    asyncio.run(main())
