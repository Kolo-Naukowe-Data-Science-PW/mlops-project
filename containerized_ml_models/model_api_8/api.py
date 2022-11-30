from fastapi import FastAPI, Request
from pickle import load
import numpy as np
from uvicorn import run

app = FastAPI()

file = open("model.pkl", "rb")
model = load(file)
file.close()


@app.get("/ping")
def ping():
    return {"ping": "success", "model": "8"}


@app.post("/predict")
def predict():
    request_data = Request.get_json()
    data = np.array([request_data["data"]])
    prediction = model.predict(data)
    return {"Result": prediction.tolist()}


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
