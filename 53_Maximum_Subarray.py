
# Link: https://leetcode.com/problems/maximum-subarray/

# Solution A: Kadane's Algorithm, 不追蹤當前儲存的element有哪些，只看current sum
# 思路: 先初始 curr_sum & max_sum = nums[0]，當每次traverse到新的number時，用curr_sum+nums[i]去跟nums[i]比大小，接著比max_sum跟curr_sum的大小。記得edge cases
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         curr_sum = nums[0]
#         max_sum = nums[0]

#         if len(nums) == 0:
#             return 0
#         elif len(nums) == 1:
#             return sum(nums)
        
#         for i in range(1, len(nums)):
#             curr_sum = max(curr_sum + nums[i], nums[i])
#             max_sum = max(curr_sum, max_sum)
#             print("Curr_sum = {}, Max_sum = {}, Index = {}".format(curr_sum, max_sum, i))
#         return max_sum
            

# Solution A.1: CA's solution 還不懂為什麼 c < 0 時要 c = 0 (尤其數組可能所有數字都是負的?)
class Solution(object):
    def maxSubArray(self, nums):
        result = nums[0]
        c = 0
        for num in nums:
            if c < 0:
                c = 0
            c += num
            result = max(result, c)
        return result
				
				# Method 3: 前綴作法，可以執行的懂，但是不懂maxValue和minValue原理
        # 速度快：87%
        # prefix = 0
        # minValue = 0
        # maxValue = -sys.maxsize
        # for i in nums:
        #     prefix += i
        #     maxValue = max(prefix - minValue, maxValue)
        #     minValue = min(prefix, minValue)
        # return maxValue
        
        # Method 2: 另解，但也不太懂
        # 速度快：87%
        # Q: 為什麼for loop從1開始？為什麼nums[i-1]>0就會+=? 這樣有按照順序？
#         for i in range(1, len(nums)):
#             if nums[i - 1] > 0:
#                 nums[i] += nums[i - 1]
#         return max(nums)
           

    
    

# Solution: Brute Force 還不懂
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = -math.inf #-float('inf')
#         for i in range(0, len(nums)):
#             curr_sum = 0
#             for j in range(i, len(nums)):
#                 curr_sum += nums[j]
#                 max_sum = max(max_sum, curr_sum)
#         return max_sum
        
        
        


# Failed
# 原始思路: 先設初始max_val = nums[0]，以及一個空的list，然後traverse nums list。計算新number加上原本max_val是否大於max_val? 若有，就append number 到 list 上繼續traverse，若沒有，就把max_val設定為當前的值
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = nums[0]
#         res = [nums[0]]
#         ind = 1        

#         while ind < len(nums) - 1:
#             res.append(nums[ind])
#             curr_sum = sum(res)
#             if curr_sum < max_sum:
#                 ind += 1
#                 res = []
#             else:
#                 max_sum = curr_sum
#                 ind += 1
#             print("Curr_sum = {}, Max_sum = {}, Index = {}".format(curr_sum, max_sum, ind))
#         return max_sum
