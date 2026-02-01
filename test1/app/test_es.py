from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
index_name = "rbcapp1-health"

print("Cluster info:", es.info())
print("Index exists?", es.indices.exists(index=index_name))
