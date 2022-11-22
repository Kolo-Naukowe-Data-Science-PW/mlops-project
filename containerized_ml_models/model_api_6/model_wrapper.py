from singleton_decorator import singleton
from constants import MODEL_PATH
import pickle as pkl
import numpy as np


@singleton
class ModelWrapper:
    def __init__(self, model_path: str = MODEL_PATH) -> None:
        with open(MODEL_PATH, "rb") as f:
            self._model = pkl.load(f)

    def predict(self, data: np.ndarray) -> np.ndarray:
        return self._model.predict(data)
