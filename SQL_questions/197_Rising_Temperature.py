
https://leetcode.com/problems/rising-temperature/description/

# 這邊 w2 是現在、w1是過去
# Solution 1: Use "SUBDATE"
# MySQL SUBDATE() subtracts a time value (as interval) from a given date.
Select w2.id As Id
From Weather w1, Weather w2
Where Subdate(w2.RecordDate, 1) = w1.RecordDate
    And w2.temperature > w1.temperature



# Solution 2: Use "Datediff"
# Select w2.id As Id
# From Weather w1, Weather w2
# Where Datediff(w2.recordDate, w1.recordDate) = 1
#     And w2.temperature > w1.temperature
    

# Solution 3: Us "To_Days"
# Select w2.id As Id
# From Weather w1, Weather w2
# Where To_Days(w1.recordDate) + 1 = To_Days(w2.recordDate)
#     And w2.temperature > w1.temperature



# Solution 4: Join with datediff
#思路: 這邊 w2 是現在、w1是過去
# SELECT w2.id
# FROM Weather w1
#     JOIN Weather w2 
#     ON DATEDIFF(w2.recordDate, w1.recordDate) = 1
# WHERE w1.temperature < w2.temperature



# Solution 5: Same logic but use "TO_DAYS"
# TO_DAYS(DATE) return the number of days between from year 0 to date DATE
# SELECT w2.id
# FROM Weather w1
# JOIN Weather w2
# ON TO_DAYS(w1.recordDate) + 1 = TO_DAYS(w2.recordDate)
# WHERE w1.Temperature < w2.Temperature



