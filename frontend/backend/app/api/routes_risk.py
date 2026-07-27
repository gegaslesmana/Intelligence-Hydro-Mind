from fastapi import APIRouter
from datetime import datetime
from app.services.lstm_service import predict_flood_risk, predict_all_kelurahan

router = APIRouter()

@router.get("/")
def risk_root():
    return {"module": "risk", "status": "ready"}

@router.get("/score/{kelurahan}")
def get_risk_score(
    kelurahan: str,
    blockage_score: float = 50.0,
    rainfall_mm: float = 10.0
):
    result = predict_flood_risk(
        kelurahan=kelurahan,
        blockage_score=blockage_score,
        rainfall_mm=rainfall_mm
    )
    result["last_updated"] = datetime.now().isoformat()
    return result

@router.get("/all")
def get_all_risk_scores():
    results = predict_all_kelurahan({})
    return {
        "total": len(results),
        "data": results,
        "last_updated": datetime.now().isoformat()
    }