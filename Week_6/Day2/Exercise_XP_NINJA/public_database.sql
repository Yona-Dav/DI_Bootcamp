-- -- -- -- Exercise 1 : Bonus Public Database (Continuation Of XP)-- -- -- --

-- 1. Fetch the last 2 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
select first_name, last_name from customers order by last_name desc limit 2;

-- 2. Use SQL to delete all purchases made by Scott.
delete from purchases where purchases.customer_id =(select customer_id from customers where first_name = 'Scott');

-- 3. Does Scott still exist in the customers table, even though he has been deleted? Try and find him. 
select * from customers where first_name = 'Scott'; -- He still exists

-- 4. Join purchases with the customers table, so that Scott’s order will appear, although instead of the customer’s first and last name, you should only see empty/blank.
select * from purchases full outer join customers on purchases.customer_id = customers.customer_id;


-- 5. Join purchases with the customers table, so that Scott’s order will NOT appear.
select * from purchases inner join customers on purchases.customer_id = customers.customer_id;
