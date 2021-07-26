
# Link: https://leetcode.com/problems/queries-quality-and-percentage/

# Solution A: use sum()/count()
# SELECT query_name, ROUND(SUM(rating/position)/COUNT(*), 2) AS quality, 
#     ROUND(SUM(IF(rating < 3, 1, 0))/COUNT(*) * 100, 2) AS poor_query_percentage
# FROM Queries
# GROUP BY query_name


# Solution B: use AVG
#rating < 3 returns either 1 and 0 for each group. Then AVG the groups returns the proportion of 1 and 0 which can be converted to a %

SELECT query_name, ROUND(AVG(rating/position), 2) AS quality,
    ROUND(AVG(rating < 3) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name
    


