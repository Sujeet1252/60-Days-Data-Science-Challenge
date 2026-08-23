from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello, Data Scientist!</h1>"


@app.route("/form", methods=["GET", "POST"])
def form():

    if request.method == "POST":

        dependents = request.form["dependents"]
        education = request.form["education"]
        self_employed = request.form["self_employed"]
        income = request.form["income"]
        loan_amount = request.form["loan_amount"]
        loan_term = request.form["loan_term"]
        cibil_score = request.form["cibil_score"]
        residential_assets = request.form["residential_assets"]
        commercial_assets = request.form["commercial_assets"]
        luxury_assets = request.form["luxury_assets"]
        bank_assets = request.form["bank_assets"]

        print("Dependents:", dependents)
        print("Education:", education)
        print("Self Employed:", self_employed)
        print("Income:", income)
        print("Loan Amount:", loan_amount)
        print("Loan Term:", loan_term)
        print("CIBIL Score:", cibil_score)
        print("Residential Assets:", residential_assets)
        print("Commercial Assets:", commercial_assets)
        print("Luxury Assets:", luxury_assets)
        print("Bank Assets:", bank_assets)

        return render_template(
            "form.html",
            prediction="Form submitted successfully!"
        )

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)