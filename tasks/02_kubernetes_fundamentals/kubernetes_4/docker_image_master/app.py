from flask import Flask, request, jsonify
import numpy as np
import ast

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    raw_data = request.get_data(as_text=True)
    data = ast.literal_eval(raw_data)
    probabilities = np.array(data['probabilities'])
    return jsonify({"prediction": f"{np.argmax(probabilities) + 1}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
