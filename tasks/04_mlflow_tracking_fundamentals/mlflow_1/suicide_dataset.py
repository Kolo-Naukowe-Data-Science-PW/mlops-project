import pandas as pd
from sklearn.preprocessing import LabelEncoder


def convert_to_categorical(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    for column in columns:
        df[column] = df[column].astype("category")
    return df


def encode_categorical_features(df, columns):
    le = LabelEncoder()
    df_encoded = df.copy()
    for col in columns:
        df_encoded[col] = le.fit_transform(df[col])
    return df_encoded


def data_preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(
        columns=[
            "country-year",
            "suicides/100k pop",
            " gdp_for_year ($) ",
            "generation",
        ]
    )
    df = convert_to_categorical(df, ["country", "year", "sex", "age"])
    df = encode_categorical_features(df, ["country", "year", "sex", "age"])
    df = df.dropna()
    return df


def load_dataset() -> dict:
    raw_data = pd.read_csv("data/master.csv")
    preprocessed_data = data_preprocessing(raw_data)
    data = {
        "data": preprocessed_data.drop("country", axis=1),
        "target": preprocessed_data["country"],
    }
    return data


if __name__ == "__main__":
    data = load_dataset()
    print(data)
