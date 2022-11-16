import json
import pickle
from flask import Flask, request

app = Flask(__name__)

with open("model.pkl", "rb") as file:
    pickle_in = pickle.load(file)


@app.route("/ping", methods=["GET"])
def ping():
    return json.dumps({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    record = json.loads(request.get_data())
    pr = pickle_in.predict(record).tolist()
    return json.dumps({"Result": pr})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
