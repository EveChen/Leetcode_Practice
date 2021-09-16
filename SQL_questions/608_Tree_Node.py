

# Wrong 1
# SELECT id, (CASE
#                 WHEN p_id IS NULL THEN 'Root'
#                 WHEN id = leaf_id THEN 'Leaf'
#                 ELSE 'Inner'
#             END) AS Type
# FROM tree, (SELECT id AS leaf_id
#            FROM tree
#            WHERE p_id IN id AND id NOT IN p_id) AS tmp
# ORDER BY id ASC

# Wrong 2
# SELECT id
# FROM tree
# WHERE p_id IN (SELECT id FROM tree) # return id = 2, 3, 4, 5
#     AND id NOT IN (SELECT p_id FROM tree) # return null


# <Break Down>
# 找 Inner or leaf
# SELECT id AS 'inner_or_leaf'
# FROM tree
# WHERE p_id IN (SELECT DISTINCT id FROM tree)

# Note: 記得不能這樣寫
# SELECT id
# FROM tree
# WHERE id IN p_id


# <Break Down>
# 找 inner: id 在 p_id 中，但該 id 並不是 root
# SELECT id
# FROM tree
# WHERE p_id IS NOT NULL AND id IN (SELECT p_id FROM tree)


# Solution A - CASE WHEN
# 1. 判斷是否有parent node --> 沒有的話就是root
# 2. 判斷id是否存在於p_id中，如果有，就是inner node
# 3. 其他都是leaf
# SELECT id, (CASE
#                 WHEN p_id IS NULL THEN 'Root'
#                 WHEN p_id IS NOT NULL AND id IN (SELECT p_id FROM tree) THEN 'Inner'
#                 ELSE 'Leaf'
#            END) AS Type
# FROM tree           
           

# 同 Solution A
# SELECT id, (CASE WHEN ISNULL(p_id) THEN 'Root'
#                 WHEN id IN (SELECT p_id FROM tree) THEN 'Inner'
#                 ELSE 'Leaf'
#             END) AS 'Type'
# FROM tree
# ORDER BY id


# 同上面的做法
SELECT id,
    CASE 
        WHEN t1.id = (SELECT t2.id FROM tree t2 WHERE t2.p_id IS NULL) THEN 'Root'
        WHEN t1.id IN (SELECT t2.p_id FROM tree t2) THEN 'Inner'
        ELSE 'Leaf'
    END AS 'Type'
FROM tree t1
ORDER BY id

# Solution B: 概念一樣，但用雙層IF來做
# SELECT id,
#     IF(ISNULL(t1.p_id), 'Root', 
#       IF(t1.id IN (SELECT p_id FROM tree), 'Inner', 'Leaf')) AS 'Type'
# FROM tree t1
# ORDER BY id
           
           
