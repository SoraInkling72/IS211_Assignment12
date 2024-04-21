DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS quiz;
DROP TABLE IF EXISTS quiz_results;

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);
INSERT INTO students VALUES (1, 'John', 'Williams');
INSERT INTO students VALUES (2, 'Sarah', 'Williams');
INSERT INTO students VALUES (3, 'John', 'Davis');
INSERT INTO students VALUES (4, 'Annie', 'Mei');
INSERT INTO students VALUES (5, 'Leon', 'Pollo');


CREATE TABLE quiz (
    id INTEGER PRIMARY KEY,
    subject TEXT,
    number_of_questions INTEGER,
    date_given DATE
);
INSERT INTO quiz VALUES (1, 'Algebra', 40, '04/03/2022');
INSERT INTO quiz VALUES (2, 'Calculus', 50, '05/02/2022');
INSERT INTO quiz VALUES (3, 'English 101', 36, '03/24/2022');
INSERT INTO quiz VALUES (4, 'Chemistry 101', 64, '04/19/2022');
INSERT INTO quiz VALUES (5, 'Project Management', 25, '02/28/2022');


CREATE TABLE quiz_results (
    student_id INTEGER PRIMARY KEY,
    student TEXT,
    quiz_id INTEGER,
  	student_score INTEGER
);
INSERT INTO quiz_results VALUES (1, 'John Williams', 2, 89);
INSERT INTO quiz_results VALUES (2, 'Sarah Williams', 5, 92);
INSERT INTO quiz_results VALUES (3, 'John Davis', 4, 93);
INSERT INTO quiz_results VALUES (4, 'Annie Mei', 1, 100);
INSERT INTO quiz_results VALUES (5, 'Leon Pollo', 3, 86);
