from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_detection, routes_risk, routes_dashboard

app = FastAPI(
    title="DRAIN-EYE API",
    description="AI-powered drainage blockage detection & flood risk scoring system for DKI Jakarta",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "https://drain-eye-tbnt.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_detection.router, prefix="/api/detection", tags=["Detection"])
app.include_router(routes_risk.router,      prefix="/api/risk",      tags=["Risk Score"])
app.include_router(routes_dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])

@app.get("/")
def root():
    return {
        "status": "online",
        "project": "DRAIN-EYE",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}