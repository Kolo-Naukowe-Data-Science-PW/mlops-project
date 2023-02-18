import pandas as pd
import os
import mlflow
import seaborn as sns
import numpy as np
import warnings
import matplotlib.pyplot as plt

from hyperopt import hp, Trials, STATUS_OK, fmin, tpe
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.compose import ColumnTransformer
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator

warnings.filterwarnings("ignore")

RANDOM_STATE = 101
TEST_SIZE = 0.3
KEY_TO_MODEL = "model_stored_as_key_in_space"
N_FOLDS = 3
MAX_EVALS = 10


def objective(space: dict) -> dict:
    mlflow.sklearn.autolog()
    model_class = space[KEY_TO_MODEL]
    del space[KEY_TO_MODEL]

    with mlflow.start_run(nested=True):
        model = model_class(**space)

        scores = cross_val_score(
            model, X_train, y_train, scoring="f1", cv=N_FOLDS, n_jobs=-1
        )

        best_score = max(scores)

        loss = 1 - best_score

    mlflow.sklearn.disable_autologging()
    return {
        "loss": loss,
        "status": STATUS_OK,
        "model": model,
        "loss_variance": np.var([1 - i for i in scores]),
    }


def get_best_model_from_trials(trials: Trials) -> BaseEstimator:
    trials_with_OK_STATUS = [
        trial for trial in trials if STATUS_OK == trial["result"]["status"]
    ]
    score_of_valid_trials = [
        float(trial["result"]["loss"]) for trial in trials_with_OK_STATUS
    ]
    ind_of_lowest_loss = np.argmin(score_of_valid_trials)
    return trials_with_OK_STATUS[ind_of_lowest_loss]["result"]["model"]


def log_best_model(model: BaseEstimator) -> None:
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    dir = os.path.join("mlruns/models")
    plot = sns.heatmap(confusion_matrix(y_test, preds), annot=True)
    path_to_mtrx = os.path.join(dir, "conf-matrix.png")
    path_to_model = os.path.join(dir, "model")

    plt.savefig(plot, path_to_mtrx)
    mlflow.log_artifact(path_to_mtrx)
    mlflow.sklearn.save_model(model, path_to_model)


if __name__ == "__main__":
    df = pd.read_csv(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "data", "to_train.csv"
        )
    )

    X = df.drop("is_female", axis=1)
    y = df.is_female

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )

    encoder = OneHotEncoder(handle_unknown="ignore")
    cat_cols = X_train.select_dtypes(include="object").columns

    col_transformer = ColumnTransformer(
        [("onehotencoder", encoder, cat_cols)], remainder="passthrough"
    )

    X_train = col_transformer.fit_transform(X_train)
    X_test = col_transformer.transform(X_test)

    models = [
        RandomForestClassifier,
        DecisionTreeClassifier,
        XGBClassifier,
        KNeighborsClassifier,
    ]

    space = {}

    space["RandomForestClassifier"] = {
        "n_estimators": hp.choice("n_estimators", list(range(500, 4001, 500))),
        "n_jobs": -1,
        "criterion": hp.choice("criterion", ["gini", "entropy", "log_loss"]),
    }
    space["DecisionTreeClassifier"] = {
        "criterion": hp.choice("criterion", ["gini", "entropy"]),
        "min_samples_split": hp.choice("min_samples_split", list(range(2, 6))),
    }
    space["XGBClassifier"] = {
        "learning_rate": hp.loguniform("learning_rate", 0.01, 0.5),
        "max_depth": hp.choice("max_depth", np.arange(2, 11).tolist()),
        "min_child_weight": hp.choice("min_child_weight", np.arange(0, 101).tolist()),
        "gamma": hp.loguniform("gamma", 0.0, 2.0),
        "subsample": hp.uniform("subsample", 0.5, 1.0),
        "colsample_bytree": hp.uniform("colsample_bytree", 0.5, 1.0),
        "colsample_bylevel": hp.uniform("colsample_bylevel", 0.5, 1.0),
        "reg_alpha": hp.loguniform("reg_alpha", 0.0, 2.0),
        "reg_lambda": hp.loguniform("reg_lambda", 0.0, 2.0),
        "n_jobs": -1,
    }
    space["KNeighborsClassifier"] = {
        "n_jobs": -1,
        "n_neighbors": hp.choice("n_neighbors", np.arange(1, 11).tolist()),
        "weights": hp.choice("weights", ["uniform", "distance"]),
    }

    mlflow.set_experiment("Hyperopt-optimazation")
    algo = tpe.suggest

    for i, model in enumerate(space.keys()):
        trials = Trials()

        with mlflow.start_run(run_name=model) as run:
            space[model][KEY_TO_MODEL] = globals()[model]
            best_params = fmin(
                objective,
                space[model],
                algo=algo,
                trials=trials,
                max_evals=MAX_EVALS,
                verbose=True,
            )

            print(f"{'*'*25}\nDONE - {model}\n{'*'*25}")

            best_params = {k: float(v) for (k, v) in best_params.items()}

            mlflow.log_dict(best_params, "best_model.json")
