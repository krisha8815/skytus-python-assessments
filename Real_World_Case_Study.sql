CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id)
    REFERENCES orders(order_id),
    FOREIGN KEY (product_id)
    REFERENCES products(product_id)
);


INSERT INTO customers VALUES
(1,'Amit','Ahmedabad'),
(2,'John','Mumbai'),
(3,'Alice','Delhi'),
(4,'Emma','Ahmedabad'),
(5,'David','Pune');

INSERT INTO products VALUES
(101,'Laptop',50000),
(102,'Mobile',20000),
(103,'Headphones',3000),
(104,'Keyboard',1500);

INSERT INTO orders VALUES
(1001,1,'2025-01-10',50000),
(1002,2,'2025-01-15',20000),
(1003,1,'2025-02-05',3000),
(1004,3,'2025-02-20',50000),
(1005,4,'2025-03-01',21500);

INSERT INTO order_items VALUES
(1001,101,1),
(1002,102,1),
(1003,103,1),
(1004,101,1),
(1005,102,1),
(1005,104,1);


//commands

SELECT
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;


SELECT
    c.customer_id,
    c.name
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;



SELECT
    p.product_name,
    SUM(oi.quantity) AS total_sold
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC
LIMIT 1;



SELECT
    MONTH(order_date) AS month_no,
    SUM(amount) AS total_sales
FROM orders
GROUP BY MONTH(order_date)
ORDER BY month_no;



SELECT
    c.customer_id,
    c.name,
    SUM(o.amount) AS total_purchase
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.amount) > 50000;


SELECT
    c.city,
    SUM(o.amount) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY revenue DESC
LIMIT 3;