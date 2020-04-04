# https://leetcode.com/problems/reverse-string/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Method 1: Use built-in function (violate the problem statement as reverse will create a copy of string)
        return s.reverse()
    
        # Method 2: Use list operation
        # Note: We cannot simply use return s[: : -1] because the problem only allow in-place solution.
        s[:] = s[: : -1]
        return s[:]
        
        # Method 3: Recursion --> why cannot work?! Is it because the problem wants an 'in-place' solution?
        if len(s) < 1:
            return s
        return s[-1] + self.reverseString(s[:-1])
        
        # Method 4: Exchange positions
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    
        
        
