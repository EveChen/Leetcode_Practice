
# https://leetcode.com/problems/product-sales-analysis-ii/

# Wrong answer: 記得要加上SUM那麼GROUP BY才能運行
# SELECT product_id, quantity
# FROM Sales
# GROUP BY product_id

# Solution A: 但這個答案並沒有考慮quantity為0的product_id
# SELECT product_id, 
#     IFNULL(SUM(quantity), 0) AS total_quantity
# FROM Sales
# GROUP BY product_id

# Solution B: 比較完整的解答，畢竟題目問的是EVERY product_id
SELECT p.product_id,
    IFNULL(SUM(quantity), 0) AS total_quantity
FROM Product p
    JOIN Sales s
    ON p.product_id = s.product_id
GROUP BY p.product_id
