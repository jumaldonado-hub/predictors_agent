from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag


# Create the RAG agent
root_agent = Agent(
    model="gemini-2.5-flash",
    name="rag_agent",
    description="Agent that recommends candidates based on job descriptions.",
    instruction="""
    You are an expert technical recruiter. Use the candidate profiles in memory to recommend the best matches for a given job description.
    Always provide clear reasoning for why each candidate fits the role.
    """,
    tools = [google_search]
)


# Function to recommend candidates
def recommend_candidates(job_description: str):
    query = f"Job description: {job_description}\nSelect the most suitable candidates from the profiles in memory."
    return {"result": root_agent.run(query)}