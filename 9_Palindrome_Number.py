
# https://leetcode.com/problems/palindrome-number/

# Method 1: 將所有數字都翻轉，跟原數字相比，壞處是，容易在翻轉後 overflow
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Case 1: x < 0
        if x < 0:
            return False
        backup = x
        
        # Cases: x > 0, rev = rev * 10 + x % 10
        rev = 0
        while x != 0:
            rev = rev * 10 + x % 10
            x = x // 10
            
        return backup == rev
        
# Method 2: 只翻轉一半數字，比對前半部和後半部一不一致，因為只翻轉一半的數字，故不會造成 overflow 
# 1. 若個數為偶數，則x == rev就是一致，如1221
# 2. 若個數為奇數，那麼看 x == rev / 10，是的話就是一致，如121
# Time = O(log10(n))

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        temp = x
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10
        return x == rev or x == rev // 10
            
# 作弊方法
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x)[::-1] == str(x)
