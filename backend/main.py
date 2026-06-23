from fastapi import FastAPI
import pandas as pd
import joblib

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ParkSight AI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load artifacts
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# Prediction Function
# -------------------------

from backend.model_utils import (
    predict_hotspot,
    forecast_hotspots,
    smart_enforcement_planner,
    get_station_list
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/risk-score")
def risk_score(
    junction_name:str,
    police_station:str,
    hour:int,
    weekday:str,
    month:str
):
    
    pred = predict_hotspot(
        junction_name,
        police_station,
        hour,
        weekday,
        month
    )
    
    return {
        "predicted_violations":pred
    }
    
@app.get("/forecast")
def forecast(
    hour:int,
    weekday:str,
    month:str
):
    
    result = forecast_hotspots(
        hour,
        weekday,
        month
    )
    
    return result.to_dict(
        orient="records"
    )
    
@app.get("/deployment")
def deployment(
    police_station:str,
    weekday:str,
    month:str
):
    
    result = smart_enforcement_planner(
        police_station,
        weekday,
        month
    )
    
    return result.to_dict(
        orient="records"
    )
    
@app.get("/")
def home():
    return {
        "message": "ParkSight AI API is live",
        "docs": "/docs"
    }
    
@app.get("/stations")
def stations():
    return get_station_list()

