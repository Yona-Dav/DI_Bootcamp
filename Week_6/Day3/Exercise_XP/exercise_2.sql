-- -- -- -- Exercise 2 : DVD Rental -- -- -- --

-- 1. Use UPDATE to change the language of some films. Make sure that you use valid languages.
update film
set language_id = 2
where film_id between 20 and 50;

-- 2. Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- foreign keys : store_id, address_id
-- it depends on update possibilities (district,cascade,no action,set null, set default)

-- 3. We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
drop table if exists customer_review;

-- 4. Find out how many rentals are still outstanding (ie. have not been returned to the store yet). ---> 183
select count(*) from rental where return_date is NULL;

-- 5. Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
select film.title, film.rental_rate
from (film join inventory on film.film_id = inventory.film_id)
join rental on rental.inventory_id = inventory.inventory_id
where rental.return_date is NULL
order by rental_rate desc
limit 30;

-- 6. Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe. --> park citizen
select film.title
from (film join film_actor on film.film_id = film_actor.film_id)
join actor on actor.actor_id = film_actor.actor_id
where actor.first_name = 'Penelope' and actor.last_name = 'Monroe' and description ilike '%wrestler%';

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”. --> Cupboard Sinners
select film.title 
from (film join film_category on film.film_id = film_category.film_id)
join category on category.category_id = film_category.category_id
where category.name = 'Documentary' and length <60 and rating='R';


-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.

select film.title
from (film join inventory on film.film_id = inventory.film_id join customer on customer.store_id = inventory.store_id)
join rental on rental.inventory_id = inventory.inventory_id
where customer.first_name= 'Matthew' and customer.last_name='Mahan' and rental_rate>4.00 and return_date between '2005-07-28' and '2005-08-01';



-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
select film.title
from (film join inventory on film.film_id = inventory.film_id join customer on customer.store_id = inventory.store_id)
join rental on rental.inventory_id = inventory.inventory_id
where customer.first_name= 'Matthew' and customer.last_name='Mahan' and rental_rate>4.00 and description ilike '%boat%' or title ilike '%boat%';



