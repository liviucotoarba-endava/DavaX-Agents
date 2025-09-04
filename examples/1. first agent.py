import os

from agents import set_default_openai_key, Agent, Runner, ModelSettings

set_default_openai_key(os.getenv("ENDAVA_OPENAI_API_KEY"))

agent = Agent(name="Agent007", instructions="You are a helpful agent", model="gpt-4.1", model_settings=ModelSettings(max_tokens=100))
result = Runner.run_sync(agent, "Tell me a joke.")
print(result.final_output)
