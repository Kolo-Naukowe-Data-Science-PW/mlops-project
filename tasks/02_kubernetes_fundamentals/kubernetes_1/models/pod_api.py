import json
from flask import Flask, request, jsonify
import numpy as np
import pickle
import sys

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    data = json.loads(request.get_data())
    x = np.array(data).reshape(1, -1)

    with open(sys.argv[1] + "/" + sys.argv[1] + ".pkl", "rb") as model_handle:
        model = pickle.load(model_handle)
        try:
            prediction = model.predict(x).tolist()
        except Exception:
            prediction = "Invalid data"

    return jsonify({"Prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
