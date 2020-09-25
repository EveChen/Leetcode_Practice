
# from collections import Counter
# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         count = 0
#         for j in J:
#             for s in S:
#                 if s == j:
#                     count += 1
#         return count

# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         res = 0
        
#         for s in S:
#             if s in J:
#                 res += 1
#         return res

# Method: Hashmap
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        hashmap = {}
        for s in S:
            if s not in hashmap:
                hashmap[s] = 1
            else:
                hashmap[s] += 1
        
        res = 0
        for stone in hashmap:
            if stone in J:
                res += hashmap[stone]
        return res
    
# Method: hashmap - collections.Counter
from collections import Counter
class Solution(object):
    def numJewelsInStones(self, J, S):
        count = 0
        jewel = Counter(J)
        
        for s in S:
            if s in jewel:
                count += 1
        return count
        
    
# class Solution(object):
#     def numJewelsInStones(self, J, S):
#         """
#         :type J: str
#         :type S: str
#         :rtype: int
#         """
        # 重點：看短String J在长String S里面的出现频率
        
        # Method 1: Brute Force
        # Speed: 88.51%
        # Time: O(len(S) x len(J)), Space = O(1)
        # return sum(i in J for i in S)

        # Method 2: Hash Set
        # Speed: 88.51%
        # Time: O(len(S) + len(J)), Space = O(len(J))
        # Jset = set(J)
        # return sum(i in Jset for i in S)
    
        # Method 3: map
        # map(J.count, S)會出現[相同的次數]，可是是list，所以用sum處理成number
        # return sum(map(J.count, S))
        
       

        
