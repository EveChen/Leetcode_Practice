
https://leetcode.com/problems/employee-bonus/description/

# Solution 1: Left join
SELECT name, bonus
FROM Employee
    LEFT JOIN Bonus ON Employee.empId = Bonus.empId
WHERE bonus < 1000 OR bonus IS NULL
# 也可以寫成 WHERE bonus < 1000 OR ISNULL(bonus)



# Wrong Answer
# Select name, bonus
# From (
#         Select name, bonus
#         From Employee e
#         Join Bonus b
#             On e.empId = b.empId
#         Where bonus < 1000 Or bonus is null
# ) As tmp


# Wrong answer
# Select name, bonus
# From Employee e
# Join Bonus b
#     On e.empId = b.empId
# Where bonus < 1000 Or bonus is null
