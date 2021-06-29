

# Link: https://leetcode.com/problems/swap-salary/

# Solution: use if
# UPDATE Salary
# SET sex = IF(sex = 'm', 'f', 'm')


# Solution: use case when
UPDATE Salary
SET sex = CASE WHEN sex = 'm' THEN 'f'
                ELSE 'm'
                END
                
              
