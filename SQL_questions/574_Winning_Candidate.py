
# Solution A:
SELECT Name
FROM (
    SELECT Name, COUNT(*) AS num
    FROM Vote v
        LEFT JOIN Candidate c
        ON v.CandidateId = c.id
    GROUP BY Name) AS tmp
ORDER BY num DESC
LIMIT 1

# Solution B:
# Step1: 先找出Vote table中誰是winner （包括COUNT和ORDER BY+LIMIT)
# Step2: 找出名字，用對應id的方式
# SELECT Name
# FROM Candidate
#     JOIN (SELECT CandidateId
#          FROM Vote
#          GROUP BY CandidateId
#          ORDER BY COUNT(*) DESC
#          LIMIT 1) AS winner
# WHERE Candidate.id = winner.CandidateId



# 同樣邏輯，不同寫法
# SELECT Name
# FROM Candidate
#     JOIN (SELECT CandidateId, COUNT(*) AS Votes
#             FROM Vote
#             GROUP BY CandidateId
#             ORDER BY Votes DESC
#             LIMIT 1) AS temp
#     ON Candidate.Id = temp.CandidateId

# Failed - 不要雞婆，在 subquery 裡多加不相關的 column id
# SELECT DISTINCT Name
# FROM Candidate
#     JOIN (SELECT id, CandidateId, COUNT(CandidateId) AS num
#             FROM Vote
#             GROUP BY CandidateId) AS temp
#     ON Candidate.id = temp.CandidateId
# ORDER BY temp.num DESC
# LIMIT 1
