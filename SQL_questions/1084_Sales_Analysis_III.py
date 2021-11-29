
# https://leetcode.com/problems/sales-analysis-iii/

# Failed: 第二個產品有兩個被賣出的時間點，其中一個不是春天賣出的
# Select distinct p.product_id, p.product_name
# From Product p
#     Join Sales s On p.product_id = s.product_id
# Where sale_date Between '2019-01-01' And '2019-03-31'


# Solution A: 同 II 加上 filter out 的條件
Select distinct p.product_id, p.product_name
From Product p
    Join Sales s On p.product_id = s.product_id
Where sale_date Between '2019-01-01' And '2019-03-31'
    And p.product_id Not in (Select product_id
                            From Sales
                            Where sale_date < '2019-01-01'
                                Or sale_date > '2019-03-31')

# Solution C: 用 having + min/max
Select Distinct p.product_id, p.product_name
From Product p 
    Join Sales s On p.product_id = s.product_id
Group By p.product_id
Having Min(sale_date) >= '2019-01-01'
    And Max(sale_date) <= '2019-03-31'
		
		
# Solution D: 用 in
Select product_id, product_name
From Product
Where product_id In (Select product_id
                     From Sales
                     Group By product_id
                     Having Min(sale_date) >= '2019-01-01'
                        And Max(sale_date) <= '2019-03-31')
												
												
												
-- Solution B: 用Except語法
Select distinct p.product_id, p.product_name
From Product p Join Sales s On p.product_id = s.product_id
Where sale_date Between '2019-01-01' And '2019-03-31'

Except

Select distinct p.product_id, p.product_name
From Product p Join Sales s On p.product_id = s.product_id
Where sale_date < '2019-01-01' Or sale_date > '2019-03-31'
