
# Link: https://leetcode.com/problems/consecutive-available-seats/

# Solution A
# SELECT DISTINCT c1.seat_id
# FROM cinema c1, cinema c2 #can use join as well
# WHERE ABS(c1.seat_id - c2.seat_id) = 1
#     AND c1.free = 1 AND c2.free = 1
# ORDER BY c1.seat_id ASC


# Same solution but use join
# SELECT DISTINCT c1.seat_id
# FROM cinema c1
# JOIN cinema c2 ON ABS(c1.seat_id - c2.seat_id) = 1
#     AND c1.free = 1 AND c2.free = 1
# ORDER BY c1.seat_id ASC

# Solution B: similar to solution A and somehow explains the question
# Q: 這邊不能用 c1.seat_id = c2.seat_id - 1 或者 c1.seat_id + 1 = c2.seat_id，還不曉得原因
SELECT DISTINCT c1.seat_id 
FROM cinema c1, cinema c2
WHERE c1.free = 1 AND c2.free = 1 
    AND (c1.seat_id = c2.seat_id + 1 OR c1.seat_id = c2.seat_id - 1)
ORDER BY c1.seat_id ASC



# Solution C: different logic
# SELECT DISTINCT seat_id
# FROM cinema
# WHERE free = 1 AND (
#     seat_id - 1 IN (SELECT seat_id FROM cinema WHERE free = 1) OR
#     seat_id + 1 IN (SELECT seat_id FROM cinema WHERE free = 1))
# ORDER BY seat_id ASC




