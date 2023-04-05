from dataclasses import dataclass

import mlflow
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from suicide_dataset import load_dataset


class MLflowConfig:
    EXPERIMENT_NAME = "knds-mlops-mlflow-task"
    EXPERIMENT_ID = mlflow.create_experiment(EXPERIMENT_NAME)


@dataclass
class TestConfig:
    clf: any
    hyperparam: str
    hyperparam_values: list


def main() -> None:
    suicides = load_dataset()
    features, labels = suicides["data"], suicides["target"]
    features_train, features_test, labels_train, labels_test = train_test_split(
        features, labels, test_size=0.2, random_state=42
    )

    test_configs = [
        TestConfig(
            clf=DecisionTreeClassifier,
            hyperparam="max_depth",
            hyperparam_values=[1, 2, 5, 10, 20],
        ),
        TestConfig(
            clf=RandomForestClassifier,
            hyperparam="n_estimators",
            hyperparam_values=[1, 2, 5, 10, 20],
        ),
        TestConfig(
            clf=GradientBoostingClassifier,
            hyperparam="n_estimators",
            hyperparam_values=[1, 2, 5, 10, 20],
        ),
    ]

    for test_config in test_configs:
        for idx, hyperparam_value in enumerate(test_config.hyperparam_values):
            test_args = {test_config.hyperparam: hyperparam_value}
            clf = test_config.clf(**test_args)
            clf.fit(features_train, labels_train)
            labels_pred = clf.predict(features_test)
            accuracy = accuracy_score(labels_test, labels_pred)

            RUN_NAME = f"{test_config.clf.__name__}_{idx}"
            with mlflow.start_run(
                experiment_id=MLflowConfig.EXPERIMENT_ID, run_name=RUN_NAME
            ) as run:
                mlflow.log_param(test_config.hyperparam, hyperparam_value)
                mlflow.log_metric("accuracy", accuracy)
                mlflow.sklearn.log_model(clf, "classifier")


if __name__ == "__main__":
    main()
