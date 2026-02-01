
from fastapi import APIRouter
from app.models.service import ServiceStatus
from app.services.health_service import save_status

router = APIRouter()

@router.post("/add")
def add_status(payload: ServiceStatus):
    save_status(payload.dict())
    return {"message": "Status added"}
