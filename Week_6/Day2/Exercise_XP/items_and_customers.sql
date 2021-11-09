
-- Items And Customers


-- -- 1.Use SQL to get the following from the database:-- --

-- All items, ordered by price (lowest to highest).
select * from items order by price asc;

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
select * from items where price >= 80 order by price desc;

-- The first 3 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
select first_name, last_name from customers order by last_name asc limit 3;

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
select last_name from customers order by last_name desc;

----------------------------------------------------------------------------------------
-- -- 2. Create a table named purchases. It should have 2 columns : customer_id and item_id.-- --
-- These columns are references from the tables customers and items. 

create table purchases (
item_id integer,
FOREIGN KEY(item_id) REFERENCES public.items (items_id),
customer_id integer,
FOREIGN KEY(customer_id) REFERENCES public.customers (customer_id)
);

-- Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?
Insert into purchases(customer_id) values 
((SELECT customer_id from customers WHERE first_name='Greg'));

-- Add 5 rows which reference existing customers and items.
Insert into purchases(customer_id, item_id)values 
((SELECT customer_id from customers WHERE first_name='Sandra'),(SELECT items_id from items WHERE price=300)),
((SELECT customer_id from customers WHERE first_name='Scott'),(SELECT items_id from items WHERE price=80)),
((SELECT customer_id from customers WHERE first_name='Trevor'),(SELECT items_id from items WHERE price=100)),
((SELECT customer_id from customers WHERE first_name='Melanie'),(SELECT items_id from items WHERE price=300));


--------------------------------------------------------------------------------------

-- --  3.Use SQL to get the following from the database: -- --

-- All purchases. Is this information useful to us? Not useful
select * from purchases;

-- All purchases, joining with the customers table.
select * from purchases inner join customers on purchases.customer_id = customers.customer_id;

-- Purchases of the customer with the ID equal to 4.
select * from purchases inner join customers on purchases.customer_id = customers.customer_id where customers.customer_id=4;

-- Purchases for a large desk AND a small desk
select * from purchases inner join items on purchases.item_id = items.items_id where name='Small Desk' or name='Large Desk';

------------------------------------------------------------------------------------------

-- -- 4. Create a purchase for Scott Scott – he bought a hard drive.-- --

-- Insert into customers(first_name, last_name) values ('Scott','Scott');
-- Insert into items(name,price) values('Hard Drive',200);
-- insert into purchases(customer_id , item_id) values
-- ((SELECT customer_id from customers WHERE first_name='Scott' and customer_id = 6),(SELECT items_id from items WHERE price=200));

-------------------------------------------------------------------------------------------

-- Use SQL to show all the customers who have made a purchase.
-- select customers.first_name, customers.last_name, items.name from purchases join items on purchases.item_id = items.items_id join customers on purchases.customer_id = customers.customer_id;






