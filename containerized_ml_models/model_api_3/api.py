import json

from flask import Flask, jsonify, request
import pickle
import numpy as np


app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    request_data = json.loads(request.data)
    prediction_data = np.array(request_data)

    model = pickle.load(open("model.pkl", "rb"))
    result = model.predict(prediction_data)

    return jsonify({"Result": result.tolist()})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
