from flask import Flask
from flask import request
import pickle
import json

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return json.dumps({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    arr = json.loads(request.get_data())
    return read_model(arr)


def read_model(data):
    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    return model.predict(data).tolist()


app.run(port=8000, host="0.0.0.0")
