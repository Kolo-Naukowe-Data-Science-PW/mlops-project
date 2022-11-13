from flask import Flask, jsonify, request
from pickle import load as pkl_load
from ast import literal_eval
from numpy import asarray

app = Flask(__name__)
MODEL_NAME = "model.pkl"


def load_pickle(fileName):
    return pkl_load(open(MODEL_NAME, "rb"))


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    model = load_pickle()
    data = request.get_data(as_text=True)

    input = literal_eval(input)
    input = asarray(input)  
    output = model.predict(input)

    return jsonify({"Result": f"{output}"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
