
# https://leetcode.com/problems/valid-parentheses/

# Method 1: 這裡需要用一個棧，開始遍歷輸入字符串，如果當前字符為左半邊括號時，則將其壓入棧中，如果遇到右半邊括號時，若此時棧為空，則直接返回 false，如不為空，則取出棧頂元素，若為對應的左半邊括號，則繼續循環，反之返回 false
# Q: 搞不清楚 if/elif 有哪幾種可能...QAQ

class Solution:
    def isValid(self, s: str) -> bool:
        # Create a dictionary and an empty stack
        hashmap = {')' : '(', ']' : '[', '}' : '{'}
        stack = []
        
        # 第一種 if/elif/else 寫法
        for p in s:
            if p not in hashmap:
                stack.append(p)
            elif p in hashmap:
                if len(stack) == 0:
                    return False
                elif hashmap[p] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack #Q: 這個 return 的位置是在 for loop 之下? 
    
    
    
# # 同 Method 1: 同樣邏輯，但是不同 if/elif/else 寫法
class Solution:
    def isValid(self, s: str) -> bool:
        # Create a dictionary and an empty stack
        hashmap = {')' : '(', ']' : '[', '}' : '{'}
        stack = []
    
        for p in s:
            if p not in hashmap:
                stack.append(p)
            elif p in hashmap:
                if len(stack) != 0 and hashmap[p] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(p)
        return not stack #Q: 這個 return 的位置是在 for loop 之下? 
    
# 同 Method 1 但不同 if/elif/else 寫法
class Solution:
    def isValid(self, s):
        stack = []
        hashmap = {'}' : '{', ')' : '(', ']' : '['}
        for p in s:
            if p in hashmap: #case1: 遍歷到} or ) or ]
                left_parethsis = stack.pop() if stack else '#'
                if left_parethsis != hashmap[p]: #left_parethsis e.g. '[', '(', '{'
                    return False                 #hashmap[p]: '{', '[', '('
            else: # case2: 遍歷到{ or ( or [ or 其他符號
                stack.append(p)
        return not stack

    
    
# Method 2: CA 的漂漂解法 (不同的 if/elif/else 邏輯 @@)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for p in s:
            if p in ['[', '{', '(']:
                stack.append(p)
            elif len(stack) == 0:
                return False
            else: # p in [']', '}', ')']
                num = stack.pop()
                s = num + p
                if s not in ['[]', '{}', '()']:
                    return False
        return len(stack) == 0
                
