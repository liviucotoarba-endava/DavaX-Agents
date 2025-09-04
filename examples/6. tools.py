import asyncio
import os

from agents import Agent, Runner, function_tool
from agents import set_default_openai_key
from pydantic import BaseModel

set_default_openai_key(os.getenv("ENDAVA_OPENAI_API_KEY"))


class Weather(BaseModel):
    city: str
    temperature_range: str
    conditions: str


@function_tool
def get_weather(city: str) -> Weather:
    print("[debug] get_weather called")
    return Weather(city=city, temperature_range="14-20C", conditions="Sunny with wind.")


agent = Agent(
    name="Agent007",
    instructions="You are a helpful agent",
    tools=[get_weather],
)


async def main():
    result = await Runner.run(agent, input="What's the weather in Tokyo?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
