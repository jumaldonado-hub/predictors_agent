from vertexai.preview import rag

# Inicializa Vertex AI
rag.init(project="us-con-gcp-sbx-0001190-100925", location="us-west1")

# Listar documentos
docs = rag.list_documents(rag_corpus="projects/254863210019/locations/us-west1/ragCorpora/8646911284551352320")
for d in docs:
    print(d.name)

# Borrar documento
#rag.delete_document(name="projects/254863210019/locations/us-west1/ragCorpora/8646911284551352320/documents/<DOCUMENT_ID>")