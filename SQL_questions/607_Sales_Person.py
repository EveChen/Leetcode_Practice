
# Link: https://leetcode.com/problems/sales-person/

# 注意: 不能用下面這種思路 - 以原本 test case 的例子，這會找到 sales_id = 4 & 5 的 Pam 和 Alex，可是 orders 裡面 sales_id = 4 的 Pam 明明就和 RED company 有往來 (order_id = 4)
# SELECT s.name
# FROM salesperson s
#     LEFT JOIN orders o ON s.sales_id = o.sales_id
#     LEFT JOIN company c ON o.com_id = c.com_id
# WHERE c.name NOT LIKE 'RED'

       
# 例如: 用下面 query 會跑出 sales_id = 4 & 5，但 4 不應該在這裡
# SELECT o.sales_id
# FROM orders o
#  JOIN company c ON o.com_id = c.com_id
# WHERE c.name NOT LIKE 'RED'


# Solution A: 先找出和RED company有營業往來的sales_id，再把這些sales_id從salesperson table中剔除
# SELECT s.name
# FROM salesperson s
# WHERE s.sales_id NOT IN 
#     (SELECT orders.sales_id
#     FROM orders
#     LEFT JOIN company c ON orders.com_id = c.com_id
#     WHERE c.name LIKE 'RED')


# Solution B: 反向推導的思路，先找出orders中屬於RED company的orders，然後right join salesperson table，去找sales_id != NULL的name
SELECT s.name
FROM orders o
    JOIN company c ON o.com_id = c.com_id AND c.name LIKE 'RED'
    RIGHT JOIN salesperson s ON o.sales_id = s.sales_id WHERE o.sales_id IS NULL

