from fastapi import FastAPI
from pydantic import BaseModel
from model.ml_model import predict_score
from model.ml_model import version as mversion

app = FastAPI()

@app.get("/")
def home():
    return {'health check': 'ok', 'model version':mversion}
