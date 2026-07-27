from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# ── REQUEST SCHEMAS ──────────────────────────────────────────

class DetectionRequest(BaseModel):
    """Data yang dikirim warga saat upload foto"""
    latitude: float
    longitude: float
    kelurahan: str
    kecamatan: str
    kota: str = "Jakarta"
    reporter_note: Optional[str] = None


# ── RESPONSE SCHEMAS ─────────────────────────────────────────

class BlockageResult(BaseModel):
    """Hasil deteksi YOLOv8 untuk satu titik drainase"""
    detection_id: str
    latitude: float
    longitude: float
    kelurahan: str
    blockage_percentage: float        # 0.0 - 100.0
    severity_class: str               # clear / partial / blocked / severely_blocked
    waste_type: Optional[str]         # organic / plastic / debris / mixed
    confidence_score: float           # 0.0 - 1.0
    timestamp: datetime
    image_url: Optional[str] = None


class FloodRiskScore(BaseModel):
    """Skor risiko banjir per kelurahan"""
    kelurahan: str
    kecamatan: str
    risk_score: float                 # 0.0 - 100.0
    risk_level: str                   # low / moderate / high / critical
    total_blockage_points: int        # jumlah titik tersumbat
    avg_blockage_percentage: float    # rata-rata % sumbatan
    rainfall_forecast_mm: float       # prakiraan hujan 48 jam (BMKG)
    last_updated: datetime


class AlertNotification(BaseModel):
    """Peringatan otomatis untuk petugas DLH"""
    alert_id: str
    kelurahan: str
    risk_score: float
    risk_level: str
    message: str
    triggered_at: datetime
    is_acknowledged: bool = False


class MaintenanceTask(BaseModel):
    """Tugas maintenance untuk antrian petugas lapangan"""
    task_id: str
    priority: int                     # 1 = tertinggi
    kelurahan: str
    location_detail: str
    latitude: float
    longitude: float
    blockage_percentage: float
    assigned_team: Optional[str] = None
    status: str = "pending"           # pending / in_progress / completed
    created_at: datetime


class DashboardSummary(BaseModel):
    """Ringkasan data untuk halaman utama dashboard DLH"""
    total_active_blockages: int
    total_high_risk_areas: int
    total_completed_today: int
    total_citizen_reports: int
    risk_scores: List[FloodRiskScore]
    active_alerts: List[AlertNotification]
    maintenance_queue: List[MaintenanceTask]
    last_updated: datetime


# ── UPLOAD RESPONSE ──────────────────────────────────────────

class UploadResponse(BaseModel):
    """Response setelah warga upload foto"""
    success: bool
    message: str
    detection_id: Optional[str] = None
    blockage_percentage: Optional[float] = None
    severity_class: Optional[str] = None
    risk_level: Optional[str] = None
