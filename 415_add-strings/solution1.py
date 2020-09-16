
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        n1 = len(num1) - 1
        n2 = len(num2) - 1
        
        while n1 >= 0 or n2 >= 0:
            x1 = ord(num1[n1]) - ord('0') if n1 >= 0 else 0
            x2 = ord(num2[n2]) - ord('0') if n2 >= 0 else 0
            
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            
            res.append(value)
            n1 -= 1
            n2 -= 1
            
        if carry:
            res.append(carry)
            
        return ''.join(str(x) for x in res[::-1])
            
