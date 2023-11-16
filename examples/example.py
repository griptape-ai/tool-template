from griptape.structures import Agent
from reverse_string_tool import ReverseStringTool


agent = Agent(tools=[ReverseStringTool()])

agent.run("Use the ReverseStringTool to reverse 'Griptape'")
