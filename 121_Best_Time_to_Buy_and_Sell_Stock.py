
# Method 1: Compare minimum price and current profit
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = float('inf')
#         max_profit = 0

#         for i in range(0, len(prices)):
#             if prices[i] < min_price:
#                 min_price = prices[i]
#             else:
#                 current_profit = prices[i] - min_price
#                 if current_profit > max_profit:
#                     max_profit = current_profit
#         return max_profit


# Method 1.1: More concise way
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = float('inf')
#         max_profit = 0

#         for price in prices:
#             if price < min_price:
#                 min_price = price
#             else:
#                 current_profit = price - min_price
#                 if current_profit > max_profit:
#                     max_profit = current_profit
#         return max_profit

# Method 1.2: Similar as method 1
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         current_min = float('inf')
#         max_profit = 0

#         for i in range(0, len(prices)):
#             if prices[i] < current_min:
#                 current_min = prices[i]
            
#             current_profit = prices[i] - current_min
#             if current_profit > max_profit:
#                 max_profit = current_profit
#         return max_profit

# Method 1.3: Same logic but use while loop
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = float('inf')
        max_profit = 0
        index = 0

        while index <= len(prices) - 1:
            if prices[index] < current_min:
                current_min = prices[index]
            
            current_profit = prices[index] - current_min
            if current_profit > max_profit:
                max_profit = current_profit
            index += 1
        return max_profit



# Method 2: Use built-in function
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         current_min = float('inf')
#         max_profit = 0

#         for price in prices:
#             current_min = min(price, current_min)
#             max_profit = max(price - current_min, max_profit)
#         return max_profit




# Wrong because these codes treat as if I can buy/sell multiple times
# e.g. [7, 1, 5, 3, 6, 4] --> 5 - 1 = 4 & 6 - 3 = 3, 4 + 3 = 7
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         result = 0

#         for i in range(0, len(prices) - 1):
#             if prices[i] < prices[i + 1]:
#                 result += prices[i + 1] - prices[i]
#         return result

# Wrong: reason same as above
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         result = 0

#         if len(prices) == 1:
#             result = 0
#         else:
#             for i in range(1, len(prices)):
#                 if prices[i] > prices[i - 1]:
#                     result += prices[i] - prices[i - 1]
#             return result



