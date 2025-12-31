# Customer Churn Prediction – ML Deployment

An end-to-end Machine Learning project to predict customer churn, deployed using **FastAPI**, **Streamlit**, **Docker**, and **GitHub Actions CI/CD**.

---

## Overview

This project serves a trained customer churn prediction model through:
- A REST API built with FastAPI
- A user-friendly web interface built with Streamlit
- Dockerized deployment
- Automated CI/CD pipeline using GitHub Actions

---

## Tech Stack

- Python
- Scikit-learn
- FastAPI
- Streamlit
- Docker & Docker Compose
- GitHub Actions (CI/CD)

---

## Project Structure

customer-churn-fastapi/
├── app.py # FastAPI backend
├── streamlit_app.py # Streamlit UI
├── customer_churn_model.pkl # Trained ML model
├── encoders.pkl # Encoders
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .github/workflows/ci.yml
└── README.md

yaml
Copy code

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
