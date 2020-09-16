
# Method 1: Wrong solution
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         hashmap = {}
#         for price, order in enumerate(prices):
#             hashmap[order] = price
        
#         res = []
#         while hashmap:
#             min_num = min(hashmap.keys())
#             max_num = max(hashmap.keys())
#             if hashmap[min_num] < hashmap[max_num]:
#                 res.append(max_num - min_num) # can't do that
#                 hashmap.pop(min_num)
#                 hashmap.pop(max_num)
#         return sum(res)

# Method 2: Eve's solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        if len(prices) == 1:
            res = 0
        else:
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
        return res
            
# Method 3: hint in https://www.cnblogs.com/grandyang/p/4280803.html
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i + 1]:
                res += prices[i + 1] - prices[i]
        return res
            
        
