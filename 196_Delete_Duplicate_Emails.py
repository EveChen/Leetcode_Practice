
# Link: https://leetcode.com/problems/delete-duplicate-emails/

-- # Method 1: Self join
-- Delete p1
--     From Person p1, Person p2
-- Where p1.email = p2.email And p1.id > p2.id

# Method 1.2: Self join another way
Delete p1
From Person p1
Join Person p2 On p1.email = p2.email
Where p1.id > p2.id


-- # Method 2: subquery
-- Delete From Person
-- Where id Not In (
--     Select tmp.min_id 
--     From (
--         Select Min(id) As min_id
--         From Person
--         Group By email
--     ) As tmp
-- ) 


-- # Method 2.2: Use windows function (note: can't use the name "rank" because that's a function's name)
-- Delete From Person
-- Where id In (
--     Select id 
--     From (
--         Select id, Row_Number() Over (Partition By email Order By id) As rn
--         From Person
--     ) As tmp
--     Where rn > 1
-- )



-- -- # Other way: If we don't need to delete
-- -- With tmp As (
-- --     Select id, email, ROW_NUMBER() Over (Partition By email Order By id Asc) As rank
-- --     From Person
-- -- )

-- -- Select id, email
-- -- From tmp
-- -- Where rank = 1


-- If we don't need to delete
# select email,min(id) from Person group by email
