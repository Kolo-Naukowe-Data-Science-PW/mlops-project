from pathlib import Path
import sys

sys.path.append(str(Path(".").resolve()))

import numpy as np
from xgboost import XGBClassifier
from flask import Flask, jsonify, request
from containerized_ml_models.api import io

MODEL_PATH: str = "containerized_ml_models/api/model.pkl"
model: XGBClassifier = io.load_model(MODEL_PATH)

app: Flask = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    content: list[list[float]] = request.json
    input_data: np.ndarray = np.array(content)
    prediction = model.predict(input_data).tolist()
    return jsonify({"prediction": prediction})
