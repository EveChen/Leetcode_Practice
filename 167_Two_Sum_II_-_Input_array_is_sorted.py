
#link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# # Solution A: hashmap
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i in range(len(numbers)):
#             if target - numbers[i] in hashmap:
#                 return [hashmap[target - numbers[i]] + 1, i + 1]
#             hashmap[numbers[i]] = i
            
            
# # Solution B: Two pointers
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         left = 0
#         right = len(numbers) - 1
#         while left < right:
#             total = numbers[left] + numbers[right]
#             if total < target:
#                 left += 1
#             elif total > target:
#                 right -= 1
#             elif total == target:
#                 return [left + 1, right + 1]

# Solution C: Binary Search
# 思路: 因為一定有解，而且數組是有序的，那麼第一個數字肯定要小於目標值target，那麼我們每次用二分法來搜索target - numbers[i]即可
# Note: 翻筆記去查為什麼 left = i + 1 且必須 while left <= right
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left = i + 1
            right = len(numbers) - 1
            tmp = target - numbers[i]
            
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    left = mid + 1
                elif numbers[mid] > tmp:
                    right = mid - 1
                    


