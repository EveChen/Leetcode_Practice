
# https://leetcode.com/problems/sales-analysis-i/

# # Solution A: 直接用 Sales table 中的 price
# Select seller_id
# From Sales
# Group By seller_id
# Having Sum(price) = (Select Sum(price)
#                     From Sales
#                     Group By seller_id
#                     Order By 1 Desc
#                     Limit 1)


# Solution B: 先做一個 tmp table 再 query
# With tmp As
# (Select seller_id, Sum(price) As total_price
# From Sales
# Group by seller_id)

# Select seller_id
# From tmp
# Where total_price = (Select Max(total_price)
#                     From tmp)




-- -- Solution C: rank()
-- select seller_id
-- from
--     (select seller_id, 
--             rank() over(order by sum(price) desc) as rank
--     from Sales
--     group by seller_id) as tmp
-- where rank = 1


-- Solution D: Top 1 with ties
Select Top 1 With Ties seller_id
From Sales
Group By seller_id
Order By Sum(price) Desc


