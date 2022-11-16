from typing import Any
from flask import Flask, request, jsonify
import numpy as np
import pickle
import ast

app = Flask(__name__)
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict() -> np.ndarray[(Any, 1), float]:
    raw_data = request.get_data(as_text=True)
    data = np.asarray(ast.literal_eval(raw_data))
    return jsonify({"prediction": f"{model.predict(data)}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
