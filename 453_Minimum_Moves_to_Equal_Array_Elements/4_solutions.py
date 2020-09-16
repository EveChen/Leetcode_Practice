
# Method 1: can pass the run code result but TLE - Eve's version
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
    
        while len(set(nums)) != 1:
            nums = sorted(nums)
            for i in range(n - 1):
                nums[i] += 1
            total += 1
        return total

# Method 2: Time Limit Exceeded - ca's version
from collections import Counter
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        total = 0
        dist = Counter(nums)
        
        if len(nums) == 1:
            return 0
        
        while len(dist) != 1:
            max_num = max(nums)
            n_max_num = dist[max_num]
            
            # Case 1: If we have only one maximum number, skip it but add 1 to the other keys
            if dist[max_num] == 1:
                # dist.update({dist[nums[i]]: dist[nums[i]] + 1})
                dist = {k+1: v for k, v in dist.items() if k != max_num}
                if max_num in dist:
                    dist[max_num] += 1
                else:
                    dist[max_num] = 1
                    
            # Case 2: If we have over two maximum number, add 1 to one of the maximum number and add 1 to the rest of the elements
            else: # if dist[max_num] > 1
                dist = {k+1:v for k, v in dist.items() if k != max_num}
                if max_num in dist:
                    dist[max_num] += 1
                    dist[max_num + 1] = n_max_num - 1
                else:
                    dist[max_num] = 1
                    dist[max_num + 1] = n_max_num - 1
                
            total += 1
        return total

    #   看最大減一在不在，不在的話，dist[max_num] = 1；如果在的話，那就是 dist[max_num] += 1
# [5, 7, 7, 7] -- > [6, 8, 8, 7]  --> [6, 7, 8, 8] --> [7, 8, 9, 8] --> sort
# --> [7, 8, 8, 9] --> [8, 9, 9, 9] --> [9, 10, 10, 9] --> sort [9, 9, 10, 10]
# --> [10, 10, 11, 10] --> sort [10, 10, 10, 11] --> [11, 11, 11, 11]

# Method 3: ca's solution
#key: 大部分的人加一，就等於沒加一那個人不用加一 (就等於這個人被扣一了)
# 要扣幾次後大家才會一樣?
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        distance = []
        
        for i in range(len(nums)):
            distance.append(nums[i] - min_num)
        return sum(distance)
           
# Method 4: One line code
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)
            
