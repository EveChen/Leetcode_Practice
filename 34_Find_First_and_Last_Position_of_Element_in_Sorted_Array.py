https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#Q: 試圖暴力解但答案錯 e.g. nums = [3, 3, 3], target = 3, answer = [0, 2], Eve = [0, 1, 2]

from collections import defaultdict
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        res = []
        
        # Create a hashmap to store {num:[index]}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = list()
                hashmap[nums[i]].append(i)
            hashmap[nums[i]].append(i)
           
        # Case 1: nums list does not exist
        if len(nums) == 0:
            return [-1, -1]
        
        # Case 2: If target is not in nums, e.g. nums = [1, 2, 3], target = 4, return [-1, -1]
        if target not in hashmap.keys():
            return [-1, -1]
        
        # Case 3: If multiple targets are in nums, e.g. nums = [3, 3, 3], target = 3, return [0, 2]
        elif target in hashmap.keys():
            if len(set(hashmap[target])) == 1:
                return [min(hashmap[target]), max(hashmap[target])] #Wrong: return [0, 1, 2]
                
        # Case 4: If two targets are in nums
        for i in range(len(nums)):
            if nums[i] == target:
                if nums[i] in hashmap.keys():
                    res.append(i)
        return res
