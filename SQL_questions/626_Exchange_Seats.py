
# Link: https://leetcode.com/problems/exchange-seats/

# Wrong: Why? --> 必須要新建一個 LENGTH，而不能直接 COUNT(*)
# SELECT (CASE
#             WHEN MOD(id, 2) = 1 AND id = COUNT(*) THEN id
#             WHEN MOD(id, 2) = 1 AND id != COUNT(*) THEN id + 1
#             WHEN MOD(id, 2) = 0 THEN id - 1
#         END) AS id, student
# FROM seat
# ORDER BY id ASC


# Method 1: 核心概念是調轉 Id, 最後Order By
# If 奇數，則id + 1, 但如果最後一個id是奇數，那該id不變; If偶數，則Id - 1

SELECT (CASE 
        WHEN MOD(id, 2) != 0 AND id != Length THEN id + 1
        WHEN MOD(Id, 2) != 0 AND id = Length THEN id
       ELSE id - 1
       END) AS id, student
FROM seat, (SELECT COUNT(*) AS Length
           FROM seat) AS CountFreq
ORDER BY id ASC
