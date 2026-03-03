from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic
import os

# make sure the Anthropic API key is available before instantiating
api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    raise RuntimeError(
        "ANTHROPIC_API_KEY environment variable is not set. "
        "Please export it before running this script."
    )

model = ChatAnthropic(
    model_name="claude-3-5-sonnet-latest",
    api_key=api_key,
    timeout=None,
    stop=None,
)


def get_weather(city: str) -> str:
    """Get current weather for the given city."""
    return f"The current weather in {city} is sunny with a temperature of 25°C."


agent = create_agent(
    model=model,
    # model = os.environ.get("ANTHROPIC_API_KEY"),
    tools=[get_weather],
    system_prompt="You are a helpful assistant that provides weather information. Use the get_weather tool to fetch the current weather for any city when asked.",
)

response = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "What is the current weather in New York?"}
        ]
    }
)

print(response)
