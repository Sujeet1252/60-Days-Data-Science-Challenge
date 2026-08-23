from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load Day 45 trained model
model = joblib.load("models/employee_salary_model.joblib")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        age = int(request.form["age"])
        experience = int(request.form["experience"])
        education = request.form["education"]
        job_title = request.form["job_title"]
        gender = request.form["gender"]
        location = request.form["location"]

        new_employee = pd.DataFrame({
            "Age": [age],
            "Experience": [experience],
            "Education": [education],
            "Job_Title": [job_title],
            "Gender": [gender],
            "Location": [location]
        })

        prediction = model.predict(new_employee)[0]

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)