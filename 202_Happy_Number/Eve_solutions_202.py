# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        # Method 1: Use Set
        mem = set()
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            # Case 1: If n has already in mem, we returns false to stop the endless cycle
            if n in mem:
                return False
            else:
                mem.add(n)
            
        return True  


        

        # Method 2: Use Dictionary
        hashmap = {}

        while n != 1:
            n = sum(pow(int(i), 2) for i in str(n))
            if n in hashmap:
                return False
            else:
                hashmap[n] = True # Add a dummy variable to detect endless cycle

        return True
        
