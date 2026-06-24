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
(3, 'Rima', 'CSE', 1, 78),
(4, 'Tamanna', 'ECE', 2, 65),
(5, 'Mitva', 'CSE', 4, 88);

//commands
SELECT COUNT(*) AS Total_Students
FROM students;

SELECT AVG(marks) AS Average_Marks
FROM students;

SELECT MAX(marks) AS Highest_Marks,
       MIN(marks) AS Lowest_Marks
FROM students;

SELECT department,
       AVG(marks) AS Average_Marks
FROM students
GROUP BY department;

SELECT department,
       AVG(marks) AS Average_Marks
FROM students
GROUP BY department
HAVING AVG(marks) > 70;