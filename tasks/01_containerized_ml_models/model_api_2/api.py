from flask import Flask, jsonify, request
import pickle
from ast import literal_eval
import numpy as np

app = Flask(__name__)
MODEL_NAME = "model.pkl"
PORT = 5000
HOSTNAME = "0.0.0.0"


def load_pickle() -> object:
    with open(MODEL_NAME, "rb") as file:
        obj = pickle.load(file)
    return obj


@app.route("/ping", methods=["GET"])
def ping() -> any:
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict() -> any:
    model = load_pickle()

    data = request.get_data(as_text=True)
    data = literal_eval(data)
    data = np.asarray(data)

    output = model.predict(data)
    return jsonify({"Result": f"{output}"})


if __name__ == "__main__":
    app.run(host=HOSTNAME, port=PORT)
