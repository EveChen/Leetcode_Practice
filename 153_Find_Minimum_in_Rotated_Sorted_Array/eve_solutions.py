
# Brute Force - list index out of range
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         for i in range(len(nums)):
#             if nums[i] > nums[i + 1]:
#                 return nums[i + 1]

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         start, end = 0, len(nums) - 1
        
#         while start < end:
#             mid = start + (end - start) // 2
#             if nums[mid] < nums[end]: #如果數組沒有旋轉，則nums[end]一定最大
#                 end = mid #所以要往array的右半邊找
#             else: #數組有旋轉，要往array的左半邊找
#                 start = mid + 1
#         return nums[end]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        start, end = 0, len(nums) - 1
        if nums[end] > nums[0]: #代表array根本沒有旋轉
            return nums[0]
        
        while start < end: #array有旋轉
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]: #mid + 1最小
                return nums[mid + 1]
            
            if nums[mid] < nums[mid - 1]:#mid 最小
                return nums[mid]
            
            if nums[mid] > nums[0]:
                start = mid + 1
            else:
                end = mid - 1
            
                
