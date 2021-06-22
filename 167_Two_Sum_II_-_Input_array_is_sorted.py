
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
# Status: Wrong answer......
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left = i
            right = len(numbers) - 1
            tmp = target - numbers[i]
            
            while left < right:
                mid = left + (left - right) // 2
                if tmp == numbers[mid]: 
                    return [i + 1, mid + 1]
                elif tmp > numbers[mid]:
                    left += 1
                elif tmp < numbers[mid]:
                    right -= 1
                    

