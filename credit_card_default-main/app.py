from flask import Flask, render_template, request
import pandas as pd
import pickle
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

app = Flask(__name__)

model_path = "model.pkl"

# Train a model if it doesn't exist
if not os.path.exists(model_path):
    print("model.pkl not found — training a dummy model...")

    # Create dummy dataset (23 features to match expected input)
    X, y = make_classification(n_samples=1000, n_features=23, random_state=42)
    model = LogisticRegression()
    model.fit(X, y)

    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print("Model saved as model.pkl")
else:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    print("Loaded model from model.pkl")

# Mappings for categorical input
education_mapping = {
    "Graduate School": 1,
    "University": 2,
    "High School": 3,
    "Others": 4
}
marriage_mapping = {
    "Married": 1,
    "Single": 2,
    "Others": 3
}

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        try:
            # Parse and convert input data
            def get_int(name): return int(request.form.get(name, 0))

            limit_bal = get_int("limit_bal")
            sex = 1 if request.form.get("sex") == "Male" else 2
            education = education_mapping.get(request.form.get("education"), 4)
            marriage = marriage_mapping.get(request.form.get("marriage"), 3)
            age = get_int("age")

            pay_status = [get_int(f"pay_status_{m}") for m in ["sept", "aug", "jul", "jun", "may", "apr"]]
            bill_amt = [get_int(f"bill_amt_{m}") for m in ["sept", "aug", "jul", "jun", "may", "apr"]]
            pay_amt = [get_int(f"pay_amt_{m}") for m in ["sept", "aug", "jul", "jun", "may", "apr"]]

            # Prepare input for model
            user_data = pd.DataFrame([[
                limit_bal, sex, education, marriage, age,
                *pay_status, *bill_amt, *pay_amt
            ]])

            result = model.predict(user_data)[0]
            prob = model.predict_proba(user_data)[0][1]

            prediction = f"Prediction: {'No Default' if result == 1 else 'Default'} (Probability: {prob:.2%})"

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
