
# Link: https://leetcode.com/problems/big-countries/

# Solution A: use where
# SELECT name, population, area
# FROM World
# WHERE area > 3000000 OR population > 25000000

# Solution B: use union
SELECT name, population, area
FROM World
WHERE area > 3000000

UNION

SELECT name, population, area
FROM World
WHERE population > 25000000
