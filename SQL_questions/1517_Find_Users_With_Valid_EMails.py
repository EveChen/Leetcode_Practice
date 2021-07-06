
# Link: https://leetcode.com/problems/find-users-with-valid-e-mails/

# Solution A: Use Regular expression
SELECT *
FROM Users
WHERE REGEXP_LIKE(mail, '^[A-Za-z]+[A-Za-z0-9\_\.\-]*@leetcode.com')

