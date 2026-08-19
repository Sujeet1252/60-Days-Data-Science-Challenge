try:
    from flask import Flask, render_template, request  # type: ignore
except ModuleNotFoundError as exc:
    raise ModuleNotFoundError(
        "Flask is not installed. Install it with: pip install flask"
    ) from exc

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to Marks Calculator</h1>"


@app.route("/form", methods=["GET", "POST"])
def form():

    if request.method == "POST":

        python = float(request.form["python"])
        data_science = float(request.form["data_science"])
        sql = float(request.form["sql"])
        statistics = float(request.form["statistics"])
        machine_learning = float(request.form["machine_learning"])

        average = (
            python +
            data_science +
            sql +
            statistics +
            machine_learning
        ) / 5

        if average >= 90:
            grade = "A"
        elif average >= 80 :
            grade = "B"
        elif average >= 70:
            grade = "C"
        else:
            grade = "F"
        

        print("Python:", python)
        print("Data Science:", data_science)
        print("SQL:", sql)
        print("Statistics:", statistics)
        print("Machine Learning:", machine_learning)
        print("Average:", average)

        return render_template(
            "form.html",
            average=round(average, 2),
            grade=grade
        )

    return render_template(
        "form.html",
        average=None,
        grade=None
    )

if __name__ == "__main__":
    app.run(debug=True,
            port=5001
    )