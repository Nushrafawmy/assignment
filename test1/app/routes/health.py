
from fastapi import APIRouter, HTTPException
from app.services.health_service import get_all_status, get_service_status

router = APIRouter()

@router.get("/healthcheck")
def healthcheck():
    data = get_all_status()
    if not data:
        raise HTTPException(status_code=404, detail="No data found")
    return data

@router.get("/healthcheck/{service_name}")
def service_health(service_name: str):
    data = get_service_status(service_name)
    if not data:
        raise HTTPException(status_code=404, detail="Service not found")
    return data
