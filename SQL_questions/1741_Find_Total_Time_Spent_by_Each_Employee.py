
# Link: https://leetcode.com/problems/find-total-time-spent-by-each-employee/

# Solution A: subquery
# SELECT event_day AS day, emp_id, total_time
# FROM (SELECT *, SUM(out_time - in_time) AS total_time
#       FROM Employees
#       GROUP BY emp_id, event_day
#         ) AS tmp
# ORDER BY day ASC

# Solution B: without using subquery
# SELECT event_day AS day, emp_id, SUM(out_time - in_time) AS total_time
# FROM Employees
# GROUP BY day, emp_id

# Same solution but slower
SELECT event_day AS day, emp_id, SUM(out_time) - SUM(in_time) AS total_time
FROM Employees
GROUP BY 1, 2
