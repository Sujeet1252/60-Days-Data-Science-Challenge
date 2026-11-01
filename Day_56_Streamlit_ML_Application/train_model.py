import os

try:
    import joblib  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]
except ImportError:  # pragma: no cover - handled at runtime
    joblib = None

import pandas as pd  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]

from sklearn.compose import ColumnTransformer  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]
from sklearn.linear_model import LinearRegression  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]
from sklearn.metrics import (  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]
    mean_absolute_error,
    r2_score,
)
from sklearn.model_selection import train_test_split  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]
from sklearn.pipeline import Pipeline  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]
from sklearn.preprocessing import StandardScaler  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]


# ============================================================
# PATHS
# ============================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data", "house_data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "model", "house_price_pipeline.pkl")

# ============================================================
# TRAIN MODEL
# ============================================================

def train_model():

    # --------------------------------------------------------
    # LOAD DATA
    # --------------------------------------------------------

    df = pd.read_csv(DATA_PATH)

    print("Dataset loaded successfully.")

    print(
        f"Dataset shape: {df.shape}"
    )

    print("\nDataset:")
    print(df)


    # --------------------------------------------------------
    # FEATURES AND TARGET
    # --------------------------------------------------------

    X = df[
        [
            "area",
            "bedrooms",
            "bathrooms",
            "age"
        ]
    ]

    y = df["price"]


    # --------------------------------------------------------
    # TRAIN TEST SPLIT
    # --------------------------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


    # --------------------------------------------------------
    # PREPROCESSING
    # --------------------------------------------------------

    numeric_features = [
        "area",
        "bedrooms",
        "bathrooms",
        "age"
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                StandardScaler(),
                numeric_features
            )
        ]
    )


    # --------------------------------------------------------
    # PIPELINE
    # --------------------------------------------------------

    pipeline = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "model",
                LinearRegression()
            )
        ]
    )


    # --------------------------------------------------------
    # TRAIN
    # --------------------------------------------------------

    pipeline.fit(
        X_train,
        y_train
    )

    print("\nModel trained successfully.")


    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    predictions = pipeline.predict(
        X_test
    )


    # --------------------------------------------------------
    # EVALUATION
    # --------------------------------------------------------

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    print("\n==============================")
    print("MODEL EVALUATION")
    print("==============================")

    print(
        f"MAE: {mae:.2f}"
    )

    print(
        f"R² Score: {r2:.4f}"
    )


    # --------------------------------------------------------
    # SAVE MODEL
    # --------------------------------------------------------

    os.makedirs(
        os.path.dirname(MODEL_PATH),
        exist_ok=True
    )

    joblib.dump(
        pipeline,
        MODEL_PATH
    )

    print(
        f"\nModel saved successfully:"
    )

    print(
        MODEL_PATH
    )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    train_model()