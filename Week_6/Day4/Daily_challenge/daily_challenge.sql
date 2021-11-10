-- Create a table called orders and a table called items. You decide which fields should be in each table, although make sure the items table has a column called price.
create table items(
item_id serial primary key,
name varchar(50),
price int);

insert into items(name,price)
values('none',0),('table',800), ('chair',300), ('desk', 500), ('televison', 1000), ('camera', 400), ('glass', 10);

create table orders (
order_id serial primary key,
item1 integer not null,
foreign key (item1) references items(item_id) on delete restrict,
item2 integer default 1,
foreign key (item2) references items(item_id) on delete restrict,
item3 integer default 1,
foreign key (item3) references items(item_id) on delete restrict);

insert into orders(item1)
values (1);
insert into orders(item1,item2,item3)
values((select item_id from items where name = 'table'),(select item_id from items where name = 'glass'),(select item_id from items where name = 'desk')),
((select item_id from items where name = 'chair'),(select item_id from items where name = 'table'),(select item_id from items where name = 'camera'));
insert into orders(item1,item2)
values((select item_id from items where name = 'table'),(select item_id from items where name = 'desk'));


-- Create a function that returns the total price for a given order.

create function total_price_order(ord int) returns int as $total_price$
declare
	price1 int;
	price2 int;
	price3 int;
begin
	price1 = (select price from items join orders on orders.item1 = items.item_id where order_id = ord);
	price2 = (select price from items join orders on orders.item2 = items.item_id where order_id = ord);
	price3 = (select price from items join orders on orders.item3 = items.item_id where order_id = ord);
	return price1+price2+price3;
end;
$total_price$ LANGUAGE plpgsql;

select * from total_price_order(2);


-- -- -- -- Bonus : -- -- -- --


create table users(
user_id serial primary key,
first_name varchar(50) not null,
last_name varchar(50) not null,
order1 integer,
foreign key (order1) references orders(order_id),
order2 integer default 1,
foreign key (order2) references orders(order_id));

insert into users(first_name, last_name, order1,order2) values ('Lea','Guez',2,3);
insert into users(first_name, last_name, order1) values ('Tom','Sanz', 4);


-- Create a function that returns the total price for a given order of a given user.

create function total_price_user_order(use int , ord int) returns int as $total_price$
declare
	price1 int;
	price2 int;
	price3 int;
begin
	if ord = 1 then 
		price1 = (select price from items join orders on orders.item1 = items.item_id join users on orders.order_id = users.order1
				  where order_id = (select order1 from users where user_id=use));
		price2 = (select price from items join orders on orders.item2 = items.item_id join users on orders.order_id = users.order1
				  where order_id = (select order1 from users where user_id=use));
		price3 = (select price from items join orders on orders.item3 = items.item_id join users on orders.order_id = users.order1
				  where order_id = (select order1 from users where user_id=use));
		return price1+price2+price3;
	elsif ord = 2 then
		price1 = (select price from items join orders on orders.item1 = items.item_id join users on orders.order_id = users.order2
				  where order_id = (select order2 from users where user_id=use));
		price2 = (select price from items join orders on orders.item2 = items.item_id join users on orders.order_id = users.order2
				  where order_id = (select order2 from users where user_id=use));
		price3 = (select price from items join orders on orders.item3 = items.item_id join users on orders.order_id = users.order2
				  where order_id = (select order2 from users where user_id=use));
		return price1+price2+price3;
	end if;

end;
$total_price$ LANGUAGE plpgsql;

select * from total_price_user_order(2,1)








