
# Link: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

# Solution A: subquery
# SELECT customer_number
# FROM (
#     SELECT customer_number, COUNT(customer_number) AS number_of_order
#     FROM Orders
#     GROUP BY customer_number
#     ORDER BY number_of_order DESC) AS tmp
# LIMIT 1


# Solution B: without subquery
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1


# Windows Function
# SELECT MAX(COUNT(customer_number)) OVER (PARTITION BY order_number) AS customer_number
# FROM orders

