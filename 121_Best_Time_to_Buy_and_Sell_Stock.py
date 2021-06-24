
#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Solution A: while loop traverse
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        max_profit = 0
        ind = 0
        
        while ind <= len(prices) - 1:
            if prices[ind] < min_val:
                min_val = prices[ind]

            curr = prices[ind] - min_val
            if max_profit < curr:
                max_profit = curr
            ind += 1
        return max_profit
        
# Same way but use for loop
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        max_profit = 0
        
        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
                
            curr_profit = prices[i] - min_val
            if max_profit < curr_profit:
                max_profit = curr_profit
                
        return max_profit
                

# Same way but use built-in functions
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = float('inf')
        
        if len(prices) == 0:
            return 0
        
        for p in prices:
            min_val = min(p, min_val)
            curr_profit = p - min_val
            max_profit = max(max_profit, curr_profit)
            
        return max_profit
            

# Solution B: Brute Force
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:    
#         max_profit = 0
        
#         for i in range(0, len(prices) - 1):
#             for j in range(i+1, len(prices)):
#                 profit = prices[j] - prices[i]
#                 if profit > max_profit:
#                     max_profit = profit
#         return max_profit
    
    
# 問題 1: 怎麼算出當前的 profit? 
# A: 只需要遍歷一次數組，用一個變量記錄遍歷過數中的最小值，然後每次計算當前值和這個最小值之間的差值最為利潤

# 問題 2: 怎麼確保最小值的 index 在當前值的前面?
# A: 當每次遍歷數組找最小值的時候，都會自動更新最小值，因此若list是遞減的，最小值都會跟著變小，等到curr = prices[ind] - min_val 時，prices[ind] 其實就等於 min_val
