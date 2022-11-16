from flask import Flask, jsonify, request
import pickle
import numpy as np
import json

app = Flask(__name__)


@app.route("/ping")
def ping_success():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    record = request.get_data(as_text=True)
    data = np.array(json.loads(record))
    with open("model.pkl", "rb") as model_bin:
        model = pickle.load(model_bin)
        prediction = model.predict(data)
    return jsonify({"Result": f"{prediction}"})


if __name__ == "__main__":
    app.run()
