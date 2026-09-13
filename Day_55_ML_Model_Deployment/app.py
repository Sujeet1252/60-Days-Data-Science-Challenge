from flask import Flask, request
import pandas as pd
import joblib

from utils.validation import validate_house_data

MODEL_PATH = "model/house_price_pipeline.pkl"

app = Flask(__name__)

# Load the trained model

try:
    model = joblib.load(MODEL_PATH)
    print("Model loaded successfully.")

except Exception as error:
    model = None
    print(f"Error loading model: {error}")

# Home endpoint
@app.route("/")
def home():
    return{
        "message" : "House Price Prediction API",
        "version" : "1.0",
    }

# Health check

@app.route("/health", methods=["GET"])
def health():
    if model is None:
        return {"status": "Unhealthy",
                "model_Loaded": False}, 503
    return {"status": "Healthy",
            "model_Loaded": True}, 200

# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    error = validate_house_data(data)
    if error:
        return {
            "success": False,
            "error": error
        }, 400

    input_data = pd.DataFrame([
        {
            "area": data["area"],
            "bedrooms": data["bedrooms"],
            "bathrooms": data["bathrooms"],
            "age": data["age"]
        }
    ])

    try:
        prediction = model.predict(input_data)[0]

        return {
            "success": True,
            "message": "Prediction successful",
            "data": {
                "predicted_price": round(float(prediction), 2)
            }
        }, 200

    except Exception as error:
        return {
            "success": False,
            "error": str(error)
        }, 500

# Run the Flask application
if __name__ == "__main__":

    app.run(
        debug=True
    )