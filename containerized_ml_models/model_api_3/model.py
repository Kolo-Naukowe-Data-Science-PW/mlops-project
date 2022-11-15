"""
Using the fact that module is imported only one
"""
import pickle


with open("model.pkl", "rb") as file:
    model = pickle.load(file)
