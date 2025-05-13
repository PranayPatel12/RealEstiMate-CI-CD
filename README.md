# RealEstiMate-CI-CD 🏡

RealEstiMate is a Machine Learning-powered web application that predicts house prices based on user input. It utilizes a Decision Tree Regression model and is deployed with FastAPI. The project also supports CI/CD workflows for smooth and automated deployment.

## 🚀 Features

- Predict house prices using trained ML models
- FastAPI-based backend for rapid API development
- HTML-based user interface using Jinja2 templates
- Handles user input and predicts price in real-time
- Input preprocessing with column alignment
- CI/CD ready (can be integrated with GitHub Actions or similar tools)

## 🧠 Model Overview

- Model: Decision Tree Regressor
- Trained on real estate data with features such as:
  - Area in sq. ft
  - Number of BHKs
  - Location coordinates (latitude, longitude)
  - RERA and resale status
  - Construction status and posting details

## 🗂️ Project Structure

RealEstiMate-CI-CD/
├── main.py # FastAPI app with prediction logic
├── HousePricePrediction.ipynb # Model training and evaluation
├── decision_tree_model.pkl # Trained ML model
├── model_columns.pkl # Feature columns used for training
├── Train.csv / Test.csv # Datasets
├── templates/
│ └── form.html # Web form for user input



## ⚙️ How to Run Locally

1. **Install dependencies**  
   Make sure you have Python 3.8+ and install packages:
   ```bash
   pip install -r requirements.txt
2. Start the FastAPI app
   uvicorn main:app --reload
3. Visit in browser
   Open http://127.0.0.1:8000 to access the prediction form.

📦 Sample Input Fields
POSTED_BY: Owner / Dealer / Builder

UNDER_CONSTRUCTION: 0 or 1

RERA: 0 or 1

BHK_NO: Number of bedrooms

BHK_OR_RK: BHK or RK

SQUARE_FT: Total area

READY_TO_MOVE: 0 or 1

RESALE: 0 or 1

LATITUDE and LONGITUDE: Location coordinates



🔄 CI/CD (Optional Integration)
This project can be integrated with CI/CD tools like:

GitHub Actions

Jenkins

Docker 

Pipeline can include:

Linting and testing the FastAPI code

Re-training and evaluating the model

Automatic deployment after successful commit



📌 Requirements

Python 3.8+

FastAPI

Pandas

Joblib

Uvicorn
