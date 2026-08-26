from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

import sqlite3

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


# --------------------------------------------------
# Flask Application
# --------------------------------------------------

app = Flask(__name__)


# Secret key required for Flask sessions
# This is suitable for learning.
# For production, use an environment variable.
app.secret_key = "day50-learning-secret-key"


# --------------------------------------------------
# Database Configuration
# --------------------------------------------------

DATABASE = "users.db"


def get_db_connection():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection


# --------------------------------------------------
# Home Route
# --------------------------------------------------

@app.route("/")
def home():

    return render_template("home.html")


# --------------------------------------------------
# Registration Route
# --------------------------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username", "").strip()

        password = request.form.get("password", "")


        # Check empty fields
        if not username or not password:

            flash(
                "Username and password are required.",
                "error"
            )

            return redirect(url_for("register"))


        # Check password length
        if len(password) < 6:

            flash(
                "Password must contain at least 6 characters.",
                "error"
            )

            return redirect(url_for("register"))


        # Hash password
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
                (
                    username,
                    hashed_password
                )
            )

            connection.commit()


        except sqlite3.IntegrityError:

            connection.close()

            flash(
                "Username already exists!",
                "error"
            )

            return redirect(
                url_for("register")
            )


        connection.close()


        flash(
            "Registration successful! Please login.",
            "success"
        )

        return redirect(
            url_for("login")
        )


    return render_template(
        "register.html"
    )


# --------------------------------------------------
# Login Route
# --------------------------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        ).strip()

        password = request.form.get(
            "password",
            ""
        )


        # Check empty fields
        if not username or not password:

            flash(
                "Username and password are required.",
                "error"
            )

            return redirect(
                url_for("login")
            )


        connection = get_db_connection()


        user = connection.execute(
            """
            SELECT *

            FROM users

            WHERE username = ?
            """,
            (username,)
        ).fetchone()


        connection.close()


        # Verify username and password
        if user and check_password_hash(
            user["password"],
            password
        ):

            # Store user information in session
            session["user_id"] = user["id"]

            session["username"] = user["username"]


            flash(
                "Login successful!",
                "success"
            )


            return redirect(
                url_for("dashboard")
            )


        # Invalid credentials
        flash(
            "Invalid username or password.",
            "error"
        )

        return redirect(
            url_for("login")
        )


    return render_template(
        "login.html"
    )


# --------------------------------------------------
# Protected Dashboard
# --------------------------------------------------

@app.route("/dashboard")
def dashboard():

    # Check whether user is logged in
    if "user_id" not in session:

        flash(
            "Please login to access the dashboard.",
            "error"
        )

        return redirect(
            url_for("login")
        )


    return render_template(
        "dashboard.html",
        username=session["username"]
    )


# --------------------------------------------------
# Logout Route
# --------------------------------------------------

@app.route("/logout")
def logout():

    # Remove all session data
    session.clear()


    flash(
        "You have been logged out successfully.",
        "success"
    )


    return redirect(
        url_for("login")
    )


# --------------------------------------------------
# Run Application
# --------------------------------------------------

if __name__ == "__main__":

    app.run(debug=True)