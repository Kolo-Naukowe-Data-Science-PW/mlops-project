import pandas as pd
import os
import mlflow
import seaborn as sns
import warnings

from hyperopt import hp, Trials, STATUS_OK, fmin, tpe
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.compose import ColumnTransformer
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import OneHotEncoder

warnings.filterwarnings("ignore")

RANDOM = 101
TEST_SIZE = 0.3
KEY_TO_MODEL = "type"
FOLDS = 2


def objective(space: dict) -> dict:
    mlflow.sklearn.autolog()
    model_class = space[KEY_TO_MODEL]
    space.pop(KEY_TO_MODEL)

    with mlflow.start_run(nested=True):
        model = model_class(**space)

        scores = cross_val_score(
            model, X_train, y_train, scoring="f1", cv=FOLDS, n_jobs=-1
        )

        best_score = max(scores)

        loss = 1 - best_score

    mlflow.sklearn.disable_autologging()
    return {"loss": loss, "status": STATUS_OK}


if __name__ == "__main__":
    df = pd.read_csv(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "data", "to_train.csv"
        )
    )

    X = df.drop("is_female", axis=1)
    y = df.is_female

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM
    )
    X_test, X_valid, y_test, y_valid = train_test_split(
        X_test, y_test, test_size=TEST_SIZE, random_state=RANDOM
    )

    encoder = OneHotEncoder(handle_unknown="ignore")
    cat_cols = X_train.select_dtypes(include="object").columns

    col_transformer = ColumnTransformer(
        [("onehotencoder", encoder, cat_cols)], remainder="passthrough"
    )

    X_train = col_transformer.fit_transform(X_train)
    X_test = col_transformer.transform(X_test)

    space = {}

    space["RandomForestClassifier"] = {
        "n_estimators": hp.choice("n_estimators", list(range(500, 4001, 500))),
        "n_jobs": -1,
        "criterion": hp.choice("criterion", ["gini", "entropy"]),
    }
    space["DecisionTreeClassifier"] = {
        "criterion": hp.choice("criterion", ["gini", "entropy"]),
        "min_samples_split": hp.choice("min_samples_split", list(range(2, 6))),
    }
    space["XGBClassifier"] = {
        "booster": hp.choice("booster", ["gbtree", "gblinear", "dart"]),
        "learning_rate": hp.uniform("learning_rate", 0.01, 0.025),
        "gamma": hp.uniform("gamma", 0.01, 0.1),
        "n_jobs": -1,
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
                max_evals=10,
                verbose=True,
            )
            print(f"{'*'*25}\nDONE {model}\n{'*'*25}")
            best_params = {k: float(v) for (k, v) in best_params.items()}
            mlflow.log_dict(best_params, "best_model.json")
        mlflow.end_run()
