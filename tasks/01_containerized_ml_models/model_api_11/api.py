from flask import Flask, jsonify, request
import pickle
import ast

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "POST":
        data = request.get_data().decode("ascii")
        data = ast.literal_eval(data)
        model = pickle.load(open("model.pkl", "rb"))
        try:
            prediction = model.predict(data).tolist()
        except Exception:
            prediction = None
    return jsonify({"Result": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
