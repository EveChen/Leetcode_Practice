
# https://leetcode.com/problems/longest-common-prefix/

        # Method 1
        # Time: O(len(strs) x len(shortest))?
        # Space: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        shortest = min(strs, key = len) # example 1 will return "flow"
        for i, ch in enumerate(shortest):
            for word in strs:
                if word[i] != ch:
                    return shortest[:i]
        return shortest
       
        # Method 2: Don't know why cannot pass Leetcode test
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs)
        
        for i in range(len(shortest)):
            for word in strs:
                if word[i] != shortest[i]:
                    return shortest[:i]
        return shortest
    
    
    
        # Method 3: Use zip
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i, ch in enumerate(zip(*strs)):
            if len(set(ch)) > 1: # means there's at least one common prefix 
                return strs[0][:i]
        return min(strs)

    
    
        # Method 4: Use zip (similar way)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = ""
        
        for i in zip(*[list(i) for i in strs]): # e.g. ('f', 'f', 'f')
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix
        
        

        # Method 5: Built-in function
import os
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return os.path.commonprefix(strs)



    
