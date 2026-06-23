from functools import lru_cache
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

model_df["station_clean"] = (
    model_df["police_station"]
    .str.strip()
    .str.lower()
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

@lru_cache(maxsize=100)
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
    
    forecast_df = junction_station_map.copy()

    forecast_df["hour"] = hour
    forecast_df["weekday"] = weekday
    forecast_df["month"] = month

    forecast_df["predicted_violations"] = model.predict(
        forecast_df[
            [
                "junction_name",
                "police_station",
                "hour",
                "weekday",
                "month"
            ]
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
    
@lru_cache(maxsize=100)
def smart_enforcement_planner(
    police_station,
    weekday,
    month,
    top_n=5
):
    
    station_junctions = (
        model_df[
            model_df['station_clean']
            ==
            police_station.strip().lower()
        ]
        [['junction_name']]
        .drop_duplicates()
    )
    
    actual_station = (
        model_df[
            model_df["station_clean"]
            == police_station.strip().lower()
        ]["police_station"]
        .iloc[0]
    )
    
    recommendations = []
    
    samples = []

    for junction in station_junctions["junction_name"]:
        for hour in range(24):
            samples.append([
                junction,
                actual_station,
                hour,
                weekday,
                month
            ])

    sample_df = pd.DataFrame(
        samples,
        columns=[
            "junction_name",
            "police_station",
            "hour",
            "weekday",
            "month"
        ]
    )

    sample_df["prediction"] = model.predict(sample_df)
    
    best_rows = (
        sample_df
        .sort_values("prediction", ascending=False)
        .groupby("junction_name")
        .first()
        .reset_index()
    )
    
    rec_df = best_rows.rename(
        columns={
            "hour": "recommended_hour",
            "prediction": "predicted_violations"
        }
    )

    rec_df = rec_df[
        [
            "junction_name",
            "recommended_hour",
            "predicted_violations"
        ]
    ]

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
    
def get_station_list():

    return sorted(
        model_df["police_station"]
        .dropna()
        .unique()
        .tolist()
    )
    
