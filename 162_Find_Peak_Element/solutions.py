
# 只要找到局部的最大值即可
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         start, end = 0, len(nums) - 1
        
#         if len(nums) == 1: #當nums只有一個數，則這個數就是peak
#             return 0
        
#         while start < end:
#             mid = start + (end - start) // 2
#             if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]: # peak是比兩邊都大的數
#                 return mid
#             elif nums[mid] < nums[mid + 1]:
#                 start = mid + 1
#             else:
#                 end = mid
#         return end # 如果是[1, 2, 3, 4]，已經在15th把end = mid，故return end


# Leetcode's solution - iteration
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 0
#         start, end = 0, len(nums) - 1
        
#         while start < end:
#             mid = start + (end - start) // 2
#             if nums[mid] > nums[mid + 1]:
#                 end = mid
#             else:
#                 start = mid + 1
#         return end  
    
    
    
# Leetcode's solution - recursion
class Solution:
    def search(self, nums, start, end):
            if start == end:
                return start
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]: #此時要把end = mid
                return self.search(nums, 0, mid)
            else: #這時候nums[mid] < nums[mid + 1]，在山峰的左邊，故把start = mid + 1
                return self.search(nums, mid + 1, end) 
            
    def findPeakElement(self, nums: List[int]) -> int:
        return self.search(nums, 0, len(nums) - 1)
    
        

