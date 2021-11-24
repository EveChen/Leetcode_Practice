
# https://leetcode.com/problems/project-employees-i/

# Solution A
# SELECT project_id, ROUND(SUM(experience_years)/COUNT(p.employee_id), 2) AS average_years
# FROM Project p
#     JOIN Employee e
#     ON p.employee_id = e.employee_id
# GROUP BY project_id


# Solution B
SELECT project_id, ROUND(AVG(experience_years), 2) AS average_years
FROM Project p
    JOIN Employee e
    ON p.employee_id = e.employee_id
GROUP BY project_id
