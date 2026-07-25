from fastapi import FastAPI, Request
from pydantic import BaseModel
import pandas as pd
import time
from prometheus_exporter import generate_metrics

from prometheus_client import start_http_server

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    start_http_server(8001)
    print("Prometheus metrics server started on port 8001")

class Features(BaseModel):
    gender: int
    age: float
    hypertension: int
    heart_disease: int
    smoking_history: int
    bmi: float
    HbA1c_level: float
    blood_glucose_level: int

# Note: In a real scenario, you would load the MLflow model here:
# import mlflow
# model = mlflow.pyfunc.load_model("models:/DiabetesModel/Production")

@app.post("/predict")
async def predict(features: Features):
    start_time = time.time()
    
    # Mock prediction
    prediction = 0 
    
    latency = time.time() - start_time
    
    # Generate custom metrics for Prometheus
    generate_metrics(latency=latency, prediction=prediction)
    
    return {"prediction": prediction, "latency": latency}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
