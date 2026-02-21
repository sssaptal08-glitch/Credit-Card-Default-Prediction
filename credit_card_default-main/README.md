# 💳 Credit Card Default Prediction

A Machine Learning web application that predicts whether a customer is likely to default on their credit card payment based on financial and demographic details.

📌 Project Overview

This project uses a Machine Learning classification model to predict credit card default risk.
The model is trained on the UCI Credit Card dataset and deployed using a Flask web application.

It helps financial institutions assess customer risk and make informed lending decisions.

📂 Dataset

Dataset Name: UCI Credit Card Default Dataset

File Used: UCI_Credit_Card.csv

Target Variable: default.payment.next.month

Number of Features: 23 input features

The dataset includes:

Credit limit

Gender

Education

Marriage status

Age

Repayment status (last 6 months)

Bill amounts (last 6 months)

Payment amounts (last 6 months)

🛠️ Technologies Used

🐍 Python

📊 Pandas & NumPy

🤖 Scikit-learn

🌐 Flask

📁 Pickle (for model serialization)

🧠 Machine Learning Model

Algorithm: Logistic Regression

Task Type: Binary Classification

Output:

Default

No Default

Also displays prediction probability.

The trained model is saved as:

Credit-Card-Default-Prediction/
│
├── app.py                          # Flask Application
├── model.pkl                       # Trained ML Model
├── UCI_Credit_Card.csv             # Dataset
├── Credit Card Default Prediction Using Python.ipynb  # Model Training Notebook
├── templates/
│   └── index.html                  # Frontend HTML
└── README.md                       # Project Documentation

⚙️ How It Works

User enters financial details in the web form.

Input data is processed and converted into numeric format.

Data is passed to the trained ML model.

Model predicts:

Whether the customer will default

Probability of default

Result is displayed on the webpage.

🚀 Installation & Setup
1️⃣ Clone the Repository

git clone https://github.com/your-username/credit-card-default-prediction.git
cd credit-card-default-prediction
