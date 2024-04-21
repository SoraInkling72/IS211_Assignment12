from flask import Flask, request, redirect, render_template, flash, g
import re
import sqlite3

app = Flask(__name__)
app.secret_key = 'keyblade47'

conn = sqlite3.connect("hw13.db")
DATABASE = 'hw13.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def create_tables():
    conn = sqlite3.connect('hw13.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT);")
        cur.execute(
            "CREATE TABLE quiz(id INTEGER PRIMARY KEY, subject TEXT, number_of_questions INTEGER, date_given DATE);")
        cur.execute(
            "CREATE TABLE quiz_results(student_id INTEGER PRIMARY KEY, student TEXT, quiz_id INTEGER, "
            "student_score INTEGER);")


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
    conn = get_db()
    student_list = conn.execute('SELECT * FROM students').fetchall()
    quiz_list = conn.execute('SELECT * FROM quiz').fetchall()
    quiz_results = conn.execute('SELECT * FROM quiz_results').fetchall()
    conn.close()
    return render_template("dashboard.html", student_list=student_list,
                           quiz_list=quiz_list, quiz_results=quiz_results)


@app.route('/student/add', methods=["POST", "GET"])
def add_student():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        if not re.match(r"^[A-Za-z]+$", first_name):
            flash("Please input proper name")
        elif not re.match(r"^[A-Za-z]+$", last_name):
            flash("Please input proper name")
        else:
            conn = get_db()
            conn.execute('INSERT INTO students (first_name, last_name) VALUES (?, ?)',
                         (first_name, last_name))
            conn.commit()
            conn.close()
            return redirect("/dashboard")
    return render_template("add_student.html")


@app.route('/quiz/add', methods=["POST", "GET"])
def add_quiz():
    if request.method == "POST":
        subject = request.form["subject"]
        questions = request.form["questions"]
        date = request.form["date"]
        if not re.match(r"^[A-Za-z0-9]+$", subject):
            flash("Please input proper subject name")
        elif not re.match(r"^[0-9]+$", questions):
            flash("Please input valid number")
        else:
            conn = get_db()
            conn.execute('INSERT INTO quiz (subject, number_of_questions, date_given) VALUES (?, ?, ?)',
                         (subject, questions, date))
            conn.commit()
            conn.close()
            return redirect("/dashboard")
    return render_template("add_quiz.html")


@app.route('/results/add', methods=["POST", "GET"])
def add_quiz_result():
    if request.method == "POST":
        conn = get_db()
        select_student = conn.execute("SELECT * FROM students, CONCAT(first_name, ' ', last_name) AS 'Name' FROM students")
        select_quiz = conn.execute("SELECT id, subject FROM quiz")
        conn.commit()
        conn.close()
        quiz_score = request.form["score"]
        return redirect("/dashboard")
    return render_template("add_quiz_result.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
