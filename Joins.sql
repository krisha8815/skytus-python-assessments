CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT
);

INSERT INTO departments VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance');

INSERT INTO employees VALUES
(101, 'John', 1, 45000),
(102, 'Alice', 2, 60000),
(103, 'Bob', 2, 70000),
(104, 'Emma', 2, 55000),
(105, 'David', 3, 40000),
(106, 'Chris', NULL, 50000);

//commands
SELECT e.emp_name, d.dept_name
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id;

SELECT *
FROM employees
WHERE salary > 50000;

SELECT d.dept_name,
       SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name;

SELECT d.dept_name,
       COUNT(*) AS employee_count
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING COUNT(*) > 2;

SELECT *
FROM employees
WHERE dept_id IS NULL;