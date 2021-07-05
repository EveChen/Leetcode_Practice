
# Link: https://leetcode.com/problems/classes-more-than-5-students/

# Solution A: Group by + having
# SELECT class
# FROM courses
# GROUP BY class
# HAVING count(distinct student) >= 5

# Solution B: subquery
SELECT class
FROM (SELECT class, COUNT(DISTINCT student) AS num
     FROM courses
     GROUP BY class) AS tmp
WHERE num >= 5

