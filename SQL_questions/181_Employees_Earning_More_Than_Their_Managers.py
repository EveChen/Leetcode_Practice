
# Link: https://leetcode.com/problems/employees-earning-more-than-their-managers/

# Solution A: Use "Join"
# Write your MySQL query statement below
# SELECT e1.Name AS Employee
# FROM Employee e1
# LEFT JOIN Employee e2 ON e1.ManagerId = e2.Id
# WHERE e1.Salary > e2.Salary


# Solution B: Don't use "Join" and only use "Where"
SELECT e1.Name AS Employee
FROM Employee e1, Employee e2 
WHERE e1.ManagerId = e2.Id AND e1.Salary > e2.Salary
