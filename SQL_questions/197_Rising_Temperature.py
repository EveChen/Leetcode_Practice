
# Link: https://leetcode.com/problems/rising-temperature/

# Solution A: Join with datediff
#思路: 這邊 w2 是現在、w1是過去
# SELECT w2.id
# FROM Weather w1
#     JOIN Weather w2 ON DATEDIFF(w2.recordDate, w1.recordDate) = 1
# WHERE w1.temperature < w2.temperature

# Without using inner join
# SELECT w2.id
# FROM Weather w1, Weather w2
# WHERE DATEDIFF(w2.recordDate, w1.recordDate) = 1 
#     AND w1.Temperature < w2.Temperature


# Same logic but use "TO_DAYS"
# TO_DAYS(DATE) return the number of days between from year 0 to date DATE
# SELECT w2.id
# FROM Weather w1
# JOIN Weather w2
# ON TO_DAYS(w1.recordDate) + 1 = TO_DAYS(w2.recordDate)
# WHERE w1.Temperature < w2.Temperature


# Same logic but use "SUBDATE"
# MySQL SUBDATE() subtracts a time value (as interval) from a given date.
SELECT w2.id
FROM Weather w1, Weather w2
WHERE SUBDATE(w2.recordDate, 1) = w1.recordDate
    AND w1.Temperature < w2.Temperature
