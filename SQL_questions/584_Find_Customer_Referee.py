
https://leetcode.com/problems/find-customer-referee/description/

# Solution 1: Don't forget "is null"
Select name
From Customer
Where referee_id != 2 Or referee_id is null


# Solution 2: COALESCE is used to replace NULL values with zero before checking whether it is equal to 2 or not.
# SELECT name
# FROM Customer
# WHERE COALESCE(referee_id,0) <> 2


# Wrong answer
# Select c1.name
# From Customer c1
# Join Customer c2
# On c1.id = c2.id AND c2.referee_id != 2 


# Wrong answer
# Select name
# From Customer c1
# Where referee_id Not In (Select id
#         From Customer c2
#         Where id = 2) 
