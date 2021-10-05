

# 改過test case後的正解
SELECT Request_at AS Day,
    ROUND(SUM(IF(Status != 'completed', 1, 0))/
          COUNT(*), 2) AS 'Cancellation Rate'
FROM Trips
WHERE Client_Id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
    AND Driver_Id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
    AND (Request_at BETWEEN '2013-10-01' AND '2013-10-03')
GROUP BY Day


# Method 1: Without Join, 將第二個table Users當作其中一個Where的條件，而不是創造第二個table - currently wrong answer
# 注意要點: IF(__, __, __)怎麼設置? BETWEEN 日期1 AND 日期2 用法, Request_at BETEEN這一行要括弧起來
# 小錯誤: 'Cancellation Rate' 記得加引號、注意各個地方的types, 大小寫
# 也可以寫成SUM(IF(Status != 'completed', 1, 0))，記得是SUM而不是COUNT
# SELECT Request_at AS Day, 
#         ROUND(COUNT(IF(Status != "completed", TRUE, NULL)) / COUNT(*), 2) AS 'Cancellation Rate'
# FROM Trips
# WHERE Client_Id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
#     AND (Request_at BETWEEN '2013-10-01' AND '2013-10-03')
# GROUP BY Request_at
         

# Method 2: With Join - currently wrong answer
# Key: 記得 Join on 除了key之外，還可以加條件
# SELECT Request_at AS Day, 
#     ROUND(COUNT(IF(status != "completed", TRUE, NULL)) / COUNT(*), 2) AS 'Cancellation Rate'
# FROM Trips
#     INNER JOIN Users
#     ON Trips.Client_Id = Users.Users_Id AND Users.Banned = 'No'
# WHERE (Request_at BETWEEN '2013-10-01' AND '2013-10-03')
# GROUP BY Request_at
      
# 其中，計算Cancellation Rate那行也可以用CASE WHEN來處理
# ROUND(SUM(CASE WHEN 
#                 Trips.Status LIKE 'cancelled_%' 
#                 THEN 1 ELSE 0 
#                 END) / COUNT(*), 2) AS 'Cancellation Rate'

                
# Wrong: 雖然test case正確，但無法處理分母為零的狀況
# SELECT Request_at AS Day,
#     ROUND(SUM(IF(Status LIKE 'cancell%' AND Client_Id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes'), 1, 0)) / 
#           SUM(IF(Client_Id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes'), 1, 0)), 2)AS 'Cancellation Rate'
# FROM Trips
# WHERE Request_at BETWEEN '2013-10-01' AND '2013-10-03'
# GROUP BY Day
# ORDER BY Day ASC


# My Failed Codes: 我想先做兩個tables, 然後join起來
# SELECT trip_temp.Request_at AS Day, (COUNT()) AS Cancellation Rate
# FROM (SELECT *, COUNT(Status) AS freq
#         FROM Trips
#         WHERE Request_at = '2013-10-01' OR Request_at = '2013-10-02' OR Request_at = '2013-10-03'
#         GROUP BY Status) AS trip_temp 
#     INNER JOIN (SELECT *
#                FROM Users
#                WHERE Banned = 'No') AS user_temp 
#         ON trip_temp.Client_Id = user_temp.Users_Id




