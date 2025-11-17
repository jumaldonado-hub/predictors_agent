from vertexai.preview import rag
from vertexai import init
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")

# Init Vertex AI
init(project=PROJECT_ID, location=LOCATION)

# Create corpus resource
corpus = rag.create_corpus(display_name="candidate_profiles")
print("RAG Corpus created:", corpus.name)

