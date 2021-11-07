-- CREATE TABLE items (
-- items_id SERIAL PRIMARY KEY,
-- name VARCHAR(50) NOT NULL,
-- price SMALLINT NOT NULL)
 -- INSERT INTO items (name,price)
-- VALUES ('Small Desk', 100)
-- INSERT INTO items (name,price)
-- VALUES ('Large Desk', 300)
-- INSERT INTO items (name,price)
-- VALUES ('Fan', 80)
 -- CREATE TABLE customers(
-- customer_id SERIAL PRIMARY KEY,
-- first_name VARCHAR (50) NOT NULL,
-- last_name VARCHAR (100) NOT NULL)
 -- INSERT INTO customers(first_name, last_name)
-- VALUES ('Greg','Jones'),
-- 		('Sandra','Jones'),
-- 		('Scott','Scott'),
-- 		('Trevor','Green'),
-- 		('Melanie','Johnson')

-- All the items.
-- select * from items

-- All the items with a price above 80 (80 not included).
-- Select * from items where price > 80

-- All the items with a price below 300. (300 included)
-- SELECT * from items WHERE price <=300

-- All customers whose last name is ‘Smith’ (What will be your outcome?)
-- SELECT * from customers where last_name = 'Smith'

-- All customers whose last name is ‘Jones’.
-- SELECT * from customers where last_name = 'Jones'

-- All customers whose firstname is not ‘Scott’.
SELECT * from customers where first_name IS NOT 'Scott'







