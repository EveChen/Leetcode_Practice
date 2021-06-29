
# Link: https://leetcode.com/problems/triangle-judgement/

# Solution A: use case when
# SELECT *, CASE 
#         WHEN x + y > z and y + z > x and x + z > y THEN 'Yes'
#         ELSE 'No'
#         END AS triangle
# FROM triangle

# Solution B: use if
SELECT *, IF(x + y > z and y + z > x and z + x > y, 'Yes', 'No') AS triangle
FROM triangle
