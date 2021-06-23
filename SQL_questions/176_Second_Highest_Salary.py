
# Link: https://leetcode.com/problems/second-highest-salary/

# Solution A: Use 'IFNULL(statement, replacement)'
SELECT IFNULL(
    (SELECT DISTINCT(Salary)
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1),Null) AS SecondHighestSalary


# Another similar way --> Q: seems not deal with 'null' criteria
SELECT 
    (SELECT DISTINCT(Salary)
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1) AS SecondHighestSalary


# Solution B: Compare with itself
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee)
