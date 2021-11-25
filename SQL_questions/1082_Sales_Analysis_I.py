
# https://leetcode.com/problems/sales-analysis-i/

# Solution - 直接用 Sales table 中的 price
Select seller_id
From Sales
Group By seller_id
Having Sum(price) = (Select Sum(price)
                    From Sales
                    Group By seller_id
                    Order By 1 Desc
                    Limit 1)

