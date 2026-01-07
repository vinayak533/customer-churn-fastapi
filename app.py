from fastapi import FastAPI
import pandas as pd
import pickle
from ollama import chat

# Initialize app
app = FastAPI(title="Customer Churn Prediction API")

# Load model
with open("customer_churn_model.pkl", "rb") as f:
    model_data = pickle.load(f)

model = model_data["model"]
feature_names = model_data["features_names"]

# Load encoders
with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)


@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API is running"}


@app.post("/predict")
def predict_churn(data: dict):

    # Convert input to DataFrame
    input_df = pd.DataFrame([data])

    # Encode categorical columns
    for column, encoder in encoders.items():
        input_df[column] = encoder.transform(input_df[column])

    # Reorder columns
    input_df = input_df[feature_names]

    # ML Prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    churn_label = "Yes" if prediction == 1 else "No"
    churn_prob = round(float(probability), 3)

    # -------- OLLAMA EXPLANATION --------
    prompt = f"""
You are a data science assistant.

Prediction result:
Customer Churn: {churn_label}
Churn Probability: {churn_prob}

Customer data:
{data}

Explain the churn result in simple business language.
Mention 2–3 key reasons and suggest one retention action.
Limit response to 70 words.
"""

    ai_response = chat(
        model="gemma2:2b",
        messages=[{"role": "user", "content": prompt}]
    )

    explanation = ai_response["message"]["content"]

    return {
        "churn_prediction": churn_label,
        "churn_probability": churn_prob,
        "ai_explanation": explanation
    }
