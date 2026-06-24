CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    account_name VARCHAR(50),
    balance DECIMAL(10,2)
);


INSERT INTO accounts VALUES
(101, 'Amit', 10000),
(102, 'John', 15000);


//commands

SELECT * FROM accounts;



START TRANSACTION;

INSERT INTO accounts
VALUES (103, 'Alice', 20000);

SELECT * FROM accounts;

ROLLBACK;

SELECT * FROM accounts;



START TRANSACTION;

INSERT INTO accounts
VALUES (103, 'Alice', 20000);

COMMIT;

SELECT * FROM accounts;


START TRANSACTION;

UPDATE accounts
SET balance = balance - 2000
WHERE account_id = 101;

UPDATE accounts
SET balance = balance + 2000
WHERE account_id = 102;

COMMIT;

SELECT * FROM accounts;