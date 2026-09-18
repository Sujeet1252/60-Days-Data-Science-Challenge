import importlib

try:
    flask_module = importlib.import_module("flask")
    Flask = flask_module.Flask
    request = flask_module.request
    HTTPException = flask_module.HTTPException
except ModuleNotFoundError as exc:
    raise ModuleNotFoundError(
        "Flask is not installed. Please install it with: pip install flask"
    ) from exc

try:
    pd = importlib.import_module("pandas")
except ModuleNotFoundError as exc:
    raise ModuleNotFoundError(
        "pandas is not installed. Please install it with: pip install pandas"
    ) from exc

try:
    joblib = importlib.import_module("joblib")
except ModuleNotFoundError as exc:
    raise ModuleNotFoundError(
        "joblib is not installed. Please install it with: pip install joblib"
    ) from exc

from utils.validation import validate_house_data


MODEL_PATH = "model/house_price_pipeline.pkl"


app = Flask(__name__)


# --------------------------------
# Load ML model
# --------------------------------

try:

    model = joblib.load(MODEL_PATH)

    print("ML model loaded successfully.")

except Exception as error:

    model = None

    print(
        f"Failed to load model: {error}"
    )


# --------------------------------
# Home
# --------------------------------

@app.route("/")
def home():

    return {
        "message": "House Price Prediction API",
        "version": "1.0"
    }


# --------------------------------
# Health
# --------------------------------

@app.route(
    "/health",
    methods=["GET"]
)
def health():

    if model is None:

        return {
            "status": "unhealthy",
            "model_loaded": False
        }, 503

    return {
        "status": "healthy",
        "model_loaded": True
    }, 200


# --------------------------------
# Prediction
# --------------------------------

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    data = request.get_json()

    error = validate_house_data(data)

    if error:

        return {
            "success": False,
            "error": error
        }, 400

    input_data = pd.DataFrame(
        [
            {
                "area": data["area"],
                "bedrooms": data["bedrooms"],
                "bathrooms": data["bathrooms"],
                "age": data["age"]
            }
        ]
    )

    try:

        prediction = model.predict(
            input_data
        )[0]

        return {
            "success": True,
            "message": "Prediction successful",
            "data": {
                "predicted_price": round(
                    float(prediction),
                    2
                )
            }
        }, 200

    except Exception:

        return {
            "success": False,
            "error": "Prediction failed"
        }, 500


# --------------------------------
# Error handlers
# --------------------------------

@app.errorhandler(404)
def not_found(error):

    return {
        "success": False,
        "error": "Endpoint not found"
    }, 404


@app.errorhandler(405)
def method_not_allowed(error):

    return {
        "success": False,
        "error": "HTTP method not allowed"
    }, 405


@app.errorhandler(Exception)
def handle_exception(error):

    if isinstance(error, HTTPException):

        return {
            "success": False,
            "error": error.description
        }, error.code

    return {
        "success": False,
        "error": "Internal server error"
    }, 500


# --------------------------------
# Run
# --------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )