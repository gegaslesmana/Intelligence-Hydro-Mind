from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def risk_root():
    return {"module": "risk", "status": "ready"}