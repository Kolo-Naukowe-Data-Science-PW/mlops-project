import pickle
import json
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    model = pickle.load(open("model.pkl", "rb"))
    requested_data = np.array(json.loads(request.get_data()))
    prediction = model.predict(requested_data).tolist()
    return jsonify({"Result": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
