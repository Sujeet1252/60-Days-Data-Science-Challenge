try:
    from flask import (  # type: ignore[import-not-found]
        Flask,
        render_template,
        request,
        redirect,
        url_for,
        session,
    )
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Flask is not installed. Please install it with: pip install flask"
    ) from exc

import sqlite3

try:
    from werkzeug.security import (  # type: ignore[import-not-found]
        generate_password_hash,
        check_password_hash,
    )
except ImportError:  # pragma: no cover
    import hashlib
    import hmac

    def generate_password_hash(password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def check_password_hash(stored_password, password):
        return hmac.compare_digest(
            stored_password,
            hashlib.sha256(password.encode("utf-8")).hexdigest(),
        )


app = Flask(__name__)

app.secret_key = "change-this-secret-key"


def get_db_connection():

    connection = sqlite3.connect(
        "users.db"
    )

    connection.row_factory = sqlite3.Row

    return connection


@app.route("/")
def home():

    return """
    <h1>Authentication Application</h1>

    <a href="/register">Register</a>
    <br>
    <a href="/login">Login</a>
    """


@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        hashed_password = generate_password_hash(
            password
        )

        connection = get_db_connection()

        try:

            connection.execute(
                """
                INSERT INTO users
                (username, password)
                VALUES (?, ?)
                """,
                (username, hashed_password)
            )

            connection.commit()

        except sqlite3.IntegrityError:

            connection.close()

            return "Username already exists!"

        connection.close()

        return redirect(
            url_for("login")
        )

    return render_template(
        "register.html"
    )


@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        connection = get_db_connection()

        user = connection.execute(
            """
            SELECT * FROM users
            WHERE username = ?
            """,
            (username,)
        ).fetchone()

        connection.close()

        if user and check_password_hash(
            user["password"],
            password
        ):

            session["user_id"] = user["id"]

            session["username"] = user["username"]

            return redirect(
                url_for("dashboard")
            )

        return "Invalid username or password"

    return render_template(
        "login.html"
    )


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    return render_template(
        "dashboard.html",
        username=session["username"]
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("login")
    )


if __name__ == "__main__":

    app.run(debug=True)