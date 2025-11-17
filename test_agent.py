from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="A helpful assistant to answer user questions.",
    instruction="Answer user questions based on your knowledge and capabilities.",
)