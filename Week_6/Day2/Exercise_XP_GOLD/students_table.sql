-- -- -- Exercise 2: Students Table -- -- --


-- -- Update -- --
-- 1.‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
update students
set birth_date = '1998-11-02'
where first_name = 'Lea';

-- 2. Change the last_name of David from ‘Grez’ to ‘Guez’.
update students
set last_name = 'Guez'
where last_name = 'Grez';


-- -- Delete -- --
-- 1. Delete the student named ‘Lea Benichou’ from the table.
delete from students
where first_name = 'Lea' and last_name = 'Benichou';


-- -- Count -- --
-- 1. Count how many students are in the table.
select count(*) from students;

-- 2. Count how many students were born after 1/01/2000.
select count(*) from students where birth_date = '2000-01-01';



-- -- Insert / Alter -- --
-- 1. Add a column to the student table called math_grade.
-- alter table students add column math_grade smallint;

-- 2.Add 80 to the student which id is 1.
update students set math_grade = 80 where student_id = 1;

-- 3. Add 90 to the students which have ids of 2 or 4.
update students set math_grade = 90 where student_id = 2 or student_id = 4;

-- 4. Add 40 to the student which id is 6.
update students set math_grade = 40 where student_id = 6;

-- 5. Count how many students have a grade bigger than 83
select count(*) from students where math_grade>83;

-- 6.Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
insert into students(first_name,last_name,birth_date,math_grade) values ('Omer', 'Simpson','1980-10-03',70);
select * from students;

-- Bonus: Count how many grades each student has.
-- Tip: You should display the first_name, last_name and the number of grades of each student. If you followed the instructions above correctly, all the students should have 1 math grade, except Omer Simpson which has 2.
-- Tip : Use an alias called total_grade to fetch the grades.
-- Hint : Use GROUP BY.
select first_name, last_name, count(math_grade) as total_grade from students group by (first_name,last_name);


-- -- SUM -- --
-- 1. Find the sum of all the students grades.
select sum(math_grade) from students
