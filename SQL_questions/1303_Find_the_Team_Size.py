
# Link: https://leetcode.com/problems/find-the-team-size/

# 問題: 結果只有employee_id = 1, 4, 5 --> {"headers": ["employee_id", "team_size"], "values": [[1, 3], [4, 1], [5, 2]]}
# SELECT employee_id, COUNT(team_id) AS team_size
# FROM Employee
# GROUP BY team_id

# Solution A: subquery
# SELECT employee_id, team_size
# FROM Employee e
#     LEFT JOIN (
#             SELECT team_id, COUNT(DISTINCT employee_id) AS team_size
#             FROM Employee 
#             GROUP BY team_id) as tmp
#     ON e.team_id = tmp.team_id


# Solution B: correlated subquery or a synchronized subquery
# 邏輯: 每一次 WHERE 裡面條件符合的時候，就會在 COUNT(team_id) 加上 1
SELECT employee_id, (SELECT COUNT(team_id) 
                     FROM Employee
                     WHERE e.team_id = team_id) AS team_size
FROM Employee e
