
# Link: https://leetcode.com/problems/products-price-for-each-store/

# My SQL Server
/* hard code pivot */
-- SELECT *
-- FROM (
--         SELECT product_id, store, price FROM Products) AS t1
--     PIVOT
--     (MAX(price) FOR store IN ([store1], [store2], [store3])) AS t2


# Solution A: Naive case when & groupby
# 因為用了 groupby 所以需要加上 sum 或者 max，至於為什麼是 sum/max，看這題下方的網友說明 https://leetcode.com/problems/reformat-department-table/discuss/376357/MySQLPostgreSQL-solutions
# SELECT product_id, 
#     SUM(CASE WHEN store LIKE 'store1' THEN price ELSE null END) AS 'store1',
#     SUM(CASE WHEN store LIKE 'store2' THEN price ELSE null END) AS 'store2',
#     SUM(CASE WHEN store LIKE 'store3' THEN price ELSE null END) AS 'store3'
# FROM Products
# GROUP BY product_id


# Solution B: 不使用 GROUPBY，而改用 WITH + LEFT JOIN
WITH t0 AS (SELECT DISTINCT product_id FROM Products),
     t1 AS (SELECT product_id, price AS price1 FROM Products WHERE store LIKE 'store1'),
     t2 AS (SELECT product_id, price AS price2 FROM Products WHERE store LIKE 'store2'),
     t3 AS (SELECT product_id, price AS price3 FROM Products WHERE store LIKE 'store3')
     
SELECT t0.product_id, t1.price1 AS store1, t2.price2 AS store2, t3.price3 AS store3
FROM t0
    LEFT JOIN t1 ON t0.product_id = t1.product_id
    LEFT JOIN t2 ON t0.product_id = t2.product_id
    LEFT JOIN t3 ON t0.product_id = t3.product_id

