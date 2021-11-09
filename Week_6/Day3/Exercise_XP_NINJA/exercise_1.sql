-- -- -- -- Exercise 1 : DVD Rentals -- -- -- --

-- Retrieve all films with a rating of G or PG, which are are not currently rented (they have been returned/have never been borrowed).

select distinct film.film_id, title , return_date, rating
from film , inventory, rental
where inventory.film_id = film.film_id and inventory.inventory_id = rental.inventory_id and return_date is Null and rating in ('G','PG');

-- Create a new table which will represent a waiting list for children’s movies.
-- This will allow a child to add their name to the list until the DVD is available (has been returned).

-- Create table waiting_list_child (
-- child_id serial primary key,
-- first_name varchar(255),
-- last_name varchar(255),
-- film_id integer,
-- Foreign key (film_id) references film(film_id))

-- insert into waiting_list_child (first_name, last_name, film_id)
-- values ('Lea', 'Assous', 13),
-- ('Tom', 'Guez', 22),
-- ('Sigal', 'Levi', 216),
-- ('Sarah', 'Mizrahi', 13),
-- ('David', 'Sanz', 178)

-- Retrieve the number of people waiting for each children’s DVD. Test this by adding rows to the table that you created in question 2 above.

select film_id, count(film_id) from waiting_list_child group by film_id;


