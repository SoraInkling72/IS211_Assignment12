from flask import Flask, request, redirect, render_template, flash, g, re
import sqlite3
import pickle
import os
app = Flask(__name__)

conn = sqlite3.connect("hw13.db")


@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login')
def enter_credentials():
    username = request.form["Username"]
    password = request.form["Password"]

    # validate username & password
    if re.match(r"admin", username):
        if re.match(r"password", password):
            return redirect("/dashboard")
        else:
            if not re.match(r"password", password):
                flash("Invalid password")
                return redirect("/")
    else:
        if not re.match(r"admin", username):
            flash("Invalid username")
            return redirect("/")

@app.route('/dashboard')
def dashboard():
    return redirect("/")

@app.route('/add_student', methods=["POST"])
def add_student():
    global student_list
    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(port=5000)