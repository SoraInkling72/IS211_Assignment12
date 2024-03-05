from flask import Flask, request, redirect, render_template, flash, g
import sqlite3

connection = sqlite3.connect("hw13.db")

app = Flask(__name__)

@app.route("/")
def index():
    conn = get_db().cursor()
    return render_template("quiz_template.html")

def get_db():
    db = getattr(g, 'hw13.db', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'hw13.db', None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(port=5000)