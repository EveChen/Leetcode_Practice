
# Link: https://leetcode.com/problems/not-boring-movies/

# Write your MySQL query statement below
SELECT id, movie, description, rating
FROM Cinema
WHERE MOD(id, 2) = 1 AND description NOT LIKE "%boring%"
ORDER BY rating DESC


