
# Solution A
SELECT d.Name AS Department, e.Name AS Employee, e.Salary AS Salary
FROM Employee e
    JOIN Department d
    ON e.DepartmentId = d.Id
WHERE (e.DepartmentId, e.Salary) 
    IN (SELECT e2.DepartmentId, MAX(e2.Salary) AS Salary
       FROM Employee e2
       GROUP BY e2.DepartmentId)


# 另種方法 (同套題的解法) - 還不清楚邏輯
# SELECT d.Name AS Department, e.Name AS Employee, e.Salary AS Salary
# FROM Employee e
#     JOIN Department d
#     ON e.DepartmentId = d.Id
# WHERE 1 > (SELECT COUNT(DISTINCT e2.Salary)
#           FROM Employee e2
#           WHERE e2.Salary > e.Salary
#           AND e2.DepartmentId = e.DepartmentId)

# Window Functio
# SELECT d.Name AS Department, tmp.Name AS Employee, tmp.Salary
# FROM Department d
#     JOIN
#         (SELECT *, RANK() OVER(PARTITION BY DepartmentId ORDER BY Salary DESC) AS rank_num
#         FROM Employee) AS tmp
#         ON d.Id = tmp.DepartmentId
# WHERE rank_num = 1
