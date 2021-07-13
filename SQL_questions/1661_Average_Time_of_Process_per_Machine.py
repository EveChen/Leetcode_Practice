
# Link: https://leetcode.com/problems/average-time-of-process-per-machine/

# Solution A: self-join
# Q: 為什麼用 AVG?
# SELECT s.machine_id, ROUND(AVG(e.timestamp - s.timestamp), 3) AS processing_time
# FROM Activity s
#     JOIN Activity e ON s.machine_id = e.machine_id AND s.process_id = e.process_id
#     AND s.activity_type = 'start' AND e.activity_type = 'end'
# GROUP BY machine_id

# Solution B: use case when
SELECT machine_id, ROUND(
                        (SUM(CASE WHEN activity_type = 'end' THEN timestamp END) - 
                        SUM(CASE WHEN activity_type = 'start' THEN timestamp END)) / 
                        COUNT(DISTINCT process_id), 3) AS processing_time
FROM Activity
GROUP BY machine_id
