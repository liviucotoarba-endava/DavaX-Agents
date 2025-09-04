import asyncio
import os

from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
)
from agents import set_default_openai_key
from pydantic import BaseModel

set_default_openai_key(os.getenv("ENDAVA_OPENAI_API_KEY"))


class MathHomeworkOutput(BaseModel):
    reasoning: str
    is_math_homework: bool


guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking you to do their math homework.",
    output_type=MathHomeworkOutput,
)


@input_guardrail
async def math_guardrail(context: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, input, context=context.context)
    final_output = result.final_output_as(MathHomeworkOutput)

    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=final_output.is_math_homework,
    )


async def main():
    agent = Agent(
        name="Agent007",
        instructions="You are a helpful agent",
        input_guardrails=[math_guardrail],
    )

    try:
        result = await Runner.run(agent, "Tell me the Capital of Japan")
        print(result.final_output)

        result = await Runner.run(agent, "How much is 123 * 321?")
        print(result.final_output)
    except InputGuardrailTripwireTriggered:
        message = "Sorry, I can't help you with your math homework."
        print(message)


if __name__ == "__main__":
    asyncio.run(main())
