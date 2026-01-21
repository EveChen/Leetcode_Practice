
-- # Method 1: self join
-- Select e1.name As Employee
-- From Employee e1, Employee e2
-- Where e1.managerId = e2.id
--     And e1.salary > e2.salary

-- # Method 1.1
-- Select e1.name As Employee
-- From Employee e1
-- Join Employee e2 On e1.managerId = e2.id
-- Where e1.salary > e2.salary

# Method 2: subquery，在 subquery 中找主管的薪水，在 main query 中把員工跟主管的薪水拿來比較
Select name As Employee
From Employee e1
Where salary > (
    Select salary
    From Employee e2
    Where e1.managerId = e2.id
)
