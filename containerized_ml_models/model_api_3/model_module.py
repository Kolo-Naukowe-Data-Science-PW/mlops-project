"""
Using the fact that module is imported only once,
we get pseudo-singleton behavior by importing model_module
"""
import pickle


with open("model.pkl", "rb") as file:
    model = pickle.load(file)
