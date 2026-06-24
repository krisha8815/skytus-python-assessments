CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100) NOT NULL
);


CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_amount DECIMAL(10,2),

    FOREIGN KEY (user_id)
    REFERENCES users(user_id)
);



INSERT INTO users VALUES
(1, 'Amit', 'amit@gmail.com', 'pass123'),
(2, 'John', 'john@gmail.com', 'pass456'),
(3, 'Alice', 'alice@gmail.com', 'pass789');

INSERT INTO orders VALUES
(101, 1, 1500.00),
(102, 1, 2000.00),
(103, 2, 3500.00),
(104, 3, 1000.00),
(105, 3, 2500.00);



CREATE INDEX idx_email
ON users(email);


CREATE VIEW user_order_summary AS
SELECT
    u.user_id,
    u.username,
    u.email,
    COUNT(o.order_id) AS total_orders,
    SUM(o.order_amount) AS total_amount
FROM users u
LEFT JOIN orders o
ON u.user_id = o.user_id
GROUP BY u.user_id, u.username, u.email;


SELECT * FROM user_order_summary;