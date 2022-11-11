import pickle
from flask import Flask, request, jsonify
import json


MODEL_PATH = "model.pkl"
app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "Success"})


@app.route("/predict", methods=["POST"])
def predict():
    data = json.loads(request.args.get(""))
    y_pred = model.predict(data)
    return jsonify({"Result": y_pred.tolist()})


if __name__ == "__main__":

    model = pickle.load(open(MODEL_PATH, "rb"))
    app.run(host="0.0.0.0", port=8000)
