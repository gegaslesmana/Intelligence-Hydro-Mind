from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def dashboard_root():
    return {"module": "dashboard", "status": "ready"} 
