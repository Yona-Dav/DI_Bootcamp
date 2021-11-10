-- -- -- -- Subqueries -- -- -- --

-- Write a query to find the first_name, last_name and salaries of the employees who have a higher salary than the employee whose last_name is Bull.
select first_name, last_name, salary from employees
where salary > (select salary from employees where last_name = 'Bell');

-- Write a SQL subquery to find the first_name and last_name of the employees under a manager who works for a department based in the United States.

select first_name, last_name, employees.department_id, country_name
from departments, locations, countries, employees
where locations.location_id = departments.location_id and countries.country_id = locations.country_id
and employees.department_id = departments.department_id and country_name ilike '%United States%' and manager_id is not null;

-- Write a SQL subquery to find the first_name and last_name of the employees who are working as managers.
select first_name, last_name from employees where employee_id in (select distinct manager_id from employees);

-- Write a SQL subquery to find the employee(s) first_name and last_name, which salary is greater than the average salary of the employees.
select first_name, last_name, salary from employees where salary>(select avg(salary) from employees);

-- Write a SQL subquery to find the employee(s) first_name and last_name, which salary is equal to the minimum salary of their job position.
select first_name, last_name, salary , job_id
from employees where employees.salary = (select min_salary from jobs where employees.job_id = jobs.job_id);

-- Write a query to find the names (first_name, last_name) of the employees who are not supervisors.
select first_name, last_name from employees where not employee_id in (select distinct manager_id from employees WHERE manager_id IS NOT NULL);

-- Write a SQL subquery to find the employee(s) ID, first name, last name and salary of all employees whose salary is above the average salary for their departments.
Select first_name, last_name, salary, e.department_id  
From employees e
Where e.salary > ( Select avg(s.salary) From employees s
Where e.department_id = s.department_id
Group By s.department_id);

-- Write a subquery to find the 5th maximum salary of all salaries.
select first_name, last_name, salary from employees order by salary desc offset 4 limit 1;

-- Write a subquery to find the 4th minimum salary of all the salaries.
select first_name, last_name, salary from employees order by salary asc offset 3 limit 1;

-- Write a query to list the department name and number, of all the departments in which there are no employees.
select distinct employees.department_id, department_name from employees full join departments on employees.department_id = departments.department_id
where not departments.department_id in (select employees.department_id from employees);


-- -- -- -- Joins -- -- -- --

-- Write a query to find the addresses (location_id, street_address, city, state_province, country_name) of all the departments.
select department_id, departments.location_id, street_address, city, state, country_name
from departments, countries, locations
where departments.location_id = locations.location_id and countries.country_id = locations.country_id;

-- Write a query to make a join with the employees and departments table to find the name of the employee, including first_name and last name, department ID and name of departments.
select first_name, last_name, employees.department_id, department_name
from employees, departments
where employees.department_id = departments.department_id;

-- Write a SQL query to make a join with three tables: employees, departments and locations to find the name,
-- including first_name and last_name, jobs, department name and ID, of the employees working in London.
select first_name, last_name, employees.job_id , job_title, department_name, employees.department_id, city
from employees, jobs, departments, locations
where employees.department_id = departments.department_id and jobs.job_id = employees.job_id and departments.location_id = locations.location_id and city = 'London';

-- Write a query to make a join with two tables to find the employee id, last_name as Employee along with their manager_id and last name as Manager.
select e.employee_id, e.last_name as employee_name,
s.employee_id, s.last_name as manager_name
from employees e , employees s
where e.manager_id= s.employee_id;

-- Write a query to make a join with two tables employees and departments,
-- to get the employees working in each department (retrieve the employees details, and the department name and number).
select first_name, last_name, employees.department_id , department_name
from employees, departments
where employees.department_id = departments.department_id
order by department_id asc;

-- Write a query to make a join to find the employees who worked in a department which ID is 90 
-- (retrieve the employee ID, job title ).
select employee_id, job_title 
from employees, jobs
where jobs.job_id = employees.job_id and department_id = 9;

-- Write a query to make a join with two tables, employees and jobs to display the job title and average salary of the employees.
select job_title, avg(salary)
from employees , jobs
where jobs.job_id = employees.job_id
group by job_title;

-- Write a query to make a join with two tables, employees and departments to display department name, first_name and last_name,
-- hire date and salary for all the managers who achieved a working experience of more than 15 years.
select distinct department_name, w2.first_name, w2.last_name, w2.hire_date, w2.salary,date_part('year',age(now(),w2.hire_date)) Experience 
from departments , employees w2 , employees w1
where w1.manager_id = w2.employee_id and w2.department_id = departments.department_id and date_part('year',age(now(),w2.hire_date))>15;



-- -- -- -- String Function -- -- -- --

-- Write a query to update phone_number records. If the the substring ‘124’ was found in that column, update the phone_number to ‘999’.
update employees 
set phone_number = replace(phone_number, '124', '999') 
where phone_number like '%124%';

-- Write a query to find the details of the employees who contain eight or more characters in their first name.
select * from employees
where length(first_name)>7;

-- Write a query to join in uppercase, the first letter of the first_name, with the last_name, with '@example.com‘ in the email column.
update employees 
set email = CONCAT(upper(left(first_name,1)), upper(last_name), '@example.com');

-- Write a query to get the employee id, email but discard the last three characters of the email.
update employees set email=left(email, length(email)-3)
returning employee_id, email;

-- Write a query to display the first word in the job title, if the job title contains more than one words.
select job_title, SUBSTR(job_title,1, position(' ' IN job_title))from jobs;

-- Write a query that displays the first name and the length of the first name for all employees whose name starts with the letters ‘A’, ‘J’ or ‘M’.
-- Give each column an appropriate label. Sort the results by the employees’ first names.
select first_name as name, length(first_name) as length_name from employees
where first_name ilike 'A%' or first_name ilike 'J%' or first_name ilike 'M%' order by first_name asc;

-- Write a query to display the first name and salary for all employees. Display the salary with the $ symbol. Label the column as SALARY.
select first_name, concat(salary, '$') as "SALARY" from employees
