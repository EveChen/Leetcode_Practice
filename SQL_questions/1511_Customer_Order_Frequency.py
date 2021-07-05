
# Link: https://leetcode.com/problems/customer-order-frequency/

# Solution A: Use Group by and Subquery 
# SELECT customer_id, name
# FROM (
#     SELECT c.customer_id, c.name, 
#         SUM(IF(MONTH(order_date) = 6, price * quantity, 0)) AS total_June,
#         SUM(IF(MONTH(order_date) = 7, price * quantity, 0)) AS total_July
#     FROM Customers c
#     LEFT JOIN Orders o ON c.customer_id = o.customer_id
#     LEFT JOIN Product p ON o.product_id = p.product_id
#     GROUP BY customer_id) AS tmp
# WHERE total_June >= 100 AND total_July >= 100

# Solution B: No subquery
SELECT c.customer_id, c.name
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
LEFT JOIN Product p ON o.product_id = p.product_id
GROUP BY customer_id
HAVING 
    SUM(IF(MONTH(order_date) = 6, price * quantity, 0)) >= 100 AND
    SUM(IF(MONTH(order_date) = 7, price * quantity, 0)) >= 100
    
