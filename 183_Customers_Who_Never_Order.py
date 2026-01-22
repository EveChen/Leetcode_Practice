
-- # Method 1: subquery
-- # 缺點: 如果 Orders.customerId 裡含有 NULL 值，NOT IN 可能會失效（回傳空結果）
-- Select name As Customers
-- From Customers c
-- Where id Not In (
--     Select customerId
--     From Orders o
-- )

# Method 2: Left Join A 表有、但 B 表沒有
-- Select name As Customers
-- From Customers c
-- Left Join Orders o
--     On c.id = o.customerId
-- Where o.customerId Is Null

# Method 3: Except，概念是集合 A 減掉集合 B
# 必須: 上下兩個查詢的欄位數量必須一樣，而且會去調重複值 (自動Distinct)
-- 集合 A：所有客戶的名字
-- SELECT name FROM Customers

-- EXCEPT

-- -- 集合 B：所有下過訂單的人的名字
-- SELECT c.name 
-- FROM Customers c 
-- JOIN Orders o ON c.id = o.customerId;

# Method 4: Not Exist 針對每一個客戶，檢查 Orders 表裡是否「不存在」該客戶的紀錄
# 優點: 能正確處理 NULL 值
# 說明: 檢查 Joe (id=1)：在 Orders 找到紀錄了！回傳 1。NOT EXISTS 看到 1，所以排除 Joe。檢查 Henry (id=2)：在 Orders 找不到任何紀錄。NOT EXISTS 沒看到東西，所以保留 Henry。
Select name As Customers
From Customers c
Where Not Exists (
    Select 1
    From Orders o
    Where o.customerId = c.id
)
