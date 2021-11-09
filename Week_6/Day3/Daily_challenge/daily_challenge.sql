-- -- -- -- Create 2 tables : Customer and Customer profile. They have a One to One relationship. Use all the types of Joins to display the data.

-- CREATE TABLE customer (
--    customer_id SERIAL primary key,
--    first_name VARCHAR(45) NOT NULL,
--    last_name VARCHAR(45) NOT NULL
--  );

--  insert into customer (first_name,last_name)
--  values ('Lea','Johnson'), ('Michael', 'Mons') , ('Toby', 'Been'), ('Sarah', 'Zalsman'), ('Max','Buzz')

--  CREATE TABLE customer_profile (
--     c_profile_id INTEGER NOT NULL primary key,
--     email VARCHAR(255) NOT NULL,
--     CONSTRAINT cust_profile_id FOREIGN KEY (c_profile_id) REFERENCES customer (customer_id) on update cascade
--   );

--  insert into customer_profile(c_profile_id,email)
--  values ((SELECT customer_id FROM customer where first_name = 'Lea' and last_name = 'Johnson'), 'lea.johnson@gmail.com'),
--  ((SELECT customer_id FROM customer where first_name = 'Michael' and last_name = 'Mons'),'michael.mons@gmail.com'),
--  ((SELECT customer_id FROM customer where first_name = 'Sarah' and last_name = 'Zalsman'),'sarah.zalsman@gmail.com')

select first_name, last_name, email from customer inner join customer_profile on customer.customer_id = customer_profile.c_profile_id;
select first_name, last_name, email from customer left outer join customer_profile on customer.customer_id = customer_profile.c_profile_id;
select first_name, last_name, email from customer right outer join customer_profile on customer.customer_id = customer_profile.c_profile_id;
select first_name, last_name, email from customer full join customer_profile on customer.customer_id = customer_profile.c_profile_id;



-- -- -- -- Create 2 other tables : Product and Order. Order is a table with a Many to Many relationship with the Customer and Product tables.

-- create table product (
-- product_id serial primary key,
-- name varchar(255) not null,
-- price smallint not null);

-- insert into product (name,price)
-- values ('table',500), ('chair',150), ('desk',700), ('bed', 1000)

-- CREATE TABLE orders (
--   customer_id INTEGER NOT NULL,
--   product_id INTEGER NOT NULL,
--   PRIMARY KEY (customer_id, product_id),
--   FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON UPDATE CASCADE,
--   FOREIGN KEY (product_id) REFERENCES product(product_id) ON UPDATE CASCADE
-- );

-- insert into orders(customer_id, product_id)
-- values ((SELECT customer_id FROM customer where first_name = 'Lea' and last_name = 'Johnson'),
-- 		(SELECT product_id FROM product where name='bed')),
-- 		((SELECT customer_id FROM customer where first_name = 'Lea' and last_name = 'Johnson'),
-- 		(SELECT product_id FROM product where name='desk')),
-- 		((SELECT customer_id FROM customer where first_name = 'Sarah'),
-- 		(SELECT product_id FROM product where name='bed')),
-- 		((SELECT customer_id FROM customer where first_name = 'Toby'),
-- 		(SELECT product_id FROM product where name='chair')),
-- 		((SELECT customer_id FROM customer where first_name = 'Toby'),
-- 		(SELECT product_id FROM product where name='table')),
-- 		((SELECT customer_id FROM customer where first_name = 'Michael'),
-- 		(SELECT product_id FROM product where name='chair'))

select * from orders inner join product on orders.product_id = product.product_id inner join customer on customer.customer_id = orders.customer_id;
select * from orders inner join product on orders.product_id = product.product_id left join customer on customer.customer_id = orders.customer_id;
select * from orders inner join product on orders.product_id = product.product_id right join customer on customer.customer_id = orders.customer_id;
select * from orders inner join product on orders.product_id = product.product_id full join customer on customer.customer_id = orders.customer_id;


select * from orders left outer join product on orders.product_id = product.product_id inner join customer on customer.customer_id = orders.customer_id;
select * from orders left outer join product on orders.product_id = product.product_id left outer join customer on customer.customer_id = orders.customer_id;
select * from orders left outer join product on orders.product_id = product.product_id right join customer on customer.customer_id = orders.customer_id; 
select * from orders left outer join product on orders.product_id = product.product_id full join customer on customer.customer_id = orders.customer_id; 


select * from orders right join product on orders.product_id = product.product_id inner join customer on customer.customer_id = orders.customer_id;
select * from orders right join product on orders.product_id = product.product_id left join customer on customer.customer_id = orders.customer_id;
select * from orders right join product on orders.product_id = product.product_id right join customer on customer.customer_id = orders.customer_id;
select * from orders right join product on orders.product_id = product.product_id full join customer on customer.customer_id = orders.customer_id; 


select * from orders full join product on orders.product_id = product.product_id inner join customer on customer.customer_id = orders.customer_id;
select * from orders full join product on orders.product_id = product.product_id left join customer on customer.customer_id = orders.customer_id;
select * from orders full join product on orders.product_id = product.product_id right join customer on customer.customer_id = orders.customer_id;
select * from orders full join product on orders.product_id = product.product_id full join customer on customer.customer_id = orders.customer_id; 

















