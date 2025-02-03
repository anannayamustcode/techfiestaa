from fastapi import FastAPI
from pydantic import BaseModel
from model.ml_model import predict_score

import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {'health check': 'ok'}

@app.get("/{name}")
def hello(name: str):
    return {'message': f'hello there, {name}'}

class req_body(BaseModel):
    lon:float
    lat:float

@app.post('/predict')
def predict(data : req_body):
    lon=data.lon
    lat=data.lat

    score = predict_score(lon,lat)
    return {'safety score': score}