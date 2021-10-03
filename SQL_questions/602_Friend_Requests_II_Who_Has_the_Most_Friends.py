
# Solution A: 列出所有requester_id跟accepter_id的組合 (union 跟 union all 皆可)
# Select id1 As id, Count(id2) As num
# From (
#     SELECT requester_id AS id1, accepter_id As id2
#     From request_accepted
#     Union #也可以是union all
#     Select accepter_id As id1, requester_id As id2
#     From request_accepted) As tmp
# Group By id1
# Order By num Desc
# Limit 1


# Solution B: 列出所有 id 的 union all (只取subquery看就能明白)(只能用union all)
Select id, Count(*) As num
From (
    Select requester_id As id
    From request_accepted
    Union all
    Select accepter_id As id
    From request_accepted) As tmp
Group By id
Order By num Desc
Limit 1


# Wrong
# Step 1: 每個id丟出邀請，有多少人接受?
# SELECT requester_id, COUNT(accepter_id) AS accept_cnt
# FROM request_accepted
# GROUP BY requester_id

# Step 2: 一個 id 被邀請加好友，且該 id 接受的狀況有幾例? 
# SELECT accepter_id, COUNT(*) AS invited_cnt
# FROM request_accepted
# GROUP BY accepter_id

# Step 3: 加總 
# SELECT requester_id, AS id, (accept_cnt + invited_cnt) AS num
# FROM (
# SELECT requester_id, COUNT(accepter_id) AS accept_cnt
# FROM request_accepted
# GROUP BY requester_id

# UNOIN

# SELECT accepter_id, COUNT(*) AS invited_cnt
# FROM request_accepted
# GROUP BY accepter_id) AS tmp


