
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# Method 1: Brute Force
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if i != j  and nums[i] > nums[j]:
                    cnt += 1
            res.append(cnt)
        return res
    
# Method 2: Use hashmap - failed
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = dict()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    res[nums[i]] += 1
        return res


# Method 2.1: Revised hashmap
from collections import defaultdict
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = defaultdict(int)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    key = (i, nums[i])
                    res[key] += 1
        
        rex = []
        for ind, val in enumerate(nums):
            key = (ind, val)
            rex.append(res[key])
        return rex            
