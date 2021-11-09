-- -- -- Exercise 1: DVD Rental -- -- -- 

--1. Get a list of all film languages.
select distinct name from language;

-- 2. Get a list of all films joined with their languages – select the following details : film title, description, and language name. 
select title, description, name from film inner join language on film.language_id = language.language_id;
-- Get all films, even if they don’t have languages.
select title, description, name from film left outer join language on film.language_id = language.language_id;
-- Get all languages, even if there are no films in those languages.
select title, description, name from film right outer join language on film.language_id = language.language_id;

--3. Create a new table called new_film with the following columns : id, name. Add some new films to the table.
create table new_film (
id serial primary key,
name varchar(255));

insert into new_film(name) values ('Titanic'),('Avatar'),('Forest Gump'),('The Matrix');

-- 4. Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, it’s review should be automatically deleted.

create table customer_review (
review_id serial primary key NOT NULL,
film_id INTEGER REFERENCES new_film (id) ON DELETE CASCADE,
language_id INTEGER REFERENCES language (language_id) ON DELETE CASCADE,
title varchar(50),
score smallint,
review_text text,
last_update date
)


-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
 insert into customer_review (film_id,language_id,title, score, review_text, last_update)
 values ((select id from new_film where name = 'Titanic'), (select language_id from language where name='English'),'Titanic', 9,
 'Titanic is a 1997 American epic romance and disaster film directed, written, produced, and co-edited by James Cameron. Incorporating both historical and fictionalized aspects, it is based on accounts of the sinking of the RMS Titanic,
 and stars Leonardo DiCaprio and Kate Winslet as members of different social classes who fall in love aboard the ship during its ill-fated maiden voyage.','1997-01-01'),
 ((select id from new_film where name = 'Avatar'),(select language_id from language where name='English'), 'Avatar', 8,
 'In 2154, humans have depleted Earths natural resources, leading to a severe energy crisis. The Resources Development Administration (RDA) mines a valuable mineral unobtanium on Pandora, a densely forested habitable moon orbiting Polyphemus, a fictional gas giant in the Alpha Centauri star system.
  Pandora, whose atmosphere is poisonous to humans, is inhabited by the Navi, a species of 10-foot tall (3.0 m), blue-skinned, sapient humanoids[37] that live in harmony with nature and worship a mother goddess named Eywa.', '2009-03-12')

-- Delete a film that has a review from the new_film table, what happens to the customer_review table? also removed from the customer review
delete from new_film where name = 'Titanic';
select * from customer_review




