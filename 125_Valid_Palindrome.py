# Problem: https://leetcode.com/problems/valid-palindrome/

# Method 1: Use two pointers
# Time Complexity: O(n)
# Space Complexity: O(?)


class Solution:
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        
        while start < end:
            # Case 1: If the start point is not an alphabet or digit, skip it
            while start < end and not s[start].isalnum():
                start += 1
            # Case 2: If the end point is not an alphabet or digit, skip it
            while start < end and not s[end].isalnum():
                end -= 1
            # Compare two element to see if they match    
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True


# Method 2: Use two pointers (clean the string first)
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def isPalindrome(self, s):
        clean = "".join(ch for ch in s if ch.isalnum()).lower()
        
        start = 0
        end = len(clean) - 1
        while start < end:
            if clean[start] != clean[end]:
                return False
            start += 1
            end -= 1
        return True


# Method 3: Use Regex & built-in function
# Time Complexity: O(n)
# Space Complexity: O(n)
import re


class Solution:
    def isPalindrome(self, s):
        clean = re.sub('[^0-9a-zA-Z]', '', s).lower()
        return clean == clean[: : -1]
