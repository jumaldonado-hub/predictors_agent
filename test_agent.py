import vertexai
from vertexai.preview import reasoning_engines
import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")


vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    # api_endpoint="us-central1-aiplatform.googleapis.com",
)

engines = reasoning_engines.ReasoningEngine.list(filter='display_name="predictors_recruiter_agent"')

if not engines:
    print("Reasoning engine for Corporate Analyst missing")
    exit

print("Reasoning engine: " + engines[0].resource_name)
engine = reasoning_engines.ReasoningEngine(engines[0].resource_name)

session = engine.create_session(session_id="session1", user_id='user1')
sessions_data = engine.list_sessions()
print(sessions_data)

# Check if the response is a string and if so, attempt to parse as JSON
if isinstance(sessions_data, str):
    try:
        sessions_data = json.loads(sessions_data)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Received string: {sessions_data}")
        # Handle the error case. maybe return or exit
        exit()

# Now check if it's a dictionary with a 'session_ids' key
if isinstance(sessions_data, dict) and 'session_ids' in sessions_data:
    session_ids = sessions_data['session_ids']
    if not session_ids:  # Check if the list is empty
        print("Creating new session")