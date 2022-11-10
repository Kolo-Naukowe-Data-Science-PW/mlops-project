from typing import Any
import pickle as pkl


def load_model(path: str) -> Any:
    with open(path, "rb") as f:
        model = pkl.load(f)
    return model
