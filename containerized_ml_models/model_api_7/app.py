# !/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"ping": "success"})


@app.route('/predict', methods=['POST'])
def predict():
    data = json.loads(request.get_data())
    model = pickle.load(open('model.pkl', 'rb'))
    prediction = model.predict(data).tolist()
    return jsonify({'Result': prediction})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
