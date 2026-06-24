-- Create Index

CREATE INDEX idx_customer_id
ON orders(customer_id);

-- Analyze Query

EXPLAIN
SELECT *
FROM orders
WHERE customer_id = 101;

-- Optimize Join

CREATE INDEX idx_orders_customer
ON orders(customer_id);

CREATE INDEX idx_customers_customer
ON customers(customer_id);

EXPLAIN
SELECT
    c.name,
    o.order_id,
    o.amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;