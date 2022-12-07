import os
import json
import pandas as pd
import pickle as pkl
from flask import Flask, jsonify, request

with open(os.environ["MODEL_PATH"], "rb") as f:
    model = pkl.load(f)

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    content = request.json
    content = {"0": content}
    input_data = pd.read_json(json.dumps(content), orient="index")
    out = model.predict_proba(input_data).tolist()
    return jsonify({"Result": out})
