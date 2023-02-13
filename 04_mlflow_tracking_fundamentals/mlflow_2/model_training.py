import pandas as pd
import os
import mlflow

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from BasicTree import BasicTree

RANDOM = 101
TEST_SIZE = 0.3

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
        X, y, test_size=TEST_SIZE, random_state=RANDOM
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
            "clf__model__n_estimators": list(range(500, 4001, 500)),
            "clf__model__criterion": ["gini", "entropy"],
        },
        {
            "clf__model": [DecisionTreeClassifier()],
            "clf__model__criterion": ["gini", "entropy"],
            "clf__model__min_samples_split": list(range(2, 6)),
        },
        {"clf__model": [XGBClassifier()]},
    ]

    gscv = GridSearchCV(pipeline, parameters, n_jobs=12, cv=3, verbose=2, scoring="f1)

    mlflow.sklearn.autolog()

    gscv.fit(X_train, y_train)
    preds = gscv.predict(X_test)
    confusion_matrix(y_test, preds)
