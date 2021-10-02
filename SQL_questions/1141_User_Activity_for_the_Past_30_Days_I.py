
# Wrong
# {"headers": ["day", "active_users"], "values": [["2019-07-20", 3], ["2019-07-20", 1], ["2019-07-21", 2], ["2019-07-21", 3]]}
# SELECT activity_date AS day, COUNT(activity_type) AS active_users
# FROM Activity
# WHERE activity_date >= '2019-06-28' AND activity_date <= '2019-07-27'
# GROUP BY activity_date, user_id


# Solution A: Where
# SELECT activity_date AS day, COUNT(Distinct user_id) AS active_users
# FROM Activity
# WHERE activity_date >= '2019-06-28' AND activity_date <= '2019-07-27'
# GROUP BY activity_date

# Solution B: Datediff
# SELECT activity_date AS day, COUNT(Distinct user_id) AS active_users
# FROM Activity
# WHERE DATEDIFF('2019-07-27', activity_date) < 30
# GROUP BY activity_date

# Solution C: Date_sub
SELECT activity_date AS day, COUNT(Distinct user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN Date_sub('2019-07-27', Interval 29 day) AND '2019-07-27'
GROUP BY activity_date

