
# 1. Modified solution - delete duplicate rows in a subquery first (wrong after submit)
# Select viewer_id As id
# From (
#     Select *
#     From Views
#     Group By article_id, author_id, viewer_id, view_date
#     ) As tmp
# Group By view_date
# Having Count(viewer_id) > 1
# Order By id Asc


# 2. Other people's solution - use distinct + group by two columns
# https://leetcode.com/problems/article-views-ii/discuss/373144/Very-simple-MYSQL-no-JOIN
Select Distinct viewer_id As id
From Views
Group By viewer_id, view_date
Having Count(Distinct article_id) > 1 #must add "distinct" to avoid duplicate row
Order By id Asc


# 3. Other people's solution - having count
# https://leetcode.com/problems/article-views-ii/discuss/397880/Easy-MySQL-Solutions-with-Explanation
# Select Distinct viewer_id As id
# From (Select distinct * From Views) As tmp  # remove duplicate rows
# Group By viewer_id
# Having Count(Distinct view_date) != Count(view_date)
# Order By id Asc


# 4. Other people's solution - self join
# https://leetcode.com/problems/article-views-ii/discuss/363022/MSSQL-Self-Join
# Select distinct v1.viewer_id As id
# From Views v1
#     Join Views v2
#     On v1.view_date = v2.view_date
#     And v1.viewer_id = v2.viewer_id
#     And v1.article_id != v2.article_id
# Order By id Asc



###########################


# 2. My solution (wrong) - {"headers": ["id"], "values": [[1], [4], [5], [6], [7]]}
# Select v1.viewer_id As id
# From Views v1
#     Join Views v2
#     On v1.view_date = v2.view_date
# Group By v1.viewer_id
# Having Count(*) > 0
# Order By id Asc



# 3. Modified Solution (Wrong) - [{"headers": ["id"], "values": [[5], [7]]}]
# Select v1.viewer_id As id
# From Views v1
#     Join Views v2
#     On v1.view_date = v2.view_date
#         And v1.viewer_id != v2.viewer_id
# Group By v1.viewer_id
# Having Count(*) > 0
# Order By id Asc


# 4. Modified solution (wrong) - [[4], [5], [6]] because #4 is a duplicate row
# Select viewer_id As id
# From Views
# Group By view_date
# Having Count(viewer_id) > 1
# Order By id Asc




