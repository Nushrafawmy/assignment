from elasticsearch import Elasticsearch
from app.config import ELASTICSEARCH_URL, ELASTICSEARCH_INDEX

# Initialize ES client
es = Elasticsearch(ELASTICSEARCH_URL)

def init_index():
    # Make sure ELASTICSEARCH_INDEX is not None
    if not ELASTICSEARCH_INDEX:
        raise ValueError("ELASTICSEARCH_INDEX is not set")

    # Check if the index exists
    if not es.indices.exists(index=ELASTICSEARCH_INDEX):
        # Create the index if it doesn't exist
        es.indices.create(index=ELASTICSEARCH_INDEX)
        print(f"Created index: {ELASTICSEARCH_INDEX}")
    else:
        print(f"Index already exists: {ELASTICSEARCH_INDEX}")
