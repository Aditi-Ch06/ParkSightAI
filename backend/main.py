from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI(
    title="ParkSight AI"
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
    smart_enforcement_planner
)

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