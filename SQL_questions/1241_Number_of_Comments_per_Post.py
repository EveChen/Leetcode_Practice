
# Link: https://leetcode.com/problems/number-of-comments-per-post/

# Write your MySQL query statement below
# 找一個sub_id底下有幾個不重複的comments (parent_id = sub_id 的)
# SELECT DISTINCT s1.sub_id AS post_id, COUNT(DISTINCT s1.parent_id) AS number_of_comments
# FROM Submissions s1
#     JOIN Submissions s2 ON s2.sub_id = s1.parent_id
# GROUP BY s1.sub_id
# ORDER BY s1.sub_id ASC

# 退一步，先找sub_id = 1底下有多少個不重複的comments
# SELECT parent_id, COUNT(DISTINCT sub_id)
# FROM Submissions s1
# WHERE parent_id IS NOT NULL
# GROUP BY parent_id
# ORDER BY sub_id ASC

# 處理兩個 edge cases
# 1. parent_id = 7, 有一個comment，可是這個post並沒有出現在sub_id中
# 2. 有一則post的sub_id = 12，然而它的parent_id = NULL (i.e. 代表沒有 comment)
# 對一半，僅解決了 #1 case
# SELECT DISTINCT parent_id, COUNT(DISTINCT sub_id)
# FROM Submissions
# WHERE parent_id IS NOT NULL AND parent_id IN (SELECT sub_id FROM Submissions)
# GROUP BY parent_id
# ORDER BY parent_id ASC

# Q: 怎麼處理第二個 edge case? @@
# A: 先試著讓答案顯示 (12, 0) --> 代表有篇編號 12 號的 post 只有 0 則 comment 
# Wrong!
# SELECT s1.*
# FROM Submissions s1
#     JOIN Submissions s2 ON s1.parent_id = s2.sub_id

# 若 parent_id = NULL 代表 sub_id 是 post 而非 comment --> 先找出 post 有哪些
# Correct!
# SELECT DISTINCT sub_id
# FROM Submissions
# WHERE parent_id IS NULL

# 找出 posts 分別有 sub_id = 1, 2, 12 後，若 parent_id 不等於 sub_id，則 count = 0
# Wrong! [[1, 0], [2, 0], [12, 0]]
# SELECT DISTINCT sub_id AS post_id, 
#     SUM(IF(parent_id IN (SELECT sub_id FROM Submissions), 1, 0)) AS number_of_comments
# FROM (SELECT *
#      FROM Submissions
#      WHERE parent_id IS NULL) AS tmp
# GROUP BY sub_id
# ORDER BY sub_id ASC

# 單獨求 (12, 0)
# Wrong!
# SELECT DISTINCT parent_id, COUNT(DISTINCT sub_id)
# FROM Submissions
# WHERE parent_id IS NULL 
# GROUP BY sub_id



# SELECT
#     DISTINCT sub_id AS post_id,
#     (SELECT COUNT(DISTINCT sub_id) 
#      FROM Submissions S2 
#      WHERE S1.sub_id = S2.parent_id) AS number_of_comments
# FROM
#     Submissions AS S1
# WHERE parent_id IS NULL
# ORDER BY sub_id

SELECT a.sub_id                 AS post_id, 
       Count(DISTINCT b.sub_id) AS number_of_comments 
FROM   submissions a 
       LEFT JOIN submissions b 
              ON a.sub_id = b.parent_id 
WHERE  a.parent_id IS NULL 
GROUP  BY a.sub_id 
ORDER  BY NULL 

     
