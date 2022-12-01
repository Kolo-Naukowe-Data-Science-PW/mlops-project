from flask import Flask, jsonify, request
from model_wrapper import ModelWrapper
import json

app = Flask(__name__)

# singleton
ModelWrapper()


@app.route("/ping", methods=["GET"])
def get():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    model = ModelWrapper()

    content = request.values
    input_data = json.loads(list(content)[0])
    prediction = model.predict(input_data).tolist()
    return jsonify({"Result": prediction})
