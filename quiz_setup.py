from flask import Flask, request, redirect, render_template, flash, current_app, g
import re
import click
import sqlite3

app = Flask(__name__)
app.secret_key = 'keyblade47'

conn = sqlite3.connect("hw13.db")
DATABASE = 'hw13.db'


def get_db_connection():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db_connection()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def create_tables():
    conn = sqlite3.connect('hw13.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT);")
        cur.execute(
            "CREATE TABLE quiz(id INTEGER PRIMARY KEY, subject TEXT, number_of_questions INTEGER, date_given DATE);")
        cur.execute("CREATE TABLE quiz_results(student TEXT, student_score INTEGER);")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # validate username & password
        if username == "admin" and password == "password":
            return redirect('/dashboard')
        else:
            flash("Please input correct credentials")
            return redirect('/')

    return render_template("login.html")


@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    conn = get_db_connection()
    student_list = conn.execute('SELECT * FROM students').fetchall()
    quiz_list = conn.execute('SELECT * FROM quiz').fetchall()
    quiz_results = conn.execute('SELECT * FROM quiz_results').fetchall()
    conn.close()
    return render_template("dashboard.html", student_list=student_list,
                           quiz_list=quiz_list, quiz_results=quiz_results)


@app.route('/add_student', methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        if not re.match(r"^[A-Za-z]+$", first_name):
            flash("Please input proper name")
        elif not re.match(r"^[A-Za-z]+$", last_name):
            flash("Please input proper name")
        else:
            conn = get_db_connection()
            conn.execute('UPDATE students SET first_name = ?, last_name = ?',
                         (first_name, last_name))
            conn.commit()
            conn.close()
            return redirect("dashboard.html")

    return redirect("add_student.html")


@app.route('/add_quiz', methods=["POST"])
def add_quiz():
    return redirect("/dashboard")


@app.route('/add_quiz_result', methods=["POST"])
def add_quiz_result():
    return redirect("/dashboard")


if __name__ == "__main__":
    app.run(port=5000, debug=True)