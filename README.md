# 📉 Customer Churn Prediction System with FastAPI, Streamlit & Ollama

## 📌 Summary

This project is an end-to-end Machine Learning deployment that predicts customer churn using an XGBoost model and provides AI-powered explanations using a local LLM (Gemma 2B via Ollama). The system includes a FastAPI backend, Streamlit frontend, Docker deployment, and CI/CD pipeline for production-ready ML serving.

---

## 🛠️ Technologies Used

* Python
* Scikit-learn / XGBoost
* FastAPI
* Streamlit
* Ollama (Gemma 2B LLM)
* Docker & Docker Compose
* GitHub Actions (CI/CD)
* Pandas & NumPy

---

## ✨ Features

* Predicts customer churn (Yes / No)
* Returns churn probability score
* AI-generated explanations for predictions using LLM
* REST API for model inference
* Interactive Streamlit web interface
* Dockerized deployment environment
* CI/CD pipeline with GitHub Actions
* Modular backend and frontend architecture

---

## ⌨️ Keyboard Shortcuts

```
Ctrl + C   → Stop server
Enter      → Submit command
Up Arrow   → Reuse previous command
```

---

## ⚙️ Process

```
1. User enters customer details in Streamlit UI
2. Data is sent to FastAPI backend
3. ML model predicts churn probability
4. Ollama LLM generates explanation
5. Results are displayed to the user
```

---

## 🏗️ How I Built It

```
- Trained a customer churn prediction model using XGBoost
- Saved model and encoders using pickle
- Built FastAPI backend for inference API
- Created Streamlit UI for user interaction
- Integrated Ollama (Gemma 2B) for AI explanations
- Containerized the application using Docker
- Implemented CI/CD pipeline using GitHub Actions
```

---

## 📚 What I Learned

```
- End-to-end ML deployment workflow
- FastAPI backend development for ML models
- Streamlit dashboard creation
- Docker containerization and orchestration
- CI/CD automation using GitHub Actions
- Integrating LLMs into traditional ML systems
- Model serving and API design
```

---

## 🚀 How It Could Be Improved

```
- Deploy to cloud platforms (AWS, GCP, Azure)
- Add user authentication system
- Implement model monitoring and logging
- Add real-time database integration
- Improve UI/UX with advanced visualization
- Use larger LLM for more accurate explanations
```

---

## ▶️ How to Run the Project

### Clone Repository

```bash
git clone https://github.com/yourusername/customer-churn-fastapi.git
cd customer-churn-fastapi
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start FastAPI Server

```bash
uvicorn app:app --reload
```

API Docs:
http://127.0.0.1:8000/docs

### Start Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## 🐳 Run with Docker

```bash
docker-compose up --build
```

FastAPI: http://localhost:8000
Streamlit: http://localhost:8501

---

## 📂 Project Structure

```
customer-churn-fastapi/
│
├── app.py                     # FastAPI backend
├── streamlit_app.py           # Streamlit frontend
├── customer_churn_model.pkl   # Trained ML model
├── encoders.pkl               # Feature encoders
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── .github/workflows/
│   └── ci.yml                 # CI/CD pipeline
│
└── README.md
```

---

## ⭐ About

A production-ready machine learning system for predicting customer churn with AI-powered explanations using FastAPI, Streamlit, Docker, CI/CD, and Ollama.
