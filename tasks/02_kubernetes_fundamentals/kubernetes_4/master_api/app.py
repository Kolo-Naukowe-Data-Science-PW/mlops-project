from flask import Flask, request, jsonify
import requests
import numpy as np
import json
import ast

app = Flask(__name__)

SLAVE_APIS_URLS = [
    "http://10.96.1.1:5000/predict",
    "http://10.96.1.2:5000/predict",
    "http://10.96.1.3:5000/predict",
]


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    raw_data = request.get_data(as_text=True)
    data = ast.literal_eval(raw_data)
    headers = {"Content-type": "application/json"}
    slave_apis_results = [
        requests.post(url=url, data=json.dumps(data), headers=headers).json()
        for url in SLAVE_APIS_URLS
    ]
    results_arrays = [item["Result"][0] for item in slave_apis_results]
    aggregated_probas = np.sum(results_arrays, axis=0)
    prediction = np.argmax(aggregated_probas) + 1
    return jsonify({"prediction": [prediction.item()]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
