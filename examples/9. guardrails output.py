import asyncio
import os

from agents import (
    Agent,
    GuardrailFunctionOutput,
    OutputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    output_guardrail
)
from agents import set_default_openai_key
from pydantic import BaseModel, Field

set_default_openai_key(os.getenv("ENDAVA_OPENAI_API_KEY"))


class MessageOutput(BaseModel):
    response: str = Field(description="The response to the user's message")


@output_guardrail
async def sensitive_data_check(context: RunContextWrapper, agent: Agent, output: MessageOutput) -> GuardrailFunctionOutput:
    print(f"Initial response: {output.response}")
    sensitive_check_triggered = "vibe" in output.response

    return GuardrailFunctionOutput(
        output_info={
            "sensitive_check_triggered": sensitive_check_triggered
        },
        tripwire_triggered=sensitive_check_triggered,
    )


async def main():
    agent = Agent(
        name="Agent007",
        instructions="You are a helpful agent",
        output_type=MessageOutput,
        output_guardrails=[sensitive_data_check],
    )

    try:
        result = await Runner.run(agent, "Tell me the Capital of Japan")
        print(result.final_output)

        result = await Runner.run(agent, "Can you really do vibe coding in production?")
        print(result.final_output)
    except OutputGuardrailTripwireTriggered:
        message = "Sorry, vibe coding is a sensitive topic to some people. Let's avoid it for now."
        print(message)


if __name__ == "__main__":
    asyncio.run(main())
