import os
import pickle

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


DATA_PATH = "data/house_data.csv"
MODEL_PATH = "model/house_price_pipeline.pkl"


def train_model():
# Load the dataset
    df = pd.read_csv(DATA_PATH)

    print("Dataset loaded successfully.")
    print(f"Shape: {df.shape}")

# Select features and target variable
    X = df[
        [
            "area",
            "bedrooms",
            "bathrooms",
            "age"
        ]
    ]

    y = df["price"]

# Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

# Define the preprocessing steps for numeric features
    numeric_features = [
        "area",
        "bedrooms",
        "bathrooms",
        "age"
    ]

# Create a column transformer for preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", StandardScaler(), numeric_features)
        ]
    )

# Create a pipeline that combines preprocessing and model training
    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", LinearRegression())
        ]
    )

# Train the model
    pipeline.fit(X_train, y_train)

# Evaluate the model
    predictions = pipeline.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("\nModel evaluation:")
    print("-------------------")
    print(f"MAE: {mae:.2f}")
    print(f"R² Score: {r2:.2f}")

# Model Directory Creation
    os.makedirs("model", exist_ok=True)

# Save the trained model pipeline
    joblib.dump(pipeline, MODEL_PATH)
    print(f"\nModel saved successfully at : {MODEL_PATH}")

if __name__ == "__main__":
    train_model()