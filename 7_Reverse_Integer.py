
# Link: https://leetcode.com/problems/reverse-integer/

# 問題 1: 要怎麼取出個位數、十位數、百位數 etc?
# 用特殊技巧 res = 0, res = res * 10 + x % 10 且 x = x // 10 (注意負數x)，為什麼要注意負數? 看筆記 -123 % 10 = 7
# Solution A: 用特殊方法求個位十位百位數，記得設定flag
# 需要注意overflow/underflow問題: int型的数值范围是 -2147483648～2147483647
# Time = O(n)
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0
        
        flag = 1
        if x < 0:
            flag = -1
            x = -x
         
        rev = 0
        while x != 0:
            rev = rev * 10 + x % 10
            x, mod = divmod(x, 10)
            #x = x // 10
            
		#hint: 必須是 rev * flag 在 [-2**31, 2**31)
        if rev * flag <= -pow(2, 31) or rev * flag >= pow(2, 31):
            return 0
        return rev * flag
        
# # 別人的解法
# class Solution:
#     def reverse(self, x: int) -> int:
#         flag = [1, -1][x < 0]
#         res = flag * int(str(abs(x))[::-1])
#         return res if -(2**31) - 1 < res < 2**31 else 0
    
    
    
    
        
        
        
