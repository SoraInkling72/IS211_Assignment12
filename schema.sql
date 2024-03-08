CREATE SCHEMA student_quiz_scores;


CREATE TABLE students(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);
INSERT INTO students VALUES (1, 'John', 'Williams');
INSERT INTO students VALUES (2, 'Sarah', 'Williams');
INSERT INTO students VALUES (3, 'John', 'Davis');
INSERT INTO students VALUES (4, 'Garfield', 'Bucklar');
INSERT INTO students VALUES (5, 'Sandra', 'Erwin');


CREATE TABLE quiz(
    id INTEGER PRIMARY KEY,
    subject TEXT,
    number_of_questions INTEGER,
    date_given DATE
);
INSERT INTO quiz VALUES (1, 'Algebra', 40, '2022/04/03');
INSERT INTO quiz VALUES (2, 'Calculus', 50, '2022/05/02');
INSERT INTO quiz VALUES (3, 'English 101', 36, '2022/03/24');
INSERT INTO quiz VALUES (4, 'Chemistry 101', 64, '2022/04/19');
INSERT INTO quiz VALUES (5, 'Project Management', 25, '2022/02/28');


CREATE TABLE quiz_results(
    subject INTEGER,
  	student_score INTEGER
);
INSERT INTO quiz_results VALUES ('Algebra', 89);
INSERT INTO quiz_results VALUES ('Project Management', 92);
INSERT INTO quiz_results VALUES ('English 101', 93);
INSERT INTO quiz_results VALUES ('Calculus', 100);
INSERT INTO quiz_results VALUES ('Chemistry 101', 86);


CREATE TABLE quiz_results(
    subject INTEGER,
  	student_score INTEGER
);
INSERT INTO quiz_results VALUES ('Algebra', 89);
INSERT INTO quiz_results VALUES ('Project Management', 92);
INSERT INTO quiz_results VALUES ('English 101', 93);
INSERT INTO quiz_results VALUES ('Calculus', 100);
INSERT INTO quiz_results VALUES ('Chemistry 101', 86);


CREATE TABLE quiz_results(
    subject INTEGER,
  	student_score INTEGER
);
INSERT INTO quiz_results VALUES ('Algebra', 89);
INSERT INTO quiz_results VALUES ('Project Management', 92);
INSERT INTO quiz_results VALUES ('English 101', 93);
INSERT INTO quiz_results VALUES ('Calculus', 100);
INSERT INTO quiz_results VALUES ('Chemistry 101', 86);


SELECT CONCAT(students.first_name, ' ', students.last_name) AS 'Student',
       quiz.subject AS 'Subject',
       quiz_results.student_score AS 'Quiz Score'
FROM students
LEFT JOIN (quiz RIGHT JOIN quiz_results
           ON subject.quiz = subject.quiz_results
           ORDER BY subject.quiz DESC)
ON id.students = id_quiz;