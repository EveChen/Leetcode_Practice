
# Link: https://leetcode.com/problems/reformat-department-table/

# Solution: create each column by sum up the monthly revenue
# Note: understand why we need to have "Sum" instead of using case when directly
# Note: we can also use "MAX" instead of "SUM"
SELECT id, 
    SUM(CASE WHEN month = 'Jan' THEN revenue ELSE null END) AS Jan_Revenue,
    SUM(CASE WHEN month = 'Feb' THEN revenue ELSE null END) AS Feb_Revenue,
    SUM(CASE WHEN month = 'Mar' THEN revenue ELSE null END) AS Mar_Revenue,
    SUM(CASE WHEN month = 'Apr' THEN revenue ELSE null END) AS Apr_Revenue,
    SUM(CASE WHEN month = 'May' THEN revenue ELSE null END) AS May_Revenue,
    SUM(CASE WHEN month = 'Jun' THEN revenue ELSE null END) AS Jun_Revenue,
    SUM(CASE WHEN month = 'Jul' THEN revenue ELSE null END) AS Jul_Revenue,
    SUM(CASE WHEN month = 'Aug' THEN revenue ELSE null END) AS Aug_Revenue,
    SUM(CASE WHEN month = 'Sep' THEN revenue ELSE null END) AS Sep_Revenue,
    SUM(CASE WHEN month = 'Oct' THEN revenue ELSE null END) AS Oct_Revenue,
    SUM(CASE WHEN month = 'Nov' THEN revenue ELSE null END) AS Nov_Revenue,
    SUM(CASE WHEN month = 'Dec' THEN revenue ELSE null END) AS Dec_Revenue
FROM Department
GROUP BY id
ORDER BY id
    
# Solution: same logic but use if
# SELECT id,
#     MAX(IF(month = 'Jan', revenue, null)) AS Jan_Revenue,
#     MAX(IF(month = 'Feb', revenue, null)) AS Feb_Revenue,
#     MAX(IF(month = 'Mar', revenue, null)) AS Mar_Revenue,
#     MAX(IF(month = 'Apr', revenue, null)) AS Apr_Revenue,
#     MAX(IF(month = 'May', revenue, null)) AS May_Revenue,
#     MAX(IF(month = 'Jun', revenue, null)) AS Jun_Revenue,
#     MAX(IF(month = 'Jul', revenue, null)) AS Jul_Revenue,
#     MAX(IF(month = 'Aug', revenue, null)) AS Aug_Revenue,
#     MAX(IF(month = 'Sep', revenue, null)) AS Sep_Revenue,
#     MAX(IF(month = 'Oct', revenue, null)) AS Oct_Revenue,
#     MAX(IF(month = 'Nov', revenue, null)) AS Nov_Revenue,
#     MAX(IF(month = 'Dec', revenue, null)) AS Dec_Revenue
# FROM Department
# GROUP BY id
# ORDER BY id
    
