from __future__ import annotations
import pickle as pkl
import numpy as np


class Model:

    __create_key = object()
    class_instance = None

    def __init__(self, model_path: str, create_key: object) -> None:
        if create_key is not self.__create_key:
            raise ValueError(
                "You shouldn't call __init__ method. "
                "Call Model.get_or_create instead"
            )
        with open(model_path, "rb") as file:
            self.model = pkl.load(file)

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.predict(X)

    @classmethod
    def get_or_create(cls, model_path: str) -> Model:
        if cls.class_instance:
            return cls.class_instance
        cls.class_instance = cls(model_path, cls.__create_key)
        return cls.class_instance
