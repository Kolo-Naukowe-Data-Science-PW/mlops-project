from flask import Flask, jsonify, request
from constants import MODEL_PATH
import pickle as pkl
import json

app = Flask(__name__)

with open(MODEL_PATH, "rb") as f:
    model = pkl.load(f)


@app.route("/ping", methods=["GET"])
def get():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    content = request.values
    input_data = json.loads(list(content)[0])
    prediction = model.predict(input_data).tolist()
    return jsonify({"Result": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
