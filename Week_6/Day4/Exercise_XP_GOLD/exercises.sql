-- -- -- -- Update Statement -- -- -- -- 

-- Write a SQL statement to change the following details belonging all employes who’s department_id is 110:
update employees
set email = 'not available'
where department_id = 11;

-- Write a SQL statement which will change the email column of all employees to ‘available’ whom work in the ‘Accounting’ department.
update employees
set email='available'
where department_id = (select department_id from departments where department_name = 'Accounting');

-- Write a SQL statement to change the salary of the employee whose ID is 105. If the existing salary is less than 5000, change it to 8000.
update employees
set salary = 8000
where employee_id = 105 and salary<5000;



-- -- -- -- Aggregate Functions -- -- -- --

-- Write a query to find the number of jobs available in the employees table.
select count(job_id) from employees;

-- Write a query to get the number of employees working in each post.
select job_title, count(employees.job_id) from employees
inner join jobs on jobs.job_id = employees.job_id group by job_title;

-- Write a query to get the difference between the highest and lowest salaries.
select (max(salary)-min(salary)) as gap_salary  from employees;

-- Write a query to find a manager ID and the salary of the lowest-paid employee under that manager.
select manager_id, min(salary) from employees where not manager_id is null group by manager_id;

-- Write a query to get the average salary for each post excluding programmer.
select job_title, avg(salary) from employees
inner join jobs on jobs.job_id = employees.job_id 
where job_title != 'Programmer'
group by job_title;

-- Write a query to get the average salary for all departments that employ more than 10 employees.
select department_name , count(employees.department_id), avg(salary) from employees 
inner join departments on departments.department_id = employees.department_id
group by department_name
having count(employees.department_id)>10;



-- -- -- -- Alter Table Statement -- -- -- --

-- Write a SQL statement to change the name of the column “state_province” to “state” in the locations table, keeping the same data type and size.
alter table locations rename column state_province to state;

-- Write a SQL statement to add a primary key to the “location_id” column in the locations table.
ALTER TABLE locations ADD PRIMARY KEY (location_id);


-- -- -- -- Create Tables -- -- -- --

-- Write a SQL statement to create a simple table “new_countries” including columns country_id and country_name.

create table new_countries (
id serial primary key,
country_id varchar(3) unique references countries(country_id) on delete restrict,
country_name varchar(50) unique);

insert into new_countries (country_id, country_name)
values ((select country_id from countries where country_name = 'Italy'), 'Italy'),
((select country_id from countries where country_name = 'India'), 'India'),
((select country_id from countries where country_name = 'China'), 'China');

-- Write a SQL statement to create a duplicate copy of the “new_countries” table including the structure and the data of the “new_countries” table.
create table dup_new_countries as (select * from new_countries);

-- Write a SQL statement to create a table named “new_jobs” including columns job_id, job_title, min_salary, max_salary

create table new_jobs (
job_id serial not null primary key ,
job_title varchar(40) not null default ' ' ,
min_salary decimal(6,0) default 8000,
max_salary decimal(6,0) default NULL,
CONSTRAINT check_max_salary CHECK (max_salary < 25000))

-- Write an SQL statement to create a table called “new_employees” the table should include the following columns: employee_id, first_name, last_name, email, phone_number hire_date, job_id and salary.

create table new_employees ( 
employee_id serial NOT NULL primary key, 
first_name varchar(20) DEFAULT NULL, 
last_name varchar(25) NOT NULL, 
email varchar(40) NOT NULL,
phone_number bigint not null,
hire_date date not null,
job_id INTEGER NOT NULL,
salary decimal(8,2) DEFAULT NULL, 
FOREIGN KEY(job_id) 
references new_jobs(job_id) 
ON DELETE CASCADE on update restrict
);

-- Write a SQL statement to create a table called “new_job_history” the table should include the following columns: employee_id, start_date, end_date, job_id

create table new_job_history(
employee_id integer not null,
foreign key (employee_id) references new_employees(employee_id) on delete restrict on update cascade,
start_date date not null,
end_date date ,
job_id integer not null,
foreign key (job_id) references new_jobs(job_id) ON DELETE restrict on update restrict);


-- -- -- -- Insert -- -- -- --

-- Write a SQL statement to insert a record with your own value into the “new_countries” table.
insert into new_countries (country_id, country_name)
values ((select country_id from countries where country_name = 'France'), 'France');

-- Using only one insert statement insert 3 row of data to the “new_countries” table
insert into new_countries (country_id, country_name)
values ((select country_id from countries where country_name = 'Brazil'), 'Brazil'),
((select country_id from countries where country_name = 'Egypt'), 'Egypt'),
((select country_id from countries where country_name = 'Israel'), 'Israel')

-- Write a SQL statement to insert the rows whithin the “new_countries” table to a duplicate table.

-- insert into dup_new_countries (country_id, country_name)
select country_id, country_name
from new_countries
where id > 3;

