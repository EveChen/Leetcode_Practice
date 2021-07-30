
# Link: https://leetcode.com/problems/game-play-analysis-ii/

/* Use Windows function - Rank */
SELECT player_id, device_id
FROM (SELECT player_id, device_id,
      RANK() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS num_rank
     FROM Activity) AS tmp
WHERE tmp.num_rank = 1

# Failed - 不懂為什麼 @@
# SELECT player_id, device_id
# FROM (
#     SELECT player_id, device_id, MIN(event_date)
#     FROM Activity
#     GROUP BY player_id) AS tmp

# 發現 player_id 和 MIN(event_date) 是對的，不對的只有 device_id
# 原因: 如果不是 group by 所有 select 裡的東西，那麼 MySQL 會隨便選「沒有被groupby到的那個feature的值」，詳細可見這裡下方的解釋https://leetcode.com/problems/game-play-analysis-ii/discuss/312336/MySQL-Solution
# SELECT player_id, device_id, MIN(event_date)
# FROM Activity
# GROUP BY player_id

# 用這個方法可以找到正確的 minimum event_date
# SELECT MIN(event_date) 
# FROM Activity 
# GROUP BY player_id

# 用這個也可以找到正確的 minimum event_date
# SELECT player_id, MIN(event_date)
# FROM Activity
# GROUP BY player_id

# Failed，因為 having 裡只能裝之前 groupby 中的 variable、或者有在aggregation裡的variable，詳請見下方註解https://leetcode.com/problems/game-play-analysis-ii/discuss/312336/MySQL-Solution
# select player_id, device_id
# from Activity
# group by player_id
# having(min(event_date))


# Solution A: Subquery + Where in
# SELECT player_id, device_id
# FROM Activity
# WHERE (player_id, event_date) IN (SELECT player_id, MIN(event_date)
#                                  FROM Activity
#                                  GROUP BY player_id)


