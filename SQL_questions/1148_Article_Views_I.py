

# 1. My solution
# Select author_id As id
# From Views v
# Where author_id = viewer_id
# Group By author_id
# Order By author_id ASC


# 2. Use distinct
# Select distinct author_id As id
# From Views
# Where author_id = viewer_id
# Order By id ASC


# 3. Use "having" instead of "where"
Select author_id As id
From Views
Group By author_id
Having Sum(If(author_id = viewer_id, 1, 0)) > 0
Order By id Asc
