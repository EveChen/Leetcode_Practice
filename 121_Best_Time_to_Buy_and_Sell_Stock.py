
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Method: 用一個變量記錄遍歷過數中的最小值，然後每次計算當前值和這個最小值之間的差值最為利潤，然後每次選較大的利潤來更新
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        profit = 0
        minimum = float('inf')
        for p in prices:
            minimum = min(p, minimum)
            
            if p - minimum > profit:
                profit = p - minimum
        return profit


class Solution:
    def maxProfit(self, prices): 
        max_profit = 0
        min_price = float('inf') # 也可以用sys.maxsize
        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
        
# 作法同 Method 1，不過是用min/max built-in functions
# 每一次min_price都有可能被更低的價格所取代
class Solution:
    def maxProfit(self, prices): 
        #find max(prices[j] - prices[i]), for every i and j such that j > i
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        return max_profit
        
        
# Method 2: Brute Force (Time limit exceed)
# Time: O(n^2), Space = O(1)
class Solution:
    def maxProfit(self, prices): 
        max_profit = 0
        for i in range(0, len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
        
        
