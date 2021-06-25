
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# 原始思路: 先找 min_val，算出 curr_profit，只要 curr_profit > 0 就加到 max_profit 上；接著 min_val 歸零，換找下一個 min_val，重複找下一個 curr_profit，若 > 0 就再累加到 max_profit 上。
# 問題 1: 如何在 buy -> sell 結束後重來? 例如現在 min_val = 1, 如何重置 min_val 當 ind = 3 的時候 min_val 變成 3 而非 1?
# A: 重置 min_val = prices[ind] (當前遍歷的數)
# Solution A: From myself
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         min_val = float('inf')
#         ind = 0
        
#         while ind <= len(prices) - 1:
#             if min_val > prices[ind]:
#                 min_val = prices[ind]
                
#             curr_profit = prices[ind] - min_val
#             if curr_profit > 0:
#                 max_profit += curr_profit
#                 min_val = prices[ind] # 重要的一步，要重置 min_val
#             # print("MAX: {} and ind = {}".format(max_profit, ind))
#             ind += 1
#         return max_profit


# Same solution: Use for loop
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_val = float('inf')
#         max_profit = 0
        
#         for p in prices:
#             if min_val > p:
#                 min_val = p
#             curr_profit = p - min_val
            
#             if curr_profit > 0:
#                 max_profit += curr_profit
#                 min_val = p
#         return max_profit
            

# Solution B
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                max_profit += prices[i + 1] - prices[i]
                
        return max_profit
    


        
