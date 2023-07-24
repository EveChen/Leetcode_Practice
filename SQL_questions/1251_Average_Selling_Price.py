
https://leetcode.com/problems/average-selling-price/description/

#Answer 3 - use ">=, <=" instead of "Between"
Select p.product_id, Round(Sum(units * price) / Sum(units), 2) As average_price
From Prices p
Join UnitsSold s
    On p.product_id = s.product_id
Where purchase_date >= start_date And purchase_date <= end_date
Group By p.product_id



# Answer 2 - use "Where" instead of "On" two criteria 
# Select p.product_id, Round(Sum(units * price)/Sum(units) ,2) As average_price
# From Prices p
# Join UnitsSold s
#     On p.product_id = s.product_id
# Where purchase_date Between start_date And end_date
# Group By p.product_id


#Answer 1 - (Join on two criterias)
# Select p.product_id, Round(Sum(p.price * s.units) / Sum(s.units), 2) As average_price
# From Prices p
# Join UnitsSold s
#     On p.product_id = s.product_id AND purchase_date Between start_date And end_date
# Group By product_id




# My wrong answer
# Select product_id, Round(total_price / total_units, 2) As average_price
# From (
#     Select p.product_id, units * IF(purchase_date >= start_date
#         And purchase_date <= end_date, price, 0) As total_price, Sum(units) As total_units
#     From Prices p
#     Join UnitsSold s
#     On p.product_id = s.product_id
#     ) As tmp
