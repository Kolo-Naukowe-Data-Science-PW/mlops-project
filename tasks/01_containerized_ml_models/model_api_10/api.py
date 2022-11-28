import json
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

with open("model/model.pkl", "rb") as file:
    pickle_in = pickle.load(file)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    record = json.loads(request.get_data())
    pr = pickle_in.predict(record).tolist()
    return jsonify({"Result": pr})


if __name__ == "__main__":
    app.run()
