# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

# Solution 1: Two pointers
# Time: O(N)
# Space: O(1) ?
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Find the maximum index of "end"
        current = nums[0]
        end = 0
        for i in range(1, len(nums)):
            if nums[i] >= current:
                current = nums[i]
            else:
                end = i
                
        # Step 2: Find the minimum index of "start"
        current = nums[-1]
        start = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= current:
                current = nums[i]
            else:
                start = i
                
        # Step 3: Find the shortest subarray that needs to be sorted
        if start == end:
            return 0
        return max(end - start + 1, 0)
        



        
# Solution 2: Sorting
# Time: O(Nlog(N)) because each sort is O(log(N))
# Space: O(N) because we copy the original nums?
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sorting = sorted(nums)
        if sorting == nums:
            return 0
        
        # Step 1: find the "start" of the unascending order
        start = min(i for i in range(n) if nums[i] != sorting[i])
        
        # Step 2: find the "end" of the unascending order
        end = max(i for i in range(n) if nums[i] != sorting[i])
        
        # Step 3: Return result
        return end - start + 1
