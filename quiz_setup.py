from flask import Flask, request, redirect, render_template, flash, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'keyblade47'

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

@app.route('/dashboard', methods=["POST"])
def dashboard(student_list, quiz_list, quiz_results):
    return render_template("dashboard.html", student_list=student_list,
                           quiz_list=quiz_list, quiz_results=quiz_results)

@app.route('/add_student', methods=["POST"])
def add_student():
    global student_list
    return redirect("/dashboard")

@app.route('/add_quiz', methods=["POST"])
def add_quiz():
    global quiz_list
    return redirect("/dashboard")

@app.route('/add_quiz_result', methods=["POST"])
def add_quiz_result():
    global quiz_results
    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(port=5000)