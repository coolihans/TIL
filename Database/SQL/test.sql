SELECT MAX(balance), first_name FROM users;

SELECT AVG(balance), last_name, first_name FROM users;

SELECT first_name, last_name, balance FROM users
WHERE balance = (SELECT MAX(balance) FROM users);

SELECT * FROM users ORDER BY age ASC, balance DESC LIMIT 10;