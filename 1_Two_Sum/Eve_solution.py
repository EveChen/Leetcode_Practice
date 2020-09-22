
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Method: 用hashmap解
        # Time: O(n), We traverse the list containing n elements only once，每個值是O(1)
        # Space: O(n), 我們存了n個值在hashmap中
        hashmap = {}
        for i in range(0, len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i #添加hashmap，這裡不像count一樣是計算個數，而是存值nums[i]和位置i
                                # 其中，nums[i]是map中的index, 而i是map中的value
        return [-1] #之前是寫return [-1, -1] #也可以不加這行
				
				
				
				# Brute Force: time = O(n^2), space = O(1)
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] == target - nums[i]:
        #             return [i, j]
