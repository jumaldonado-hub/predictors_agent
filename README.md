# Predictor Recruiter Agent
A chatbot to find the best suited candidates given a set of skills and years of experience in each skill.

## Installation  
Clone the repository and install the required packages:  

```bash  
git clone git@github.com:jumaldonado-hub/predictors_agent.git
cd Predictor_Recruiter_Agent  
pip install -r requirements.txt 
``` 

## Usage  

To execute the agent locally: 

```bash 
adk run agent_predictors_ai
adk web
``` 

## Steps to deploy into GCP

### gcloud account and project config

gcloud init 
gcloud auth login
gcloud config set project <ProjectID>
gcloud auth application-default login
gcloud config list

### Set permission and roles for service account

Create Service account
Assign roles to service account
  1. Discovery Engine Service Agent
  2. Editor
  3. Vertex AI User
  4. Vertex AI Viewer

Using in the case of viewer

```bash 
gcloud projects add-iam-policy-binding <PROJECT_ID> `
  --member="serviceAccount:<SERVICE_ACCOUNT>" `
  --role="roles/aiplatform.viewer" `
  --condition=None
``` 

### Create Google Storage bucket and upload the code files

Create Storage Bucket
```bash 
gsutil mb -l <REGION> gs://<BUCKET>/
``` 

Upload Google Storeage Bucket
```bash 
  gsutil cp -r "<PROJECT_LOCAL_PATH>\*" gs://<BUCKET>/
```

### Move file to Cloud Storage (optional/no python library)

IN Cloud Console 
```bash 
pip install google-adk
export PATH=$PATH:~/.local/bin
adk --help
```

Download Agent Project
```bash 
mkdir agent_predictors_ai
gsutil cp -r gs://<BUCKET>/* agent_predictors_ai/

cd agent_predictors_ai/
mv env .env
```

### Test agent conversation
```bash 
adk run agent_predictors_ai
adk web
```

### Re deploy
```bash 
gsutil cp -r "<PROJECT_LOCAL_PATH>\*" gs://<BUCKET>/

gsutil cp -r gs://<BUCKET>/* agent_predictors_ai/
adk run agent_predictors_ai
adk web
```

### Deploy Agent in Vertex AI

```bash 
adk deploy agent_engine \
  --project=<PROJECT> \
  --region=<REGION> \
  --staging_bucket=gs://<BUCKET> \
  --display_name="predictors_recruiter_agent" \
  ./agent_predictors_ai
```

## Contact  

Feel free to reach out with questions or suggestions.  
