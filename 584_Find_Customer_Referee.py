
https://leetcode.com/problems/find-customer-referee/description/

# Solution 1: Don't forget "is null"
Select name
From Customer
Where referee_id != 2 Or referee_id is null


# Solution 2: COALESCE is used to replace NULL values with zero before checking whether it is equal to 2 or not.
# SELECT name
# FROM Customer
# WHERE COALESCE(referee_id,0) <> 2


