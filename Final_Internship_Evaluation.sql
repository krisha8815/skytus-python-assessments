CREATE TABLE Students (
student_id INT PRIMARY KEY,
student_name VARCHAR(50),
room_no INT,
phone VARCHAR(15)
);

CREATE TABLE MealPlans (
plan_id INT PRIMARY KEY,
plan_name VARCHAR(30),
monthly_fee DECIMAL(10,2)
);

CREATE TABLE StudentPlans (
student_id INT,
plan_id INT,
start_date DATE,
PRIMARY KEY(student_id, plan_id),
FOREIGN KEY(student_id) REFERENCES Students(student_id),
FOREIGN KEY(plan_id) REFERENCES MealPlans(plan_id)
);

CREATE TABLE Menu (
menu_id INT PRIMARY KEY,
meal_type VARCHAR(20),
food_item VARCHAR(50),
menu_date DATE
);

CREATE TABLE Attendance (
attendance_id INT PRIMARY KEY,
student_id INT,
menu_id INT,
status VARCHAR(10),
FOREIGN KEY(student_id) REFERENCES Students(student_id),
FOREIGN KEY(menu_id) REFERENCES Menu(menu_id)
);

CREATE TABLE Payments (
payment_id INT PRIMARY KEY,
student_id INT,
amount DECIMAL(10,2),
payment_date DATE,
FOREIGN KEY(student_id) REFERENCES Students(student_id)
);


-- SAMPLE DATA

INSERT INTO Students VALUES
(1,'Amit',101,'9876543210'),
(2,'John',102,'9876543211'),
(3,'Alice',103,'9876543212'),
(4,'Emma',104,'9876543213'),
(5,'David',105,'9876543214');

INSERT INTO MealPlans VALUES
(1,'Basic',3000),
(2,'Premium',5000);

INSERT INTO StudentPlans VALUES
(1,1,'2025-01-01'),
(2,2,'2025-01-01'),
(3,1,'2025-01-01'),
(4,2,'2025-01-01'),
(5,1,'2025-01-01');

INSERT INTO Menu VALUES
(1,'Breakfast','Poha','2025-01-01'),
(2,'Lunch','Dal Rice','2025-01-01'),
(3,'Dinner','Paneer Curry','2025-01-01'),
(4,'Breakfast','Upma','2025-01-02'),
(5,'Lunch','Veg Biryani','2025-01-02');

INSERT INTO Attendance VALUES
(1,1,1,'Present'),
(2,2,1,'Present'),
(3,3,1,'Absent'),
(4,4,1,'Present'),
(5,5,1,'Present');

INSERT INTO Payments VALUES
(1,1,3000,'2025-01-05'),
(2,2,5000,'2025-01-05'),
(3,3,3000,'2025-01-05'),
(4,4,5000,'2025-01-05'),
(5,5,3000,'2025-01-05');


-- 15 BUSINESS QUERIES

-- 1. Display all students

SELECT * FROM Students;

-- 2. Display all meal plans

SELECT * FROM MealPlans;

-- 3. Students with Premium Plan

SELECT s.student_name
FROM Students s
JOIN StudentPlans sp
ON s.student_id = sp.student_id
WHERE sp.plan_id = 2;

-- 4. Total Students

SELECT COUNT(*) AS Total_Students
FROM Students;

-- 5. Total Payment Collected

SELECT SUM(amount) AS Total_Collection
FROM Payments;

-- 6. Students Absent

SELECT s.student_name
FROM Students s
JOIN Attendance a
ON s.student_id = a.student_id
WHERE a.status = 'Absent';

-- 7. Daily Menu

SELECT *
FROM Menu
WHERE menu_date = '2025-01-01';

-- 8. Attendance Count

SELECT status, COUNT(*) AS Count
FROM Attendance
GROUP BY status;

-- 9. Student Payment Details

SELECT s.student_name, p.amount
FROM Students s
JOIN Payments p
ON s.student_id = p.student_id;

-- 10. Students Without Payment

SELECT s.student_name
FROM Students s
LEFT JOIN Payments p
ON s.student_id = p.student_id
WHERE p.payment_id IS NULL;

-- 11. Highest Payment

SELECT MAX(amount) AS Highest_Payment
FROM Payments;

-- 12. Average Payment

SELECT AVG(amount) AS Average_Payment
FROM Payments;

-- 13. Plan-wise Student Count

SELECT plan_id,
COUNT(*) AS Student_Count
FROM StudentPlans
GROUP BY plan_id;

-- 14. Students Attending Breakfast

SELECT s.student_name
FROM Students s
JOIN Attendance a
ON s.student_id = a.student_id
JOIN Menu m
ON a.menu_id = m.menu_id
WHERE m.meal_type = 'Breakfast';

-- 15. Monthly Revenue

SELECT MONTH(payment_date) AS Month_No,
SUM(amount) AS Revenue
FROM Payments
GROUP BY MONTH(payment_date);


-- QUERY OPTIMIZATION

-- Optimization 1
CREATE INDEX idx_student_name
ON Students(student_name);

-- Optimization 2
CREATE INDEX idx_payment_student
ON Payments(student_id);

-- Optimization 3
CREATE INDEX idx_attendance_student
ON Attendance(student_id);


-- EXPLAIN QUERIES

EXPLAIN
SELECT *
FROM Students
WHERE student_name = 'Amit';

EXPLAIN
SELECT *
FROM Payments
WHERE student_id = 1;

EXPLAIN
SELECT *
FROM Attendance
WHERE student_id = 2;


-- VIEW CREATION

CREATE VIEW StudentPaymentSummary AS
SELECT
s.student_id,
s.student_name,
SUM(p.amount) AS Total_Paid
FROM Students s
JOIN Payments p
ON s.student_id = p.student_id
GROUP BY s.student_id, s.student_name;

SELECT * FROM StudentPaymentSummary;

