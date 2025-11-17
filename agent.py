from google.adk.agents import Agent
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Vertex AI configuration from environment
#PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
#LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")
RAG_CORPUS = os.environ.get("RAG_CORPUS_NAME")

# Retrieval corpus 
rag_corpus = RAG_CORPUS#"projects/254863210019/locations/us-west1/ragCorpora/8646911284551352320"

# Config RAG
candidate_profiles_retrieval = VertexAiRagRetrieval(
    name="retrieve_candidate_profiles",
    description="Retrieve candidate profiles relevant to the job description from the RAG corpus.",
    rag_resources=[
        rag.RagResource(rag_corpus=rag_corpus)
    ],
    similarity_top_k=10,
    vector_distance_threshold=0.6,
)

# Agent definition
root_agent = Agent(
    model="gemini-2.5-flash",
    name="predictors_recruiter_agent",
    instruction=""" 
        You are an expert technical recruiter specialized in the technology industry.
        Your task is to:
        1. Use the RAG tool to retrieve candidate profiles relevant to the provided job description.
        2. Select at least 3 candidates that best match the role.
        3. For each candidate, provide:
        - Name (or identifier if available)
        - Key skills and technologies
        - A professional explanation of why they fit the role
        - A fit score (percentage) based on relevance to the job description
        4. Ensure the tone is professional and concise.
    """,
    tools=[candidate_profiles_retrieval],
)

# Function to recommend candidates
def recommend_candidates(job_description: str):
    query = f"""
        Job description:
        {job_description}

        Please find the top 3 candidates that best match this role.
        Calculate a fit score for each candidate (0-100%) based on skills, tools, and experience alignment.
        Return the results in a structured format:
        Candidate Name | Fit Score | Key Skills | Explanation
        """
    return {"result": root_agent.run(query)}