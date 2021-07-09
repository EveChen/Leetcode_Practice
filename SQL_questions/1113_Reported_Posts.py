
# Link: https://leetcode.com/problems/reported-posts/

# Solution
SELECT extra AS report_reason, COUNT(DISTINCT post_id) AS report_count
FROM Actions
WHERE action_date = '2019-07-04'
    AND action LIKE 'report'
GROUP BY extra
