**🚀 Insurance Premium Prediction API (FastAPI + ML)**

This project demonstrates how to deploy a Machine Learning model using FastAPI and integrate it with a frontend interface.

The model predicts an individual's Insurance Premium Category as:

🟢 Low

🟡 Medium

🔴 High

based on personal, lifestyle, and financial attributes.

This project follows an industry-standard workflow:

Model Building → API Development → Frontend Integration

📌 Project Overview

This project is divided into three major phases:

🧠 Model Building (Scikit-learn)

⚡ API Development (FastAPI)

🎨 Frontend Integration (Streamlit)

🧠 1️⃣ Model Building
📊 Dataset

A toy dataset created specifically for demonstration.

The goal is to show model deployment rather than achieve real-world accuracy.

🔹 Input Features

Age

Weight

Height

Annual Income (LPA)

Smoker Status

City

Occupation

🔹 Target Variable

Insurance Premium Category:

High

Medium

Low

🔧 Feature Engineering

Instead of using raw data directly, engineered features were created:

BMI → calculated using weight & height

Age Group → categorized age ranges

Lifestyle Risk → derived from BMI + smoker status

City Tier → categorized cities

🤖 Model Used

Random Forest Classifier

Built using Scikit-learn Pipeline

One-Hot Encoding for categorical features

Final trained model exported as:

model.pkl

⚡ 2️⃣ FastAPI Deployment

The trained model is served using FastAPI.

🔹 Endpoint
POST /predict

Why POST?

Because the client sends data to the server for processing (model inference).

🔹 Data Validation

A Pydantic model is used to:

Validate input types

Enforce realistic value ranges

Ensure clean API requests

🔹 Computed Fields

The API automatically calculates:

BMI

Age Group

Lifestyle Risk

City Tier

This means:
✔ Users only send raw data
✔ The backend handles feature engineering

🔹 Model Inference Flow

Load model.pkl

Convert input to Pandas DataFrame

Pass data to model

Return prediction as JSON response

Example Response
{
  "premium_category": "High"
}

🎨 3️⃣ Frontend (Streamlit)

A simple Streamlit web app is used to interact with the API.

🔹 How It Works

User enters details in a form

Clicks Predict Premium Category

Streamlit sends POST request using requests

FastAPI returns prediction

Result is displayed on screen

🛠 Tech Stack

Python

Scikit-learn

Pandas

FastAPI

Pydantic

Uvicorn

Streamlit

📂 Project Structure
Insurance_premium_prediction_model/
│
├── model.pkl
├── main.py
├── streamlit_app.py
├── requirements.txt
└── README.md

▶️ How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run FastAPI Server
uvicorn main:app --reload


Server runs at:

http://127.0.0.1:8000


Swagger Docs:

http://127.0.0.1:8000/docs

3️⃣ Run Streamlit App
streamlit run streamlit_app.py
