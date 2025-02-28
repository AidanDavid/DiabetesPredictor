# Dependancies

from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the saved model

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Home page route

@app.route("/")
def home():
    return render_template("home.html")

# Prediction route

@app.route("/predict", methods=["POST"])
def predict():

    # Gather form data (names match 'name' attributes in home.html)

    data_dict = {
        "HighBP": int(request.form["HighBP"]),
        "HighChol": int(request.form["HighChol"]),
        "CholCheck": int(request.form["CholCheck"]),
        "BMI": float(request.form["BMI"]),
        "Smoker": int(request.form["Smoker"]),
        "Stroke": int(request.form["Stroke"]),
        "HeartDiseaseorAttack": int(request.form["HeartDiseaseorAttack"]),
        "PhysActivity": int(request.form["PhysActivity"]),
        "Fruits": int(request.form["Fruits"]),
        "Veggies": int(request.form["Veggies"]),
        "HvyAlcoholConsump": int(request.form["HvyAlcoholConsump"]),
        "AnyHealthcare": int(request.form["AnyHealthcare"]),
        "NoDocbcCost": int(request.form["NoDocbcCost"]),
        "GenHlth": int(request.form["GenHlth"]),
        "MentHlth": float(request.form["MentHlth"]),
        "PhysHlth": float(request.form["PhysHlth"]),
        "DiffWalk": int(request.form["DiffWalk"]),
        "Sex": int(request.form["Sex"]),
        "Age": float(request.form["Age"]),
        "Education": int(request.form["Education"]),
        "Income": int(request.form["Income"])
    }
    
    # Convert data to a DataFrame

    input_df = pd.DataFrame([data_dict])
    
    # Make a prediction

    prediction = model.predict(input_df)[0]
    
    # Interpret the prediction

    if prediction == 0:
        result_text = "No Diabetes (Predicted class 0)"
    elif prediction == 1:
        result_text = "Prediabetes (Predicted class 1)"
    else:
        result_text = "Diabetes (Predicted class 2)"
    
    # Show the result

    return render_template("home.html", result=result_text)

if __name__ == "__main__":
   
    # Run the app
    app.run(debug=True)
