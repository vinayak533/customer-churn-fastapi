import streamlit as st
import requests
from ollama import chat

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

st.title("📉 Customer Churn Prediction")
st.write("Enter customer details to predict churn")

API_URL = "http://localhost:8000/predict"

with st.form("churn_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=100)
    phone = st.selectbox("Phone Service", ["Yes", "No"])
    multiple = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    device = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    tech = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment = st.selectbox("Payment Method", [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ])
    monthly = st.number_input("Monthly Charges", min_value=0.0)
    total = st.number_input("Total Charges", min_value=0.0)

    use_ai = st.checkbox("🤖 Generate AI explanation (Ollama)")

    submit = st.form_submit_button("Predict Churn")

if submit:
    payload = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple,
        "InternetService": internet,
        "OnlineSecurity": security,
        "OnlineBackup": backup,
        "DeviceProtection": device,
        "TechSupport": tech,
        "StreamingTV": tv,
        "StreamingMovies": movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()

        st.success(f"Prediction: {result['churn_prediction']}")
        st.info(f"Churn Probability: {result['churn_probability']}")

        # -------- OLLAMA EXPLANATION --------
        if use_ai:
            with st.spinner("Generating AI explanation..."):
                prompt = f"""
You are a data science assistant helping a telecom business team.

Churn Prediction: {result['churn_prediction']}
Churn Probability: {result['churn_probability']}

Customer details:
{payload}

Explain why the customer is likely or unlikely to churn.
Mention 2–3 key reasons and suggest ONE retention action.
Use simple business language. Max 80 words.
"""

                ai_response = chat(
                    model="gemma2:2b",
                    messages=[{"role": "user", "content": prompt}]
                )

                st.subheader("🤖 AI Explanation (Ollama)")
                st.write(ai_response["message"]["content"])

    else:
        st.error("Error connecting to API")
