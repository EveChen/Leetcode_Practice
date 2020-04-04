
# Problem: TLE
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Case 1: If list of numbers do not exist
        if len(nums) == 0:
            return -1
        
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + end // 2
            # Case 2: If the target is at the midpoint
            if nums[mid] == target:
                return mid
            
            # Case 3: If the target is smaller than the midpoint, then set "end" equals to mid
            elif nums[mid] > target:
                end = mid
                
            # Case 4: If the target is greater than the midpoint, then set "start" equals to mid
            else:
                start = mid
                
        #Q: Why not "if nums[end] == target return end?"
        if nums[start] == target:
            return start
        return -1
                
        
