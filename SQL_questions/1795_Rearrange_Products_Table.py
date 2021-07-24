
# Link: https://leetcode.com/problems/rearrange-products-table/

# Step 1: 先找出 store1 的 product_id & price --> Success
# SELECT product_id, store1 AS price1
# FROM Products
# WHERE store1 IS NOT NULL

# Step 2: 要怎麼才能讓 2nd store 顯示出 store1, 2, 3? --> Failed, 只能顯示出 store1 的資料 {"headers": ["product_id", "store", "price"], "values": [[0, "store1", 95], [1, "store1", 70]]}
# SELECT product_id, (CASE 
#                     WHEN store1 IS NOT NULL THEN 'store1'
#                     WHEN store2 IS NOT NULL THEN 'store2'
#                     WHEN store3 IS NOT NULL THEN 'store3'
#                     END) AS store,
#                     (CASE 
#                     WHEN store1 IS NOT NULL THEN store1
#                     WHEN store2 IS NOT NULL THEN store2
#                     WHEN store3 IS NOT NULL THEN store3
#                     END) AS price
# FROM Products

# Step 3: 要怎樣才能顯示出所有 stores 的資料? --> 看了解答，需要用UNION
SELECT product_id, 'store1' AS store, store1 AS price 
FROM Products 
WHERE store1 IS NOT NULL

UNION

SELECT product_id, 'store2' AS store, store2 AS price
FROM Products
WHERE store2 IS NOT NULL

UNION

SELECT product_id, 'store3' AS store, store3 AS price
FROM Products
WHERE store3 IS NOT NULL
