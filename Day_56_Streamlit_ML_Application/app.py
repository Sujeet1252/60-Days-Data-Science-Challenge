import pandas as pd
import joblib
import streamlit as st

from utils.validation import validate_house_data


# =========================================
# PAGE CONFIGURATION
# =========================================

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)


# =========================================
# MODEL CONFIGURATION
# =========================================

MODEL_PATH = "model/house_price_pipeline.pkl"


# =========================================
# MODEL LOADING
# =========================================

@st.cache_resource
def load_model():

    return joblib.load(
        MODEL_PATH
    )


try:

    model = load_model()

except Exception:

    st.error(
        "Unable to load the ML model."
    )

    st.stop()


# =========================================
# TITLE
# =========================================

st.title(
    "🏠 House Price Prediction System"
)

st.write(
    "Estimate a house price using a trained "
    "Machine Learning regression model."
)

st.divider()


# =========================================
# SIDEBAR INPUTS
# =========================================

st.sidebar.header(
    "🏠 House Information"
)


area = st.sidebar.number_input(
    "Area (sq ft)",
    min_value=1,
    value=1500,
    step=100
)


bedrooms = st.sidebar.number_input(
    "Bedrooms",
    min_value=1,
    value=3,
    step=1
)


bathrooms = st.sidebar.number_input(
    "Bathrooms",
    min_value=1,
    value=2,
    step=1
)


age = st.sidebar.number_input(
    "House Age (years)",
    min_value=0,
    value=5,
    step=1
)


predict_button = st.sidebar.button(
    "🔮 Predict Price"
)


# =========================================
# PROPERTY SUMMARY
# =========================================

st.header(
    "Property Summary"
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Area",
        f"{area:,} sq ft"
    )


with col2:

    st.metric(
        "Bedrooms",
        bedrooms
    )


with col3:

    st.metric(
        "Bathrooms",
        bathrooms
    )


with col4:

    st.metric(
        "Age",
        f"{age} years"
    )


st.divider()


# =========================================
# PREDICTION
# =========================================

if predict_button:

    error = validate_house_data(
        area,
        bedrooms,
        bathrooms,
        age
    )

    if error:

        st.error(error)

    else:

        input_data = pd.DataFrame(
            [
                {
                    "area": area,
                    "bedrooms": bedrooms,
                    "bathrooms": bathrooms,
                    "age": age
                }
            ]
        )

        try:

            prediction = model.predict(
                input_data
            )[0]

            st.success(
                "Prediction generated successfully."
            )

            st.subheader(
                "Estimated House Price"
            )

            st.metric(
                "Predicted Price",
                f"₹{prediction:,.2f}"
            )

            st.info(
                "The prediction is generated from "
                "the saved trained ML pipeline."
            )

        except Exception:

            st.error(
                "Prediction failed. Please try again."
            )


# =========================================
# ABOUT
# =========================================

with st.expander(
    "ℹ️ About this project"
):

    st.write(
        """
        This Streamlit application provides a user-friendly
        interface for a trained house price prediction model.

        The model uses the following features:

        - Area
        - Bedrooms
        - Bathrooms
        - House Age

        The trained preprocessing and regression model are
        stored together as a Scikit-learn pipeline.
        """
    )


# =========================================
# MODEL INFORMATION
# =========================================

with st.expander(
    "🤖 Model Information"
):

    st.write(
        "Model: Linear Regression"
    )

    st.write(
        "Task: Regression"
    )

    st.write(
        "Preprocessing: StandardScaler"
    )

    st.write(
        "Model persistence: Joblib"
    )


# =========================================
# FOOTER
# =========================================

st.divider()

st.caption(
    "Day 56 — Streamlit ML Application | "
    "60-Day Data Science Challenge"
)