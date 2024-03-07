CREATE SCHEMA student_quiz_scores;


CREATE TABLE students(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);
INSERT INTO students VALUES (1, 'John', 'Williams')
INSERT INTO students VALUES (2, 'Sarah', 'Williams')
INSERT INTO students VALUES (3, 'John', 'Davis')
INSERT INTO students VALUES (4, 'Garfield', 'Bucklar')
INSERT INTO students VALUES (5, 'Sandra', 'Erwin')


CREATE TABLE quiz(
    id INTEGER PRIMARY KEY,
    subject TEXT,
    number_of_questions INTEGER,
    date_given DATE
);
INSERT INTO quiz VALUES (1, 'Algebra', 40, '2022/04/03')
INSERT INTO quiz VALUES (2, 'Calculus', 50, '2022/05/02')
INSERT INTO quiz VALUES (3, 'English 101', 36, '2022/03/24')
INSERT INTO quiz VALUES (4, 'Chemistry 101', 64, '2022/04/19')
INSERT INTO quiz VALUES (5, 'Project Management', 25, '2022/02/28')


CREATE TABLE student_quiz_results(
    students.id INTEGER,
    quiz.id INTEGER,
  	student_score INTEGER
);
INSERT INTO student_quiz_results VALUES (1, 40, 89)
INSERT INTO student_quiz_results VALUES (3, 4, 93)
INSERT INTO student_quiz_results VALUES (2, 4, 93)