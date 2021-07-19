
# Link: https://leetcode.com/problems/patients-with-a-condition/

# Solution A: 記得 '% DIAB1%' 因為題目有說明 'Space DIAB1...'的狀況，例如 ACNE DIAB100
# SELECT *
# FROM Patients
# WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'

# Solution B: Use REGEXP
# REGEXP: https://dataschool.com/how-to-teach-people-sql/how-regex-works-in-sql/
SELECT *
FROM Patients
WHERE conditions REGEXP '^DIAB1| DIAB1';

