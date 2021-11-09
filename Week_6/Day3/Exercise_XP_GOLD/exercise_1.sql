-- -- -- -- Exercise 1 : DVD Rentals -- -- -- -- 

-- Get a list of all rentals which are out (have not been returned). How do we identify these films in the database?
select film.title
from (film join inventory on film.film_id = inventory.film_id)
join rental on rental.inventory_id = inventory.inventory_id
where return_date is null;

-- Get a list of all customers who have not returned their rentals. Make sure to group your results.
select distinct first_name ||' '|| last_name as fullname, return_date
from customer
inner join rental 
on customer.customer_id = rental.customer_id
where return_date is null;


-- Get a list of all the Action films with Joe Swank.
select film.title 
from (film join film_category on film.film_id = film_category.film_id)
join category on category.category_id = film_category.category_id
join film_actor on film.film_id = film_actor.film_id
join actor on actor.actor_id = film_actor.actor_id
where category.name = 'Action' and first_name = 'Joe' and last_name = 'Swank';

-- Before you start, could there be a shortcut to getting this information? Maybe a view?
-- CREATE VIEW films1 AS
-- SELECT film.title, first_name, last_name, category.name
-- FROM film, category,actor, film_category,film_actor
-- WHERE film.film_id = film_category.film_id and  category.category_id = film_category.category_id and film.film_id = film_actor.film_id and actor.actor_id = film_actor.actor_id ;

SELECT *
FROM films1
where name = 'Action' and first_name = 'Joe' and last_name = 'Swank';

