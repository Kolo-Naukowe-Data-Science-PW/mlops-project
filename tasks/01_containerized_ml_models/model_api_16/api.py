import pickle
from flask import Flask, request, jsonify
import json
import os


MODEL_PATH = "model.pkl"
app = Flask(__name__)


def get_model_date():
    return os.path.getatime(MODEL_PATH)


def load_model():
    return pickle.load(open(MODEL_PATH, "rb"))


def check_model():
    global model

    age = get_model_date()
    if age != last_age:
        age = last_age
        model = load_model()


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "Success", "model": "16"})


@app.route("/predict", methods=["POST"])
def predict():
    data = json.loads(request.args.get(""))

    check_model()
    y_pred = model.predict(data)

    return jsonify({"Result": y_pred.tolist()})


if __name__ == "__main__":
    model = load_model()
    last_age = get_model_date()

    app.run(host="0.0.0.0", port=8000)
