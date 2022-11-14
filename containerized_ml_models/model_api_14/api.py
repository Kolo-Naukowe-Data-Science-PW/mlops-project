from typing import Any
from flask import Flask, request, jsonify
from numpy import ndarray, asarray
import pickle
import ast

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict() -> ndarray[(Any, 1), float]:
    raw_data = request.get_data(as_text=True)
    data = asarray(ast.literal_eval(raw_data))
    return jsonify({"prediction": f"{model.predict(data)}"})


if __name__ == "__main__":
    app.run()