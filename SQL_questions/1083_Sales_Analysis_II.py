
# https://leetcode.com/problems/sales-analysis-ii/

# Failed solution: 不能用 WHERE 直接判斷，因為 query 只能一條條判斷「當前」buyer 購買的手機是否含有 'S8' 字樣? 或者沒有包含 'iPhone' 字樣，若相同的 buyer_id 出現多次，query 無法判斷
# SELECT DISTINCT buyer_id
# FROM Sales s
#     LEFT JOIN Product p ON s.product_id = p.product_id
# WHERE product_name = 'S8' AND product_name != 'iPhone'


# Solution A:
# 思路: 該顧客至少要買一支 S8 (所以 SUM() > 0)，且絕對不能買 iPhone (所以 SUM() = 0)
# SELECT buyer_id
# FROM Sales s 
#     JOIN Product p ON s.product_id = p.product_id
# GROUP BY buyer_id
# HAVING SUM(CASE 
#            WHEN product_name = 'S8' THEN 1
#            ELSE 0 END) > 0
#     AND SUM(CASE
#             WHEN product_name = 'iPhone' THEN 1
#             ELSE 0 END) = 0
            
# Same as solution A: use SUM() but more explicit
# SELECT buyer_id
# FROM Sales s JOIN Product p ON s.product_id = p.product_id
# GROUP BY buyer_id
# HAVING SUM(product_name = 'S8') > 0
#     AND SUM(product_name = 'iPhone') = 0

# Solution B: 不用 having，改用 not in，較直覺的做法
# 思路: 先選取有購買 S8 的 buyer_id，再把有購買 iPhone 的 buyer_id 做成 subquery，讓 buyer_id NOT IN (subquery)
SELECT DISTINCT buyer_id
FROM Sales s JOIN Product p ON s.product_id = p.product_id
WHERE product_name = 'S8' AND
    buyer_id NOT IN (SELECT DISTINCT buyer_id
                    FROM Sales s JOIN Product p
                                ON s.product_id = p.product_id
                    WHERE product_name = 'iPhone')
										
-- # Solution C: 用 Except 語法
Select Distinct buyer_id
From Sales s Join Product p On s.product_id = p.product_id
Where product_name = 'S8'

Except

Select Distinct buyer_id
From Sales s Join Product p On s.product_id = p.product_id
Where product_name = 'iPhone'



            
