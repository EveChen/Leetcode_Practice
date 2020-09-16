
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        res, carry = [], 0
        
        while num1 or num2:
            x1 = x2 = 0 # Q: Why I need to add this line?
            if num1:
                x1 = ord(num1.pop()) - ord('0')
            if num2:
                x2 = ord(num2.pop()) - ord('0')
            
            carry, remain = divmod(x1 + x2 + carry, 10)
            res.append(remain)
            
        if carry:
            res.append(carry)
        return ''.join(str(x) for x in res[::-1])
