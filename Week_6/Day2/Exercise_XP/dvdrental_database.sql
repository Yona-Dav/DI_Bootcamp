-- Database: dvdrental

-- DROP DATABASE dvdrental;

-- 1.In the dvdrental database write a query to select all the columns from the “customer” table.
select * from customer;

-- 2.Write a query to display the names (first_name, last_name) using an alias named “full_name”.
select concat(first_name,' ',last_name) as full_name from customer;

-- 3.Write a query to select all the create_date from the “customer” table (there should be no duplicates).
select distinct create_date from customer;

--4.Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
select * from customer order by first_name desc;

-- 5.Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
select film_id, title, description, release_year, rental_rate from film order by rental_rate asc;

-- 6.Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.
select address, phone from address where district = 'Texas';

--7.Write a query to retrieve all movie details where the movie id is either 15 or 150.
select * from film where film_id = 15 or film_id = 150;

--8.Write a query which should check if your favorite movie exists in the database.
-- Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
select film_id, title, description, length, rental_rate from film where title = 'Titanic';
 

--9.Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
select film_id, title, description, length, rental_rate from film where title like 'Ti%';

--10.Write a query which will find the 10 cheapest movies.
select * from film order by rental_rate asc limit 10;

--11. Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
select * from film order by rental_rate asc limit 10 offset 10;

-- Bonus: Try to not use LIMIT. 
Select * from 
 (
     Select ROW_NUMBER() OVER ( order by rental_rate asc) as Row_Number, * 
     from film
 ) as fi
Where fi.Row_Number between 11 and 20;
-- other way
select * from film order by rental_rate offset 10 fetch first 10 row only;

--12. Write a query which will join the data in the customer table and the payment table.
-- You want to get the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
select payment.customer_id,amount, payment_date from payment inner join customer on payment.customer_id = customer.customer_id order by payment.customer_id;

-- 13.You need to check your inventory. Write a query to get all the movies which are not in inventory.
select * from film where film_id not in (select film_id from inventory);

--14.Write a query to find which city is in which country.
select city.city , country.country from city inner join country on country.country_id = city.country_id;

-- Write a query to get the customer’s id, names (first and last),
-- the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
select staff.staff_id, customer.customer_id, customer.first_name, customer.last_name, amount, payment_date from customer
inner join payment on customer.customer_id = payment.customer_id
inner join staff on  staff.staff_id =payment.staff_id
order by staff_id;




