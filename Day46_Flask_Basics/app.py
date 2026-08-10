## Flask Application Routing

from flask import Flask

app = Flask(__name__)


@app.route("/",methods=["GET"])
def home():
    return "Hello, Data Scientist!"

@app.route("/index",methods=["GET"])
def index():
    return "Welcome to the Index Page!"

if __name__ == "__main__":
    app.run(debug=True)