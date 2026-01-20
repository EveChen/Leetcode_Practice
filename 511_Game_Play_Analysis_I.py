
# Method 1: window function
-- Select player_id, event_date As first_login
-- From (
--     Select *, 
--         Row_number() Over (Partition By player_id Order By event_date) As rn
--     From Activity
--         ) As tmp
-- Where rn = 1

# Method 2: built-in function 把資料按「球員 ID」分組，然後選出每一組裡「最早的日期」
Select player_id, Min(event_date) As first_login
From Activity
Group By player_id
