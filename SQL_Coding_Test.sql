CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary INT,
    hire_date DATE
);

INSERT INTO employees VALUES
(1,'Amit',50000,'2026-02-01'),
(2,'John',60000,'2025-01-01'),
(3,'Alice',70000,'2026-04-15'),
(4,'Emma',80000,'2024-12-01'),
(5,'David',70000,'2026-03-20');


CREATE TABLE tableA (
    id INT
);

CREATE TABLE tableB (
    id INT
);

INSERT INTO tableA VALUES
(1),(2),(3),(4);

INSERT INTO tableB VALUES
(2),(3),(5),(6);



CREATE TABLE logs (
    id INT,
    value VARCHAR(10)
);

INSERT INTO logs VALUES
(1,'A'),
(2,'A'),
(3,'B'),
(4,'B'),
(5,'B'),
(6,'C'),
(7,'D'),
(8,'D');



SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;



CREATE TABLE students (
    id INT,
    name VARCHAR(50)
);

INSERT INTO students VALUES
(1,'Amit'),
(2,'Amit'),
(3,'John'),
(4,'John'),
(5,'Alice');

DELETE FROM students
WHERE id NOT IN
(
    SELECT MIN(id)
    FROM students
    GROUP BY name
);

SELECT * FROM students;


SELECT a.id
FROM tableA a
INNER JOIN tableB b
ON a.id = b.id;


SELECT *
FROM employees
WHERE hire_date >=
DATE_SUB(CURDATE(), INTERVAL 6 MONTH);


SELECT DISTINCT value
FROM
(
    SELECT value,
           LAG(value)
           OVER(ORDER BY id) AS prev_value
    FROM logs
) t
WHERE value = prev_value;