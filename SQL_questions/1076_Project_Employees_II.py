
# https://leetcode.com/problems/project-employees-ii/

# Wrong: 只會顯示 limit 1，但如果有許多 project_id 有相同的 maximum 員工人數?
# SELECT project_id
# FROM 
#     (Select project_id, Count(p.employee_id) AS cnt
#     FROM Project p
#         JOIN Employee e
#         ON p.employee_id = e.employee_id
#     GROUP BY project_id
#     ORDER BY Count(p.employee_id) Desc
#     LIMIT 1) AS tmp


# Solution A: 記得為什麼要用 Group by
SELECT project_id
FROM Project p
GROUP BY project_id
HAVING COUNT(employee_id) =
    (SELECT Count(employee_id)
    From Project p
    Group By project_id
    Order By Count(employee_id) Desc
    Limit 1)


