
# Link: https://leetcode.com/problems/warehouse-manager/

# Solution A: subquery
# 思路: 先求出每個產品的 per_volume，再求出每個 warehouse 的 volume
SELECT name AS warehouse_name, SUM(per_volume * units) AS volume
FROM Warehouse w
    LEFT JOIN (
        SELECT product_id, (width * Length * Height) AS per_volume
        FROM Products
        # GROUP BY product_id 不用這行也可以
          ) AS tmp
    ON w.product_id = tmp.product_id
GROUP BY name

# Solution B: 不使用 subquery
# SELECT name AS warehouse_name, SUM(units * Width * Length * Height) AS volume
# FROM Warehouse w
#     LEFT JOIN Products p
#     ON w.product_id = p.product_id
# GROUP BY name
