
# Link: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

# Solution A: subquery
# Step 1: 先找出沒有買的 customer_id --> Success
# SELECT customer_id
# FROM Visits
# WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
# GROUP BY customer_id

# Step 2: 找出沒有買的 customer_id，且他們出現的次數 --> Success
# SELECT customer_Id, COUNT(customer_id) AS count_no_trans
# FROM Visits
# WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
# GROUP BY customer_id

# Solution B: left join
SELECT customer_id, COUNT(customer_id) AS count_no_trans
FROM Visits v
    LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY customer_id


# Failed
# SELECT customer_id, SUM(IF(visit_id IN (SELECT visit_id FROM Transactions), 0, 1)) AS count_no_trans
# FROM Visits
# GROUP BY customer_id
