from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI(title="APAN FastAPI Example", version="0.1")


class Numbers(BaseModel):
    values: List[float]


@app.get("/")
def read_root():
    return {
        "message": "Welcome to APAN FastAPI example",
        "endpoints": ["/health", "/predict"]
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict_numbers(payload: Numbers):
    """Simple example endpoint that returns count, sum and mean of provided numbers.

    Request JSON example:
    { "values": [1.0, 2.5, 3.0] }
    """
    arr = np.array(payload.values, dtype=float)
    count = int(arr.size)
    total = float(arr.sum()) if count > 0 else 0.0
    mean = float(arr.mean()) if count > 0 else None
    return {"count": count, "sum": total, "mean": mean}
