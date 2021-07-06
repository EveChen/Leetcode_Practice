
# Link: https://leetcode.com/problems/customers-who-never-order/

# Solution A: Not in
# SELECT Name AS Customers
# FROM Customers
# WHERE Id NOT IN (SELECT CustomerId FROM Orders)

# Solution B: Left JOIN
# SELECT c.Name AS Customers
# FROM Customers c
#     LEFT JOIN Orders o ON c.Id = o.CustomerId
# WHERE o.CustomerId IS NULL


# Solution C: Where Not Exists
# Note: 1 means any. Basically, it tests the subquery for the existence of one or more rows. In our case, it is WHERE NOT EXISTS, so the final result should satisfy the condition that the subquery (the 2nd SELECT) has 0 rows return.
SELECT A.Name AS Customers
from Customers A
WHERE NOT EXISTS (SELECT 1 FROM Orders B WHERE A.Id = B.CustomerId)

