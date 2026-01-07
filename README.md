📉 Customer Churn Prediction – ML Deployment with Ollama

An end-to-end Machine Learning project to predict customer churn, deployed using FastAPI and Streamlit, with Ollama (Gemma 2B) integrated to provide AI-powered explanations for predictions.

🚀 Overview

This project predicts whether a customer is likely to churn based on their service usage and account details.
It includes:

A trained ML churn prediction model

A FastAPI REST API for predictions

A Streamlit web application for user interaction

Ollama (Gemma 2B) for natural language explanations of predictions

Dockerized setup and CI/CD ready structure

🧠 Key Features

📊 Predicts Customer Churn (Yes / No)

📈 Returns Churn Probability

🤖 Uses Ollama (Gemma 2B) to explain why the customer may churn

🧩 Modular backend and frontend architecture

🐳 Docker-ready for deployment

🔁 CI/CD enabled using GitHub Actions

🛠️ Tech Stack

Python

Scikit-learn

FastAPI

Streamlit

Ollama (Gemma2:2B)

Docker & Docker Compose

GitHub Actions (CI/CD)

🦙 What is Ollama used for?

Ollama is used to run a local Large Language Model (Gemma 2B) that:

Explains churn predictions in simple English

Helps non-technical users understand model output

Adds an AI assistant layer to a traditional ML system


📁 Project Structure
customer-churn-fastapi/
├── app.py                     # FastAPI backend
├── streamlit_app.py           # Streamlit UI
├── customer_churn_model.pkl   # Trained ML model
├── encoders.pkl               # Feature encoders
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .github/workflows/ci.yml   # CI/CD pipeline
└── README.md


---

## Run Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt
2. Start FastAPI
bash
Copy code
uvicorn app:app --reload
API Docs: http://127.0.0.1:8000/docs

3. Start Streamlit
bash
Copy code
streamlit run streamlit_app.py
Run with Docker
bash
Copy code
docker-compose up --build
FastAPI: http://localhost:8000

Streamlit: http://localhost:8501

CI/CD Pipeline
Triggered on every push to the main branch

Automatically builds and pushes Docker images to DockerHub

Docker Image:

bash
Copy code
vinayak533/customer-churn-fastapi:latest
Author
Vinayak K V
BCA Graduate | Aspiring Data Scientist
GitHub: https://github.com/vinayak533

