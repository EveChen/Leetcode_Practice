
# 1st attempt - success
Select ROUND(SUM(IF(order_date = customer_pref_delivery_date, 1, 0))/COUNT(*), 4) * 100 As immediate_percentage
From Delivery


# 2. Use average
# Select Round(Avg(order_date = customer_pref_delivery_date), 4) * 100 As immediate_percentage
# From Delivery


# 3. Intuitive
# Select Round(immediate / total, 4) * 100 As immediate_percentage
# From (
#     (Select Count(*) As immediate From Delivery Where order_date = customer_pref_delivery_date) As tmp1,
#     (Select Count(*) As total From Delivery) As tmp2
#     )



# 4. Intuitive - don't need "From Delivery"
# Select
#     Round(
#         (Select Count(*) From Delivery Where order_date = customer_pref_delivery_date) / 
#         (Select Count(*) From Delivery)
#         , 4) * 100 As immediate_percentage;
