
# Link: https://leetcode.com/problems/second-highest-salary/

# Solution A: Use 'IFNULL(statement, replacement)' - 記得 subquery 也要括號
SELECT IFNULL(
    (SELECT DISTINCT(Salary)
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1),Null) AS SecondHighestSalary

# # Another similar way for solution A
# inner layer會是empty string，而SELECT(empty string)會return null，故此法可行
# SELECT 
#     (SELECT DISTINCT(Salary)
#     FROM Employee
#     ORDER BY Salary DESC
#     LIMIT 1 OFFSET 1) AS SecondHighestSalary

# Solution B: Compare with itself
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee)


# Another similar way for solution B
# SELECT MAX(a.Salary) AS SecondHighestSalary
# FROM Employee a
#     JOIN Employee b
#     ON a.Salary < b.Salary

# Windows function
# WITH tmp AS
#     (SELECT Salary, RANK() OVER (ORDER BY Salary DESC) AS Rank_desc
#     FROM Employee)
    
# SELECT MAX(Salary) AS SecondHighestSalary
# FROM tmp
# WHERE Rank_desc = 2


# Wrong: 不懂為什麼不能這樣寫
# SELECT IF(COUNT(Salary) <= 1, NULL, ISalary, ) AS SecondHighestSalary
# FROM Employee
# ORDER BY Salary DESC
# LIMIT 1 OFFSET 1

