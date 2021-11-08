-- -- -- -- Questions -- -- -- --

SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );
-- output : 0

SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );
-- output : 2 (id = 6 and id = 7)

SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab );
-- output : 0

SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );
-- output : 2 (id = 6 and id = 7)
