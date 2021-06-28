
# Link: https://leetcode.com/problems/delete-duplicate-emails/

# Solution A: Use "DELETE"
DELETE p2
FROM Person p1
JOIN Person p2 ON p1.Email = p2.Email
WHERE p1.Id < p2.Id


# Same as solution A
# DELETE p2
# FROM Person p1, Person p2
# WHERE p1.Id < p2.Id AND p1.Email = p2.Email

# A bit different from Solution A
# DELETE
# FROM Person
# WHERE Id not in
#     (SELECT tmp.Id 
#      FROM (SELECT min(Id) as Id
#             FROM Person 
#             GROUP BY Email) AS tmp)

# Attention: this will cause a conflict between select and update
# delete from Person where id not in(select min(id) as id from Person group by email)


# Attention: also this is wrong because we still did not delete the duplicate one
# select email,min(id) from Person group by email


# Solution B: Window Function - not test
# SELECT Id, Email
# FROM (SELECT *,
#       ROW_NUMBER() OVER (PARTITION BY Email ORDER BY Id ASC) AS row_rank
#       FROM Person
#         ) AS tmp
# WHERE row_rank = 1

