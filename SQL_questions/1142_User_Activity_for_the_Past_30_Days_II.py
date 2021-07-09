
# Link: https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/

# Solution A: group by + subquery
# Cond 1: DATE_SUB('2019-07-27', INTERVAL 30 DAY)
# Cond 2: ROUND(, 2)
# Cond 3: count for a user are those with at least one activity in that time period.
# SELECT IFNULL(ROUND(SUM(session_per_user) / COUNT(DISTINCT user_id), 2), 0) AS average_sessions_per_user
# FROM (
#     SELECT user_id, COUNT(DISTINCT session_id) AS session_per_user
#     FROM Activity
#     WHERE activity_date > DATE_SUB('2019-07-27', INTERVAL 30 DAY)
#     # WHERE activity_date > SUBDATE('2019-07-27', 30)
#     # WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
#     # WHERE DATEDIFF(DAY,activity_date,'2019-07-27') BETWEEN 0 AND 29 #SQL server
#     GROUP BY user_id) AS tmp

# Solution B: no subquery
SELECT IFNULL(ROUND(COUNT(DISTINCT user_id, session_id) / COUNT(DISTINCT user_id) ,2), 0) AS average_sessions_per_user
FROM Activity
WHERE activity_date > SUBDATE('2019-07-27', 30)


