**# 💳 Credit Card Default Prediction**

A Machine Learning web application that predicts whether a customer is likely to default on their credit card payment based on financial and demographic details.

**📌 Project Overview**

This project uses a Machine Learning classification model to predict credit card default risk.
The model is trained on the UCI Credit Card dataset and deployed using a Flask web application.

It helps financial institutions assess customer risk and make informed lending decisions.

**📂 Dataset**

Dataset Name: UCI Credit Card Default Dataset

File Used: UCI_Credit_Card.csv

Target Variable: default.payment.next.month

Number of Features: 23 input features

**The dataset includes:**

Credit limit

Gender

Education

Marriage status

Age

Repayment status (last 6 months)

Bill amounts (last 6 months)

Payment amounts (last 6 months)

**🛠️ Technologies Used**

🐍 Python

📊 Pandas & NumPy

🤖 Scikit-learn

🌐 Flask

📁 Pickle (for model serialization)

**🧠 Machine Learning Model**

Algorithm: Logistic Regression

Task Type: Binary Classification

Output:

Default

No Default

Also displays prediction probability.

The trained model is saved as:

model.pkl

**🗂️ Project Structure**

Credit-Card-Default-Prediction/
│
├── app.py                          # Flask Application
├── model.pkl                       # Trained ML Model
├── UCI_Credit_Card.csv             # Dataset
├── Credit Card Default Prediction Using Python.ipynb  # Model Training Notebook
├── templates/
│   └── index.html                  # Frontend HTML
└── README.md                       # Project Documentation

**⚙️ How It Works**

User enters financial details in the web form.

Input data is processed and converted into numeric format.

Data is passed to the trained ML model.

Model predicts:

Whether the customer will default

Probability of default

Result is displayed on the webpage.

**🚀 Installation & Setup**

1️⃣ Clone the Repository

git clone https://github.com/your-username/credit-card-default-prediction.git

cd credit-card-default-prediction

2️⃣ Install Dependencies

pip install -r requirements.txt


If requirements.txt is not available:

pip install flask pandas scikit-learn numpy

3️⃣ Run the Application

python app.py

Then open in browser:

http://127.0.0.1:5000/

**📊 Model Training**

Model training steps (in Jupyter Notebook):

Data Cleaning

Exploratory Data Analysis (EDA)

Feature Selection

Train-Test Split

Model Training (Logistic Regression)

Model Evaluation

Save Model using Pickle

**📈 Future Improvements**

Add more ML algorithms (Random Forest, XGBoost)

Improve UI design

Deploy on:

Render

Heroku

AWS

Add real-time database support

Improve model accuracy using feature engineering

**🎯 Use Cases**

Banks & Financial Institutions

Loan Approval Systems

Risk Management Systems

FinTech Applications

**👨‍💻 Author**

Sujal
CSE (AIML) Engineer

**📜 License**

This project is for educational purposes only.
