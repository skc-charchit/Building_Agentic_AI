import os
from dotenv import load_dotenv
from fireworks import Fireworks

load_dotenv()
client = Fireworks(api_key=os.getenv("FIREWORKS_API_KEY"))

# --- Tool function ---
def get_current_time(city: str) -> dict:
    """
    Mock tool: Returns the current time in a specified city.
    """
    return {"status": "success", "city": city, "time": "10:30 AM"}

# Building Agent Class
class Agent:
    def __init__(self, model, name, description, instruction, tools):
        self.client = client
        self.model = model
        self.name = name
        self.description = description
        self.instruction = instruction
        self.tools = {tool.__name__: tool for tool in tools}

    def run(self, query: str):
        # Build prompt
        prompt = f"""
{self.instruction}

If a tool is needed, respond exactly like:
TOOL: get_current_time(city)

User: {query}
"""

        # Call Fireworks LLM
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        # Get text
        text = response.choices[0].message.content.strip()

        # If model responds with a tool call
        if text.startswith("TOOL:"):
            # Example: "TOOL: get_current_time(London)"
            inside = text.split("TOOL:")[-1].strip()
            tool_name, arg = inside.split("(")
            arg_value = arg.replace(")", "").strip()
            if tool_name in self.tools:
                return self.tools[tool_name](arg_value)

        # Otherwise, return LLM output
        return text
    

# --- Define the agent ---
root_agent = Agent(
    model="accounts/fireworks/models/minimax-m2p1",  # Your model
    name="root_agent",
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
)
