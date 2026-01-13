
# Method 1: Comparison
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0

#         for i in range(1, len(prices)):
#             if prices[i] > prices[i - 1]:
#                 max_profit += prices[i] - prices[i - 1]
#         return max_profit
    

# Method 1.2: Same logic but use while loop
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         index = 1

#         while index <= len(prices) - 1:
#             if prices[index] > prices[index - 1]:
#                 max_profit += prices[index] - prices[index - 1]
#             index += 1
#         return max_profit


# Method 2: 類似Q 121題目的思路
# 思路: 先找 min_val，算出 curr_profit，只要 curr_profit > 0 就加到 max_profit 上；接著 min_val 歸零，換找下一個 min_val，重複找下一個 curr_profit，若 > 0 就再累加到 max_profit 上。
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         current_min = float('inf')
#         max_profit = 0
#         index = 0

#         while index <= len(prices) - 1:
#             if prices[index] < current_min:
#                 current_min = prices[index]
#             current_profit = prices[index] - current_min
            
#             if current_profit > 0:
#                 max_profit += current_profit
#                 current_min = prices[index]
#             index += 1
#         return max_profit

# Method 2.1: Same logic but use for loop
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         current_min = float('inf')
#         max_profit = 0

#         for price in prices:
#             if price < current_min:
#                 current_min = price
#             current_profit = price - current_min
#             if current_profit > 0:
#                 max_profit += current_profit
#                 current_min = price
#         return max_profit


# Method 3: 不管current_minimum，直接相減、比較
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0

#         for i in range(0, len(prices) - 1):
#             if prices[i + 1] > prices[i]:
#                 max_profit += prices[i + 1] - prices[i]
#         return max_profit

# Method 3.2: Same logic
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
