import json
from flask import Flask, request, jsonify
import pickle
import sys
from pathlib import Path
import os

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    data = json.loads(request.get_data())
    path = Path(__file__).parent.absolute()
    path = os.path.join(path, sys.argv[1] + ".pkl")
    prediction = path

    try:
        with open(path, "rb") as model_handle:
            model = pickle.load(model_handle)
            try:
                prediction = model.predict(data).tolist()
            except Exception as e:
                prediction = repr(e)
    except Exception:
        prediction = "Cannot open file"

    return jsonify({"Prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
