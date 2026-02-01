
from app.db.elastic import es
from app.config import ELASTICSEARCH_INDEX

def save_status(payload: dict):
    es.index(index=ELASTICSEARCH_INDEX, document=payload)

def get_all_status():
    result = es.search(index=ELASTICSEARCH_INDEX, size=1000)
    services = {}

    for hit in result["hits"]["hits"]:
        src = hit["_source"]
        services[src["service_name"]] = src["service_status"]

    if not services:
        return None

    app_status = "UP" if all(v == "UP" for v in services.values()) else "DOWN"

    return {
        "application_name": "rbcapp1",
        "application_status": app_status,
        "services": services
    }

def get_service_status(service_name: str):
    result = es.search(
        index=ELASTICSEARCH_INDEX,
        query={"match": {"service_name": service_name}},
        size=1
    )
    if not result["hits"]["hits"]:
        return None
    return result["hits"]["hits"][0]["_source"]
