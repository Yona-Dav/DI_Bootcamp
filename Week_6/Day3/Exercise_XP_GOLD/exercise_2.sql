-- -- -- -- Exercise 2 – Happy Halloween -- -- -- --

-- 1. How many stores there are, and in which city and country they are located.

-- create view stores as
-- select store_id, city.city, country.country
-- from city, address, country, store
-- where store.address_id = address.address_id and address.city_id = city.city_id and city.country_id = country.country_id;

select count(*) from stores;
select city, country, count(store_id) from stores group by (city, country);

-- 2. How many hours of viewing time there are in total in each store – in other words, the sum of the length of every inventory item in each store.
select store_id, sum(length)/60 as sum_length
from inventory
inner join film on film.film_id = inventory.film_id
group by store_id;

-- 3. Make sure to exclude any inventory items which are not yet returned. (Yes, even in the time of zombies there are people who do not return their DVDs)

-- create view film_returned2 as 
-- select distinct film.film_id, store_id,length
-- from film , inventory, rental
-- where inventory.film_id = film.film_id and inventory.inventory_id = rental.inventory_id and return_date is not Null;

select store_id, sum(length)/60 as sum_length
from film_returned2
group by store_id;

-- 4. A list of all customers in the cities where the stores are located.
select first_name, last_name, address.city_id
from customer inner join address on customer.address_id = address.address_id
where address.city_id in (select address.city_id from store join address on store.address_id = address.address_id);

-- 5. A list of all customers in the countries where the stores are located.
select first_name, last_name, country_id
from customer inner join address on customer.address_id = address.address_id inner join city on  city.city_id = address.city_id
where country_id in (select country_id from city where city_id in (select address.city_id from store join address on store.address_id = address.address_id));


-- 6. Some people will be frightened by watching scary movies while zombies walk the streets.
-- Create a ‘safe list’ of all movies which do not include the ‘Horror’ category, or contain the words ‘beast’, ‘monster’, ‘ghost’, ‘dead’, ‘zombie’, or ‘undead’ in their titles or descriptions…
-- Get the sum of their viewing time (length).
-- Hint : use the CHECK contraint
select title, description, length from film_category
join film on film.film_id = film_category.film_id
where not category_id in (select category_id from category where name='Horror') or title ilike '%beast%' 
or title ilike '%monster%' or title ilike '%ghost%' or title ilike '%dead%' or title ilike '%zombie%' or title ilike '%undead%' 
or description ilike '%beast%' or description ilike '%monster%' or description ilike '%ghost%' or description ilike '%dead%' or description ilike '%zombie%' or description ilike '%undead%' ;


select sum(length) from film_category
join film on film.film_id = film_category.film_id
where not category_id in (select category_id from category where name='Horror') or title ilike '%beast%' 
or title ilike '%monster%' or title ilike '%ghost%' or title ilike '%dead%' or title ilike '%zombie%' or title ilike '%undead%' 
or description ilike '%beast%' or description ilike '%monster%' or description ilike '%ghost%' or description ilike '%dead%' or description ilike '%zombie%' or description ilike '%undead%' ;


-- 7. For both the ‘general’ and the ‘safe’ lists above, also calculate the time in hours and days (not just minutes).

--Time in days for general--
-- select store_id, sum(length)/60/24 as sum_length
-- from film_returned2
-- group by store_id

--Time in hours for safe --
-- select sum(length)/60 as sum_length from film_category
-- join film on film.film_id = film_category.film_id
-- where not category_id in (select category_id from category where name='Horror') or title ilike '%beast%' 
-- or title ilike '%monster%' or title ilike '%ghost%' or title ilike '%dead%' or title ilike '%zombie%' or title ilike '%undead%' 
-- or description ilike '%beast%' or description ilike '%monster%' or description ilike '%ghost%' or description ilike '%dead%' or description ilike '%zombie%' or description ilike '%undead%' ;

--Time in days for safe --
-- select sum(length)/60/24 as sum_length from film_category
-- join film on film.film_id = film_category.film_id
-- where not category_id in (select category_id from category where name='Horror') or title ilike '%beast%' 
-- or title ilike '%monster%' or title ilike '%ghost%' or title ilike '%dead%' or title ilike '%zombie%' or title ilike '%undead%' 
-- or description ilike '%beast%' or description ilike '%monster%' or description ilike '%ghost%' or description ilike '%dead%' or description ilike '%zombie%' or description ilike '%undead%' ;



