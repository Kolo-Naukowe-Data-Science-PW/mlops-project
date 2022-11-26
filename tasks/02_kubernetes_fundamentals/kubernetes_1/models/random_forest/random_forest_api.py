# !/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    data = json.loads(request.get_data())
    x = np.array(data).reshape(1, -1)

    with open("random_forest_model.pkl", "rb") as model_handle:
        model = pickle.load(model_handle)
        try:
            prediction = model.predict(x).tolist()
        except Exception:
            prediction = "Invalid data"

    return jsonify({"Prediction": prediction})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)