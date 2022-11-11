import numpy as np
from flask import Flask, jsonify, request
from containerized_ml_models.api.model import Model

MODEL_PATH = "containerized_ml_models/api/model.pkl"
app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    content = request.json
    input_data = np.array(content)
    model = Model.get_or_create(MODEL_PATH)
    prediction = model.predict(input_data).tolist()
    return jsonify({"prediction": prediction})
