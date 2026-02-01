
from fastapi import FastAPI
from app.db.elastic import init_index
from app.routes import ingest, health

app = FastAPI(title="RBC App Health Service")

@app.on_event("startup")
def startup():
    init_index()

app.include_router(ingest.router)
app.include_router(health.router)
