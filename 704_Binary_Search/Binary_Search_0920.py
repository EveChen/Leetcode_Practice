
# Method 1: assume "end" is a candidate
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Case 1: If list of numbers do not exist
        if len(nums) == 0:
            return -1
        
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            # Case 2: If the target is at the midpoint
            if nums[mid] == target:
                return mid
            
            # Case 3: If the target is smaller than the midpoint, then set "end" equals to mid
            elif nums[mid] > target:
                end = mid - 1
                
            # Case 4: If the target is greater than the midpoint, then set "start" equals to mid
            else:
                start = mid + 1
                
        return -1
                


# Assume "end" is not a candidate
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         start, end = 0, len(nums)
        
#         while start < end: # 因為 end 不是候選人，不可能與 start 重合
#             mid = (start + end) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 start = mid + 1
#             else:
#                 end = mid
                
#         return -1

