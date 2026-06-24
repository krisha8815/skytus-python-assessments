CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT
);

INSERT INTO employees VALUES
(101, 'Amit', 1, 50000),
(102, 'Krisha', 2, 60000),
(103, 'Nistha', 2, 70000),
(104, 'Rima', 3, 55000),
(105, 'Tamanna', 1, 80000),
(106, 'Mitva', 2, 65000);

//commands

SELECT *
FROM employees
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees
);


SELECT dept_id,
       SUM(salary) AS total_salary
FROM employees
GROUP BY dept_id
ORDER BY total_salary DESC
LIMIT 1;


SELECT *
FROM employees
WHERE salary =
(
    SELECT MAX(salary)
    FROM employees
    WHERE salary <
    (
        SELECT MAX(salary)
        FROM employees
    )
);


SELECT *
FROM employees
WHERE dept_id =
(
    SELECT dept_id
    FROM employees
    WHERE emp_name = 'Amit'
);