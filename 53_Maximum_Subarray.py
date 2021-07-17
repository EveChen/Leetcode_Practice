
# Link: https://leetcode.com/problems/maximum-subarray

# Solution A: 不追蹤當前儲存的element有哪些，只看current sum
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
#             # print("Curr_sum = {}, Max_sum = {}, Index = {}".format(curr_sum, max_sum, i))
#         return max_sum
          
    
# Solution A.1
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = -float('inf') # can also be max_sum = nums[0]
#         curr_sum = 0
        
#         for num in nums:
#             curr_sum = max(curr_sum + num, num)
#             max_sum = max(curr_sum, max_sum)
#         return max_sum


# Solution A.2: CA's solution 
# 問題: 還不懂為什麼 curr_sum < 0 時要 curr_sum = 0 (尤其數組可能所有數字都是負的如 [-2, -1])
# A: 直接用 [-2, -1]去跑跑看就知道了，注意執行的順序，是先判斷 if curr_sum < 0，然後再加上 curr_sum + num，最後才是 max_sum = max(max_sum, curr_sum)
# Key: 注意執行的順序!!!
class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        curr_sum = 0
        
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        return max_sum
				
        
# Solution B: Brute Force 
# 思路: 由 i 加到 j，假設今天有十個數，我們要從第五個加到第七個，則 curr_sum = 0 意思是省略前面第一個到第四個數字。
# 問題: 為什麼 curr_sum = 0 要放在 for i in range...裡? 
# A: 直接用 nums = [-2,1,-3,4,-1,2,1,-5,4] 為例跑跑看
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = -float('inf')
#         for i in range(0, len(nums)):
#             curr_sum = 0 #Q: 為什麼 curr_sum = 0 在這裡?
#             for j in range(i, len(nums)):
#                 curr_sum += nums[j]
#                 max_sum = max(max_sum, curr_sum)
#                 # print("i = {}, j = {}, curr_sum = {}, max_sum = {}".format(i, j, curr_sum, max_sum))
#         return max_sum
        
        
        
# Solution C: 前綴作法，但是不懂maxValue和minValue原理
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         prefix = 0
#         minValue = 0
#         maxValue = -sys.maxsize
#         for i in nums:
#             prefix += i
#             maxValue = max(prefix - minValue, maxValue)
#             minValue = min(prefix, minValue)
#         return maxValue
        
# Solution D: 另解，若前一個數字大於0，那麼現在這個數字nums[i]=nums[i] + nums[i-1]，某種trick? 直接用[-2, 1, -3, 4, -1]可以手動跑得動，但一開始想不到這種做法
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         for i in range(1, len(nums)):
#             if nums[i - 1] > 0:
#                 nums[i] += nums[i - 1]
#         return max(nums)
           

# Solution E: 我自己的想法，但是 Failed QQ
# 原始思路: 先設初始max_val = nums[0]，以及一個空的list，然後traverse nums list。計算新number加上原本max_val是否大於max_val? 若有，就append number 到 list 上繼續traverse，若沒有，就把max_val設定為當前的值
# 問題: 邊界條件有問題，所以[-2, 1]沒辦法跑到最後一個數，試著用for loop重寫
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = nums[0]
#         res = [nums[0]]
#         ind = 0        

#         while ind < len(nums) - 1:
#             curr_sum = sum(res)
#             if curr_sum < 0:
#                 res = []
#                 ind += 1
#             elif curr_sum < max_sum:
#                 ind += 1
#             else:
#                 max_sum = curr_sum
#                 ind += 1
#             res.append(nums[ind])
#             # print("Curr_sum = {}, Max_sum = {}, Index = {}".format(curr_sum, max_sum, ind))
#         return max_sum

# 用For loop寫一樣會 Wrong Answer，死在[-2, -1]或者[1, 2]，應該是邊界條件有問題
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         res = []
#         max_sum = nums[0]
        
# #         if len(nums) == 0:
# #             return 0
# #         elif len(nums) == 1:
# #             return nums[0]
# #         elif len(nums) == 2:
# #             return max(nums)
        
#         for i in range(0, len(nums)):
#             res.append(nums[i])
#             curr_sum = sum(res)
#             if curr_sum < 0:
#                 res = []
#             elif curr_sum < max_sum:
#                 pass
#             else:
#                 max_sum = curr_sum
#             print("i = {}, curr_sum = {}, max_sum = {}, res = {}".format(i, curr_sum, max_sum, res))
#         return max_sum
                

# Solution F: Divide & conquer
# Q: time complexity?
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf # Q: why?

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            # Q: Why still needs these two lines?
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)
        
        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)
                        
                
        
