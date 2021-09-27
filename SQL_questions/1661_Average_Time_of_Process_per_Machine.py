
# Wrong - why?
# SELECT tmp1.machine_id, ROUND(AVG(tmp2.end_time - tmp1.start_time), 3) AS processing_time
# FROM (
#     SELECT machine_id, process_id, timestamp AS start_time
#     FROM Activity
#     WHERE activity_type = "start") as tmp1
#     JOIN (
#         SELECT machine_id, process_id, timestamp AS end_time
#         FROM Activity
#         WHERE activity_type = "end") AS tmp2
# GROUP BY tmp1.machine_id


# Solution A: self-join
# 除了 AVG，也可以用 SUM()/COUNT(process_id)
# SELECT s.machine_id, ROUND(SUM(e.timestamp - s.timestamp)/COUNT(s.process_id), 3) AS processing_time
# FROM Activity s
#     JOIN Activity e ON s.machine_id = e.machine_id AND s.process_id = e.process_id
#     AND s.activity_type = 'start' AND e.activity_type = 'end'
# GROUP BY machine_id


# Solution B: use case when
# SELECT machine_id, ROUND(
#                         (SUM(CASE WHEN activity_type = 'end' THEN timestamp END) - 
#                         SUM(CASE WHEN activity_type = 'start' THEN timestamp END)) / 
#                         COUNT(DISTINCT process_id), 3) AS processing_time
# FROM Activity
# GROUP BY machine_id
