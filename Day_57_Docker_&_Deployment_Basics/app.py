import os

try:
    import pandas as pd  # type: ignore
except ImportError:
    pd = None

try:
    import streamlit as st  # type: ignore
except ImportError:
    st = None

try:
    import joblib  # type: ignore
except ImportError:
    joblib = None

from utils.validation import validate_house_data


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CONSTANTS
# ============================================================

MODEL_PATH = "model/house_price_pipeline.pkl"
DATA_PATH = "data/house_data.csv"


# ============================================================
# SESSION STATE
# ============================================================

if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []

if "area" not in st.session_state:
    st.session_state.area = 1500

if "bedrooms" not in st.session_state:
    st.session_state.bedrooms = 3

if "bathrooms" not in st.session_state:
    st.session_state.bathrooms = 2

if "age" not in st.session_state:
    st.session_state.age = 5


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


# ============================================================
# LOAD DATASET
# ============================================================

@st.cache_data
def load_dataset():
    return pd.read_csv(DATA_PATH)


# ============================================================
# CHECK MODEL
# ============================================================

if not os.path.exists(MODEL_PATH):

    st.error(
        "❌ ML model not found.\n\n"
        "Please run `python train_model.py` first."
    )

    st.stop()


try:

    model = load_model()

except Exception as e:

    st.error(
        f"❌ Unable to load the ML model.\n\n"
        f"Error: {e}"
    )

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🏠 Property Controls")

    st.write(
        "Use the controls below to prepare "
        "your property information."
    )

    st.divider()

    # --------------------------------------------------------
    # QUICK PRESETS
    # --------------------------------------------------------

    st.subheader("⚡ Quick Presets")

    preset = st.selectbox(
        "Choose a property type",
        [
            "Custom",
            "Small House",
            "Family House",
            "Large House",
            "Luxury House"
        ]
    )

    if st.button(
        "Apply Preset",
        use_container_width=True
    ):

        if preset == "Small House":

            st.session_state.area = 900
            st.session_state.bedrooms = 2
            st.session_state.bathrooms = 1
            st.session_state.age = 12

        elif preset == "Family House":

            st.session_state.area = 1500
            st.session_state.bedrooms = 3
            st.session_state.bathrooms = 2
            st.session_state.age = 5

        elif preset == "Large House":

            st.session_state.area = 2100
            st.session_state.bedrooms = 4
            st.session_state.bathrooms = 3
            st.session_state.age = 4

        elif preset == "Luxury House":

            st.session_state.area = 2700
            st.session_state.bedrooms = 5
            st.session_state.bathrooms = 4
            st.session_state.age = 2

        st.rerun()

    st.divider()

    # --------------------------------------------------------
    # MODEL STATUS
    # --------------------------------------------------------

    st.subheader("🤖 Model Status")

    st.success("Model Loaded")

    st.write("Model: Linear Regression")
    st.write("Task: Regression")
    st.write("Preprocessing: StandardScaler")
    st.write("Persistence: Joblib")

    st.divider()

    # --------------------------------------------------------
    # HISTORY CONTROLS
    # --------------------------------------------------------

    st.subheader("🧹 History")

    if st.button(
        "Clear Prediction History",
        use_container_width=True
    ):

        st.session_state.prediction_history = []

        st.success("History cleared.")

        st.rerun()


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🏠 House Price Prediction System")

st.write(
    "An interactive Machine Learning application "
    "for estimating house prices."
)

st.caption(
    "Built with Python • Scikit-learn • Joblib • Streamlit"
)

st.divider()


# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "🔮 Prediction",
        "📊 History & Analytics",
        "📁 Dataset",
        "ℹ️ About"
    ]
)


# ============================================================
# TAB 1 — PREDICTION
# ============================================================

with tab1:

    st.header("Enter Property Details")

    st.write(
        "Provide the property information below "
        "and click **Predict House Price**."
    )

    # --------------------------------------------------------
    # INPUT FORM
    # --------------------------------------------------------

    with st.form("prediction_form"):

        col1, col2 = st.columns(2)

        with col1:

            area = st.number_input(
                "🏠 Area (sq ft)",
                min_value=300,
                max_value=10000,
                value=st.session_state.area,
                step=100
            )

            bedrooms = st.number_input(
                "🛏️ Bedrooms",
                min_value=1,
                max_value=10,
                value=st.session_state.bedrooms,
                step=1
            )

        with col2:

            bathrooms = st.number_input(
                "🚿 Bathrooms",
                min_value=1,
                max_value=10,
                value=st.session_state.bathrooms,
                step=1
            )

            age = st.number_input(
                "📅 House Age (years)",
                min_value=0,
                max_value=100,
                value=st.session_state.age,
                step=1
            )

        st.divider()

        predict_button = st.form_submit_button(
            "🔮 Predict House Price",
            use_container_width=True
        )


    # ========================================================
    # PREDICTION
    # ========================================================

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

                prediction = float(prediction)

                price_per_sqft = prediction / area


                # ------------------------------------------------
                # SUCCESS MESSAGE
                # ------------------------------------------------

                st.success(
                    "✅ Prediction generated successfully!"
                )


                # ------------------------------------------------
                # MAIN RESULT
                # ------------------------------------------------

                st.subheader(
                    "💰 Estimated House Price"
                )

                result_col1, result_col2 = st.columns(2)

                with result_col1:

                    st.metric(
                        "Predicted Price",
                        f"₹{prediction:,.2f}"
                    )

                with result_col2:

                    st.metric(
                        "Estimated Price / Sq Ft",
                        f"₹{price_per_sqft:,.2f}"
                    )


                # ------------------------------------------------
                # PROPERTY SUMMARY
                # ------------------------------------------------

                st.subheader(
                    "🏡 Property Summary"
                )

                summary_col1, summary_col2, summary_col3, summary_col4 = st.columns(4)

                with summary_col1:

                    st.metric(
                        "Area",
                        f"{area:,} sq ft"
                    )

                with summary_col2:

                    st.metric(
                        "Bedrooms",
                        bedrooms
                    )

                with summary_col3:

                    st.metric(
                        "Bathrooms",
                        bathrooms
                    )

                with summary_col4:

                    st.metric(
                        "Age",
                        f"{age} years"
                    )


                # ------------------------------------------------
                # SAVE HISTORY
                # ------------------------------------------------

                st.session_state.prediction_history.append(
                    {
                        "Area": area,
                        "Bedrooms": bedrooms,
                        "Bathrooms": bathrooms,
                        "Age": age,
                        "Predicted Price": round(
                            prediction,
                            2
                        ),
                        "Price per Sq Ft": round(
                            price_per_sqft,
                            2
                        )
                    }
                )


                # ------------------------------------------------
                # RESULT DETAILS
                # ------------------------------------------------

                with st.expander(
                    "🔍 View Prediction Details"
                ):

                    st.write(
                        "The prediction was generated using "
                        "the trained Scikit-learn pipeline."
                    )

                    st.write(
                        "**Input features:**"
                    )

                    st.json(
                        {
                            "area": area,
                            "bedrooms": bedrooms,
                            "bathrooms": bathrooms,
                            "age": age
                        }
                    )

                    st.write(
                        "**Model:** Linear Regression"
                    )

                    st.write(
                        "**Preprocessing:** StandardScaler"
                    )


            except Exception as e:

                st.error(
                    f"❌ Prediction failed: {e}"
                )


# ============================================================
# TAB 2 — HISTORY & ANALYTICS
# ============================================================

with tab2:

    st.header("📊 Prediction History")

    history = st.session_state.prediction_history

    if not history:

        st.info(
            "No predictions have been made yet. "
            "Go to the Prediction tab and generate a prediction."
        )

    else:

        history_df = pd.DataFrame(history)

        # ----------------------------------------------------
        # SUMMARY METRICS
        # ----------------------------------------------------

        total_predictions = len(history_df)

        average_price = history_df[
            "Predicted Price"
        ].mean()

        highest_price = history_df[
            "Predicted Price"
        ].max()

        lowest_price = history_df[
            "Predicted Price"
        ].min()


        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Total Predictions",
                total_predictions
            )

        with col2:

            st.metric(
                "Average Price",
                f"₹{average_price:,.0f}"
            )

        with col3:

            st.metric(
                "Highest Price",
                f"₹{highest_price:,.0f}"
            )

        with col4:

            st.metric(
                "Lowest Price",
                f"₹{lowest_price:,.0f}"
            )


        st.divider()


        # ----------------------------------------------------
        # HISTORY TABLE
        # ----------------------------------------------------

        st.subheader("Prediction Records")

        st.dataframe(
            history_df,
            use_container_width=True
        )


        # ----------------------------------------------------
        # CHART
        # ----------------------------------------------------

        st.subheader(
            "📈 Prediction Trend"
        )

        chart_data = history_df[
            ["Predicted Price"]
        ]

        st.line_chart(
            chart_data,
            use_container_width=True
        )


        # ----------------------------------------------------
        # PRICE PER SQ FT
        # ----------------------------------------------------

        st.subheader(
            "💵 Price per Square Foot"
        )

        st.bar_chart(
            history_df[
                ["Price per Sq Ft"]
            ],
            use_container_width=True
        )


# ============================================================
# TAB 3 — DATASET
# ============================================================

with tab3:

    st.header("📁 Training Dataset")

    try:

        df = load_dataset()

        st.write(
            f"Dataset contains **{len(df)} records**."
        )

        st.dataframe(
            df,
            use_container_width=True
        )


        st.subheader(
            "📊 Dataset Statistics"
        )

        st.dataframe(
            df.describe(),
            use_container_width=True
        )


    except Exception as e:

        st.error(
            f"Unable to load dataset: {e}"
        )


# ============================================================
# TAB 4 — ABOUT
# ============================================================

with tab4:

    st.header(
        "ℹ️ About This Project"
    )

    st.write(
        """
        This project is a Machine Learning based
        House Price Prediction System.

        The application uses a trained Linear Regression
        model to estimate house prices based on property
        characteristics.
        """
    )

    st.subheader(
        "🎯 Machine Learning Features"
    )

    st.markdown(
        """
        - Area
        - Number of bedrooms
        - Number of bathrooms
        - House age
        """
    )

    st.subheader(
        "🤖 Machine Learning Pipeline"
    )

    st.markdown(
        """
        **Input Data → StandardScaler → Linear Regression → Prediction**
        """
    )

    st.subheader(
        "🛠️ Technologies"
    )

    st.markdown(
        """
        - Python
        - Pandas
        - Scikit-learn
        - Joblib
        - Streamlit
        """
    )

    st.subheader(
        "📚 What I Learned"
    )

    st.markdown(
        """
        - Loading a trained ML model
        - Model persistence using Joblib
        - Streamlit UI development
        - Interactive widgets
        - Forms
        - Session state
        - Prediction history
        - Data visualization
        - Error handling
        - ML application deployment concepts
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Day 56 — Streamlit ML Application | "
    "60-Day Data Science Challenge"
)