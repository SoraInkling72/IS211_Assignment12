from flask import Flask, request, redirect, render_template, flash, g, abort
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("hw13.db")
DATABASE = '/path/to/hw13.db'

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
    con = sqlite3.connect('hw13.db')
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT);")
        cur.execute(
            "CREATE TABLE quiz(id INTEGER PRIMARY KEY, subject TEXT, number_of_questions INTEGER, date_given DATE);")
        cur.execute("CREATE TABLE quiz_results(subject TEXT, student_score INTEGER);")
        cur.execute("SELECT CONCAT(students.first_name, ' ', students.last_name) AS 'Student', "
                    "quiz.subject AS 'Subject', quiz_results.student_score AS 'Quiz Score' FROM students "
                    "LEFT JOIN (quiz RIGHT JOIN quiz_results ON subject.quiz = subject.quiz_results ORDER "
                    "BY subject.quiz DESC) ON id.students = id_quiz;")

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login', methods=["GET", "POST"])
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

@app.route('/dashboard', methods=["POST"])
def dashboard():
    return render_template("dashboard.html")

@app.route('/add_student', methods=["POST"])
def add_student():
    global student_list
    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(port=5000)