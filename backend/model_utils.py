import pandas as pd
import joblib

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(
    BASE_DIR / "models" / "parking_hotspot_model.pkl"
)

model_df = pd.read_csv(
    BASE_DIR / "data" / "model_data.csv"
)
def predict_hotspot(
    junction,
    police_station,
    hour,
    weekday,
    month
):
    sample = pd.DataFrame({
        'junction_name':[junction],
        'police_station':[police_station],
        'hour':[hour],
        'weekday':[weekday],
        'month':[month]
    })

    prediction = model.predict(sample)[0]

    return float(prediction)

def forecast_hotspots(
    hour,
    weekday,
    month,
    top_n=10
):
    
    predictions = []
    
    junction_station_map = (
        model_df[
            ['junction_name','police_station']
        ]
        .drop_duplicates()
    )
    
    for _, row in junction_station_map.iterrows():
        
        junction = row['junction_name']
        station = row['police_station']
        
        pred = predict_hotspot(
            junction=junction,
            police_station=station,
            hour=hour,
            weekday=weekday,
            month=month
        )
        
        predictions.append([
            junction,
            station,
            pred
        ])
    
    forecast_df = pd.DataFrame(
        predictions,
        columns=[
            'junction_name',
            'police_station',
            'predicted_violations'
        ]
    )

    forecast_df['risk_score'] = (
        forecast_df['predicted_violations']
        /
        forecast_df['predicted_violations'].max()
    ) * 100
    
    return (
        forecast_df
        .sort_values(
            'predicted_violations',
            ascending=False
        )
        .head(top_n)
    )
    
def smart_enforcement_planner(
    police_station,
    weekday,
    month,
    top_n=5
):
    
    station_junctions = (
        model_df[
            model_df['police_station']
            .str.strip()
            .str.lower()
            ==
            police_station.strip().lower()
        ]
        [['junction_name']]
        .drop_duplicates()
    )
    
    recommendations = []
    
    for junction in station_junctions['junction_name']:
        
        best_hour = None
        best_prediction = -1
        
        for hour in range(24):
            
            pred = predict_hotspot(
                junction,
                police_station,
                hour,
                weekday,
                month
            )
            
            if pred > best_prediction:
                
                best_prediction = pred
                best_hour = hour
        
        recommendations.append([
            junction,
            best_hour,
            best_prediction
        ])
    
    rec_df = pd.DataFrame(
        recommendations,
        columns=[
            'junction_name',
            'recommended_hour',
            'predicted_violations'
        ]
    )

    rec_df['risk_score'] = (
        rec_df['predicted_violations']
        /
        rec_df['predicted_violations'].max()
    ) * 100
    
    rec_df['priority'] = pd.cut(
        rec_df['risk_score'],
        bins=[0,40,70,100],
        labels=[
            'Low',
            'Medium',
            'High'
        ],
        include_lowest=True
    )
    
    return (
        rec_df
        .sort_values(
            'predicted_violations',
            ascending=False
        )
        .head(top_n)
    )