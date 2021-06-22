

#link: https://leetcode.com/problems/recyclable-and-low-fat-products/

# Solution A
# Write your MySQL query statement below
SELECT product_id
FROM Products
WHERE low_fats = 'Y'
    AND recyclable = 'Y'

# Another way
# SELECT product_id
# FROM Products
# WHERE low_fats LIKE '%Y%'
#     AND recyclable LIKE '%Y%'
