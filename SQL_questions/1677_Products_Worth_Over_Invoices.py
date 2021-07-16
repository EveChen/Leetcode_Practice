
# Link: https://leetcode.com/problems/products-worth-over-invoices/

# Solution: 注意若 product 沒有 invoice 時的處理
# SELECT name, IFNULL(SUM(rest), 0) AS rest, IFNULL(SUM(paid), 0) AS paid, IFNULL(SUM(canceled), 0) AS canceled, IFNULL(SUM(refunded), 0) AS refunded
# FROM Product p
#     LEFT JOIN Invoice i ON p.product_id = i.product_id
# GROUP BY name
# ORDER BY name


# 同前面做法，只是 IFNULL 改成 COALESCE
SELECT name, COALESCE(SUM(rest), 0) AS rest, 
    COALESCE(SUM(paid), 0) AS paid, 
    COALESCE(SUM(canceled), 0) AS canceled,
    COALESCE(SUM(refunded), 0) AS refunded
FROM Product p
    LEFT JOIN Invoice i ON p.product_id = i.product_id
GROUP BY name
ORDER BY name
