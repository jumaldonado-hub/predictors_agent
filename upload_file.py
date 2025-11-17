from vertexai import init
from vertexai.preview import rag
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")
RAG_CORPUS = os.environ.get("RAG_CORPUS_NAME")
GS_BUCKET = os.environ.get("GS_BUCKET")

# Inicializa Vertex AI
init(project=PROJECT_ID, location=LOCATION)

# Corpus existente
corpus_name = RAG_CORPUS#"projects/254863210019/locations/us-west1/ragCorpora/8646911284551352320"

# Ruta en GCS
gcs_path = GS_BUCKET#"gs://hackathon-predictors-agent-staging/skills.txt"

# Configuración de chunking
transformation_config = rag.TransformationConfig(
    chunking_config=rag.ChunkingConfig(
        chunk_size=512,       # tamaño del chunk
        chunk_overlap=50      # solapamiento
    ),
)

# Importar archivo al corpus
result = rag.import_files(
    corpus_name,
    [gcs_path],
    transformation_config=transformation_config,
    max_embedding_requests_per_min=100
)

print(f"Imported {result.imported_rag_files_count} file(s) into corpus: {corpus_name}")
