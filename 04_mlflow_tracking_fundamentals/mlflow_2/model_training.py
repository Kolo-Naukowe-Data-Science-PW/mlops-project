import pandas as pd
import os
import mlflow
import seaborn as sns
import xgboost as xgb
import numpy as np
import warnings

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    f1_score,
    roc_auc_score,
    recall_score,
    precision_score,
)
from sklearn.preprocessing import OneHotEncoder
from BasicTree import BasicTree
from mlflow import MlflowClient

warnings.filterwarnings("ignore")

RANDOM = 102
TEST_SIZE = 0.3


def log_grid_search(gscv: GridSearchCV, X, y):
    mlflow.sklearn.autolog()

    with mlflow.start_run(run_name="Grid search run") as run:
        run_id = run.info.run_id
        gscv.fit(X, y)

    mlflow.sklearn.autolog(disable=True)
    return run_id


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

    pipeline = Pipeline(
        [
            (
                "column_transformer",
                ColumnTransformer(
                    [("onehotencoder", encoder, cat_cols)], remainder="passthrough"
                ),
            ),
            ("clf", BasicTree()),
        ]
    )

    parameters = [
        {
            "clf__model": [RandomForestClassifier()],
            "clf__model__n_estimators": [1000],
            "clf__model__criterion": ["gini", "entropy"],
        },
        {
            "clf__model": [DecisionTreeClassifier()],
            "clf__model__criterion": ["gini", "entropy"],
            "clf__model__min_samples_split": list(range(2, 6)),
        },
        {
            "clf__model": [XGBClassifier()],
            "clf__model__booster": ["gbtree", "gblinear", "dart"],
            "clf__model__learning_rate": [0.05, 0.1, 0.025],
            "clf__model__gamma": [0, 0.01, 0.1],
        },
    ]

    gscv = GridSearchCV(pipeline, parameters, n_jobs=-1, cv=5, scoring="f1")
    gscv.fit(X_train, y_train)
    run_id = log_grid_search(gscv, X_test, y_test)

    clf = gscv.best_estimator_
    best_params = gscv.best_params_
    best_params.pop("clf__model")
    preds = clf.predict(X_valid)

    with mlflow.start_run(run_name="Best model") as run:

        mlflow.log_params(best_params)

        mlflow.log_metric("f1_score", f1_score(y_valid, preds))
        mlflow.log_metric("accuracy_score", accuracy_score(y_valid, preds))
        mlflow.log_metric("recall_score", recall_score(y_valid, preds))
        mlflow.log_metric("precision_score", precision_score(y_valid, preds))
        mlflow.log_metric("average_precision_score", roc_auc_score(y_valid, preds))

        mlflow.sklearn.log_model(clf, type(clf["clf"]).__name__)

        plot = sns.heatmap(
            np.round(confusion_matrix(y_valid, preds), 5),
            annot=True,
            cbar=False,
        )

        path = "./data/conf_matrix.png"
        plot.figure.savefig(path)
        mlflow.log_artifact(path)
