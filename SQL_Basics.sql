CREATE TABLE students (
    student_id INT,
    name VARCHAR(50),
    department VARCHAR(30),
    year INT,
    marks INT
);

INSERT INTO students VALUES
(1, 'Krisha', 'CSE', 2, 85),
(2, 'Nistha', 'IT', 3, 92),
(3, 'Harsh', 'CSE', 1, 78),
(4, 'Rima', 'ECE', 2, 65),
(5, 'Tamanna', 'CSE', 4, 88);

//commands
SELECT * FROM students;

SELECT name, department FROM students;

SELECT * FROM students WHERE marks > 75;

SELECT * FROM students WHERE department = 'CSE';

SELECT * FROM students ORDER BY marks DESC;

SELECT * FROM students ORDER BY marks DESC LIMIT 3;