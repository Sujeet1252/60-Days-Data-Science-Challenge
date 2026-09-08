from flask import Blueprint, render_template, request, redirect, url_for, session  # type: ignore[reportMissingImports]

from werkzeug.security import (  # type: ignore[reportMissingImports]
    generate_password_hash,
    check_password_hash,
)

import sqlite3

from database.db import get_db_connection

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        connection = get_db_connection()

        try:
            connection.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )
            connection.commit()

        except sqlite3.IntegrityError:
            connection.close()
            return "Username already exists"

        connection.close()

        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        connection = get_db_connection()

        user = connection.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        connection.close()

        if user and check_password_hash(user["password"], password):

            session["user_id"] = user["id"]
            session["username"] = user["username"]

            return redirect(url_for("auth.dashboard"))

        return "Invalid username or password"

    return render_template("login.html")


@auth_bp.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template(
        "dashboard.html",
        username=session["username"]
    )


@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("auth.login"))