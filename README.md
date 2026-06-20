# 🚦 ParkSight AI

### Predict. Prioritize. Prevent.

ParkSight AI is an AI-powered predictive parking enforcement platform developed for **Flipkart Gridlock 2.0 (Prototype Development Round)**.

The platform transforms historical parking violation records into actionable intelligence for traffic authorities by forecasting parking hotspots, estimating violation risk, and recommending optimized enforcement deployment strategies.

---

## 🌟 Problem Statement

Illegal and unregulated parking contributes significantly to urban traffic congestion. Current enforcement approaches are often reactive, leading to inefficient utilization of traffic personnel and delayed interventions.

Traffic authorities need a proactive system that can:

* Predict high-risk parking violation zones
* Forecast future congestion hotspots
* Optimize enforcement resource deployment
* Support data-driven decision making

---

## 💡 Solution

ParkSight AI leverages machine learning and spatio-temporal analytics to help traffic authorities move from reactive enforcement to predictive enforcement.

Using historical parking violation data, the platform:

* Predicts parking violation risk at specific locations and times
* Forecasts upcoming parking hotspots across the city
* Recommends priority junctions and optimal enforcement hours
* Provides actionable insights through an interactive dashboard

---

## 🚀 Key Features

### 🎯 Risk Score Prediction

Estimate expected parking violations based on:

* Junction
* Police Station
* Hour
* Day of Week
* Month

Provides proactive risk assessment before congestion occurs.

---

### 📈 Hotspot Forecasting

Identifies and ranks future parking violation hotspots across the city.

Benefits:

* Early intervention
* Better traffic management
* Reduced congestion

---

### 🚓 Smart Enforcement Planner

Generates station-specific deployment recommendations.

Outputs:

* Priority junctions
* Optimal enforcement hours
* Risk scores
* Resource allocation suggestions

---

### 📊 Interactive Dashboard

Modern web dashboard for exploring:

* Risk predictions
* Hotspot rankings
* Enforcement plans
* Historical insights

---

## 🏗️ System Architecture

Dataset → Data Audit & EDA → Feature Engineering → CatBoost Model → FastAPI Backend → React Frontend → Deployment

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* CatBoost
* Joblib

### Backend

* FastAPI
* Uvicorn

### Frontend

* React.js

### Deployment

* Render (Backend)
* Vercel (Frontend)

### Development Tools

* Google Colab
* Git
* GitHub

---

## 📂 Project Structure

```text
ParkSightAI/
│
├── backend/
│   ├── main.py
│   ├── model_utils.py
│   └── ...
│
├── frontend/
│   ├── src/
│   └── ...
│
├── models/
│   └── parking_hotspot_model.pkl
│
├── data/
│   └── model_data.csv
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone [<repository-url>](https://github.com/Aditi-Ch06/ParkSightAI)
cd ParkSightAI
```

### 2. Backend Setup

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn backend.main:app --reload
```

Backend available at:

```text
http://localhost:8000
```

API documentation:

```text
http://localhost:8000/docs
```

---

### 3. Frontend Setup

Navigate to frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend available at:

```text
http://localhost:5173
```

---

## 🌐 Live Demo

Frontend:

[https://park-sight-ai.vercel.app/](https://park-sight-ai.vercel.app/)

Backend API:

[https://parksightai.onrender.com/](https://parksightai.onrender.com/docs)

---

## 📸 Screenshots

### Home Dashboard

<img width="946" height="438" alt="Screenshot 2026-06-20 192856" src="https://github.com/user-attachments/assets/52a9a3b6-2b30-49f6-8d12-168d3418f499" />

### Smart Enforcement Planner

<img width="947" height="440" alt="Screenshot 2026-06-20 191715" src="https://github.com/user-attachments/assets/60ca81be-42b0-4d28-8c57-52fb6b46c269" />

### Hotspot Forecasting

<img width="946" height="437" alt="Screenshot 2026-06-20 191623" src="https://github.com/user-attachments/assets/1ba990c5-5aec-4b84-b668-5758f23c4e7f" />

### Risk Analysis Dashboard

<img width="944" height="438" alt="Screenshot 2026-06-20 191440" src="https://github.com/user-attachments/assets/bd3cf1e6-8ca4-496a-9310-cb28d93f7bde" />

---

## 🔮 Future Scope

* Live traffic integration
* CCTV-based violation detection
* IoT parking sensors
* Real-time city heatmaps
* Officer mobile application
* Command center integration
* Dynamic deployment optimization
* Continuous model retraining

---

## 👥 Team TransitIQ

### Machine Learning & Backend

**Aditi Chaudhary**

* Data Audit & EDA
* Feature Engineering
* CatBoost Model Development
* FastAPI Backend
* Model Deployment

### Frontend & Product Development

**Sarthak Agrawal**

* React.js Dashboard
* UI/UX Development
* Frontend Deployment
* Demo Video Production

---

## 🏆 Hackathon

**Flipkart Gridlock 2.0**
Prototype Development Round

---

## 📜 License

This project was developed for educational and hackathon purposes.
