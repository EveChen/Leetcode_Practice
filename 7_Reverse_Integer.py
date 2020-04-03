
# https://leetcode.com/problems/reverse-integer/

# Q: 為什麼 Time Complexity 是 O(log(x))，是因為 x = x // 10 嗎？
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        
        rev = 0
        while x != 0:
            rev = rev * 10 + x % 10
            x = x // 10
            
        if flag * rev <= -pow(2, 31) or flag * rev >= pow(2, 31): #Q: 不懂官方解答對於 Overflow 的解說 
            return 0                                               
        return rev * flag #有人最後三行直接寫 return rev * flag if -(2**31) - 1 < rev * flag < 2**31 else 0
                          #Q: 為什麼是 -(2**31) - 1? 我以為是 -(2**31) < rev * flag < 2**31
                          #Q: 也不懂另種寫法 if rev > 2**31 + 1 or rev < -2**31 - 1 return 0
        
# 別人的解法
class Solution:
    def reverse(self, x: int) -> int:
        flag = [1, -1][x < 0]
        res = flag * int(str(abs(x))[::-1])
        return res if -(2**31) - 1 < res < 2**31 else 0
    
    
