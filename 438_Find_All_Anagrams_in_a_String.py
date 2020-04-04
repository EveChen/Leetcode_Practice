# https://leetcode.com/problems/find-all-anagrams-in-a-string/

"""
Example 1:
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""

# Eve's solution
from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
      
      # 1. Corner Case
      if len(s) == 0 or len(p) == 0 or len(p) > len(s):
          return []
      
      # 2. Sliding windows
      cntP = Counter(p) # {a: 1, b : 1, c : 1}
      cntS = Counter(s[: len(p) - 1]) # {c : 1, b : 1}
      res = []
      
      for i in range(len(p) - 1, len(s)): # loop starting from i = 2
          startIndex = i - len(p) + 1 # This is the index we want to save to res if it matches the condition. Now startIndex = 2
          cntS[s[i]] += 1 # sliding window moves one step e.g. {c : 1, b : 1, a : 1}
        
          if cntS == cntP: # right now they are the same as {c : 1, b : 1, a : 1}
              res.append(startIndex)
          cntS[s[startIndex]] -= 1 # remove the 0th index from cntS as the attribute of the sliding window. Now cntS = {c : 0, b : 1, a : 1}
        
          if cntS[s[startIndex]] == 0: # Originally it's {c : 0, b : 1, a : 1} and we want to remove the key with the value equals to 0
            del cntS[s[startIndex]]
      
      return res 
        
      
# Test
#s = "cbaebabacd" 
#p = "abc"

#Solution()
# findAnagrams(s, p)

# I don't know how to test without using Leetcode QQ...      
      

      
      
      
      
      
      
      
      
      
