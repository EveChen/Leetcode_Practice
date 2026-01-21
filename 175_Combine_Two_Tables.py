
# Method 1: Left join 以左表為主，右表配對不到時補 NULL
-- Select firstName, lastName, city, state
-- From Person As p
--     Left Join Address As a
--     On p.personId = a.personId

# Method 1.2: Using function 當key名稱相同時可使用
-- Select firstName, lastName, city, state
-- From Person
-- Left Join Address Using (personId)

# Method 1.3: Natural left join 直接抓兩張tables中同樣名稱的column名為key，注意有風險
-- Select firstName, lastName, city, state
-- From Person
-- Natural Left Join Address


# Method 2: 用subquery，以主查詢為主，子查詢查不到時補 NULL
# 如果 Address 裡沒有該 ID 的資料，這個查詢結果是「空」，SQL中，「空」結果的欄位填入 Null。
Select firstName, lastName,
    (Select city From Address a Where p.personId = a.personId) As city,
    (Select state From Address a Where p.personId = a.personId) As state
From Person As p

