from fastapi import FastAPI
import pandas as pd
import pickle

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

    # Prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    return {
        "churn_prediction": "Yes" if prediction == 1 else "No",
        "churn_probability": round(float(probability), 3)
    }
